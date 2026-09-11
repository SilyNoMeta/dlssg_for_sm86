# Temporal correctness and shipped optimizations

2026-09-11 · release 310.9.1-8 · [English](research.en.md) / [Français](research.fr.md) / [简体中文](research.zh-CN.md)

## Finding and hypothesis

[Issue #2](https://github.com/SilyNoMeta/dlssg_for_sm86/issues/2) reported 160–170 FPS X4 with poor apparent smoothness
on RTX 3060 Ti 8 GB. The maintainer reproduced the
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

The -7 temporal fix was checked in 52 offline GPU cases on RTX 3070 Ti Laptop 8 GB, driver 616.92:
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
large X4 smoothness improvement in Wukong with that -7 binary.
A corrected Vulkan game run remains unconfirmed for this release.
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

## Loader integration: loading is not initialization

In the original -7 binary, only `version.dll` triggers automatic startup. An ASI loader can
successfully map a renamed DLL without activating its bridge. This is separate
from the X3/X4 interpolation timing defect.

Release -8 adds one idempotent startup path for three modes in the same binary:
`version.dll` forwards version-information functions; `dxgi.asi` starts on load
and exposes `InitializeASI`; `dxgi.dll` forwards the real Windows DXGI exports.
Ultimate ASI Loader also calls `InitializeASI` for other `.asi` filenames, so
activation no longer depends on the special `dxgi.asi` name.

With UAL, `version.dll` is the loader and `dxgi.asi` is our bridge: two different
binaries. Install only one bridge copy. Its configuration is always
`dlssg_sm86.ini`, beside the bridge, regardless of the selected filename.

The DXGI proxy loads the real library by its absolute system-directory path,
preventing recursion into itself. Forwarding preserves integer, floating-point
and stack arguments and returns Windows' COM objects unchanged. Real DXGI is
loaded on the first export call, outside our `DllMain`; Microsoft documents that
[factory creation from DllMain fails](https://learn.microsoft.com/en-us/windows/win32/api/dxgi/nf-dxgi-createdxgifactory).
Atomic publication handles concurrent first calls without accumulating extra
module references. Export names and ordinals are compared with the tested Windows
library, and real factory creation is tested separately.

**The -8 package supplies one `version.dll`, which can be renamed for these modes.**
The 20 DXGI exports, three factory APIs, concurrent first calls, static imports,
version forwarding and actual UAL startup pass automated checks. Across four X4
cases (DX12 under three names and Vulkan under `dxgi.dll`), all 12 output images
per case match the standard -7 byte for byte. The owner then confirmed direct
`dxgi.dll` operation in Wukong on RTX 3070 Ti Laptop 8 GB. This is a functional
validation, not a new FPS benchmark or a claim covering all games.
A successful startup event alone does not prove the game presents generated frames.

## One set of kernels, two graphics APIs

Both backends retain the 310.9.1 host graph and weights. DX12 intercepts NvAPI
compute-kernel creation; Vulkan adapts NVX CUDA-module creation and launch calls.
Both substitute verified SM86 images from the same corrected packs. The API
connection changes, while neural arithmetic and temporal correction stay shared.
The game still supplies motion/depth resources and frame presentation. Renaming
a DLL cannot provide a missing game integration or add a DX11 backend.

## Traceability

`version.dll` SHA256: `a19c3b7b65d3e485674377c8b2c8d71407179d7da314c6f9ccd691b03951fe75`.
This is the exact binary validated in Wukong as `dxgi.dll`, with no rebuild.
Renaming it does not change its hash. Its runtime and both embedded kernel packs
match -7; the change is in loader integration.
Previous releases -0…-6 were withdrawn because of the MFG defect; their historical
results are retained for interpretation, not as recommended downloads.
The mechanisms and validation above document this release;
private development logs and test applications are not bundled.
