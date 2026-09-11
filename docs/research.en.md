# Temporal correctness and shipped optimizations

2026-09-11 · release 310.9.1-7 · [English](research.en.md) / [Français](research.fr.md) / [简体中文](research.zh-CN.md)

## Finding and hypothesis

[Issue #2](https://github.com/SilyNoMeta/dlssg_for_sm86/issues/2) reported 160–170 FPS X4 with poor apparent smoothness
in Cyberpunk and Onimusha on RTX 3060 Ti 8 GB. The maintainer reproduced the
perceived problem in Wukong. The hypothesis was incorrect intermediate image
content despite successful, regularly scheduled frame generation.

We tested a 640×360 scene moving horizontally by 8 pixels per real input frame,
with known motion vectors and constant depth. A red gradient provides an analytic
displacement measurement independent of a GPU/reference DLL. The reset frame is
excluded; three subsequent input-frame groups are scored away from boundaries and UI.

| X4 source | Generated 1 | Generated 2 | Generated 3 |
|---|---:|---:|---:|
| Expected | 2 px | 4 px | 6 px |
| Upstream native 310.1, HardwareBilinear=1 | ~2 px | ~4 px | ~6 px |
| Previous 310.9.1 baseline | ~4 px | ~4 px | ~4 px |
| Corrected 310.9.1-7 | ~2 px | ~4 px | ~6 px |

Old outputs were not byte-identical duplicates. Their hashes differed while
their motion stayed near the midpoint. Previous checks compared them with a
reference using the same MFG unlock, so both could share the defect. Matching
hashes and increasing FPS establish neither independent temporal correctness nor smoothness.

## Mechanism and correction

The SM89 PTX used by this SM86 port contains 104 vector multiplications by 0.5
in `Kernel_EstimateIntermMvecsScatter` (k46). Unlocking the host's frame count
does not make those operations use the supplied per-image time.
For generated index i and n generated frames, t=i/(n+1): the correction replaces
the first 52 vector factors by 1−t and the remaining 52 by t. Half-texel coordinate
offsets are unchanged. It adapts the [RTX40MFG-Unlock transform](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp)
(Michael Robles, MIT), with an exact source-identity check.

One kernel key changes in each 148-key pack. The correction exists in both the
reference and optimized pack and cannot be disabled by the INI. X2 uses t=0.5;
the corrected all-options-off X2 outputs match the old baseline byte for byte.
The model, its weights and FP16 arithmetic are not reduced in precision.

## Validation and its limits

52 offline GPU cases were checked on RTX 3070 Ti Laptop 8 GB, driver 616.92:
49 expected successes and 3 expected failures detecting old X3/X4, including UI.
Coverage includes all 16 INI combinations in X4 on DX12 and Vulkan; X2/X3 with
all options on/off on both APIs; 1280×720; leftward motion; and HUDLess/UIAlpha.
Matched corrected DX12/Vulkan outputs are byte-identical. The displacement
tolerance is 0.5 px because RGBA8 quantization biases X3 thirds by about 0.34 px
even with upstream; the old defect is about 1.33 px in X3 and 2 px in X4.
DLL resources, cold/concurrent/warm cache behavior and corrupt-cache rejection
were also checked. [Machine-readable scope](validation-summary.json).

These tests do not measure game presentation or validate every occlusion,
camera movement, UI format or game integration. The owner then confirmed a
large X4 smoothness improvement in Wukong with this exact DLL. Cyberpunk,
Onimusha/ASI loading and a corrected Vulkan game run remain unconfirmed.
The white Wukong benchmark chart remains visible. A synthetic UI test did not
reproduce it, so the temporal fix is not presented as a fix for that separate symptom.

## Optimizations included in the DLL

| INI option | Mechanism | Evidence and limit |
|---|---|---|
| HardwareBilinear | Hardware sampling in final reconstruction (k60), following upstream's [option](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md). | Small pixel changes possible. Earlier user improvement was marginal; no guaranteed overall gain. |
| Conv13SharedInput | Reuse FP16 convolution inputs in shared memory (k13). | Arithmetic preserved in tested cases; no isolated game-speedup attribution. |
| Conv0SharedInput | Shared input halo in reconstruction convolution k0, preserving Tensor Core operation order. | One synchronized isolated test: 0.792384→0.698168 ms (−11.89%). Whole 1440p X4 blocks were nearly neutral. |
| ResidualVectorLoads | Cooperative vector reads in residual convolutions k5/k11; preserve arithmetic and barriers. | Isolated tests: −2.84% / −6.20% respectively; whole-runtime changes small and inconsistent. |

Isolated kernel measurements predate the temporal correction. They concern
specific dispatches and workloads, not FPS improvements measured for -7.
Earlier output-equivalence tests remain useful for checking an optimization's
arithmetic, but were insufficient to validate MFG motion. FP8, INT8, LZ4 and a
smaller neural model are not part of this release. Toggle optimizations only
to compare the same corrected image-generation path, restarting between runs.

## First game measurements

Wukong 1.0.21.23831, DX12, 2560×1440, High, full ray tracing Low, super resolution
58, strong motion blur; RTX 3070 Ti **Laptop 8 GB**, i9-12900H, driver 616.92.
NR/NR Cost Scaler settings and capture landmark were reported unchanged.
Exact NR values were not recorded in the CSV. One roughly 60-second capture per condition.

| X4 configuration | Displayed FPS | 1% low FPS | Mean PC latency |
|---|---:|---:|---:|
| Upstream native 310.1 | 106.151 | 61.112 | 87.691 ms |
| Old -4 | 103.710 | 72.330 | 88.099 ms |
| Corrected DLL (-7) | 98.064 | 66.295 | 91.377 ms |

**The corrected run had the Codex companion visible, unused, unlike earlier runs.**
The conditions are not strictly matched; these numbers establish neither an
FPS regression caused by the correction nor a speedup. The important new result
is the user's much smoother X4 report, consistent with the independent motion test.
The game's full-run screenshot shows 102 FPS; that is a different interval from
the 60-second FrameView capture and is not substituted for its 98.064 FPS.

[Aggregated capture data](benchmark-summary.csv) includes the initial -0…-4 series
and subsequent original/corrected runs. Source hashes identify captures; no raw
personal logs are published. FPS=1000N/ΣΔt, using MsBetweenDisplayChange. The
1%/0.1% lows invert the mean of the longest ceil(0.01N)/ceil(0.001N) intervals.
Zero intervals and spikes are retained. PC latency is the mean MsPCLatency.
No thousands-of-frames confidence claim is made: frames within a run are not
independent benchmark repetitions. Compare motion and responsiveness alongside
timing, and welcome results from other GPUs and games.

## Traceability

DLL SHA256: `d10fc4d245ddfa0a8b2bd5530dfde23547bf193d6f30623d4875627db1002bef`.
The release DLL is unchanged from the tested temporal candidate.
Previous releases -0…-6 were withdrawn because of the MFG defect; their historical
results are retained for interpretation, not as recommended downloads.
The source methodology and curated aggregates above document this release;
private development logs and test applications are not bundled.
