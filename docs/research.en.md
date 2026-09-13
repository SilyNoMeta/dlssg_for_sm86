# Temporal correctness and shipped optimizations

## 310.9.1-11: early engine, optional panel

The DLL now limits import interception to the executable, local loader modules and recognized NVIDIA paths. Windows loader exports retain their actual identity when resolved through GetProcAddress. This avoids feeding a bridge wrapper back to an overlay as its original function, which could create recursion.

Import-table interception alone can be bypassed when an overlay rewrites the table and uses saved Windows resolver addresses. A one-shot worker outside DllMain now adds MinHook detours to five loader/resolver APIs, using original trampolines for internal calls. The early import bootstrap remains: worker scheduling does not guarantee interception before every initialization. NvAPI routing distinguishes its public facade from the driver's internal implementation and scopes substitutions to the DLSSG caller. Tests cover repeated simulated overlay takeovers, real NvAPI initialization and native DX12/Vulkan control requests; these are not presentation benchmarks.

The ReShade add-on is a control client, not a second engine. The established model, temporal fix and four performance switches are retained. Optional quality and Blackwell-derived kernel variants are added, disabled by default. Startup tests and isolated control tests do not establish new performance or image-quality results.

Live fixed and dynamic controls now also handle compatible DX12 integrations that submit options without querying capabilities. The bridge makes a bounded capability query when an explicit override needs it. Presentation counts consumed by this query are returned exactly once on the game’s next successful state query; per-viewport fences and status are not replayed. Logging records a bounded number of mode/result transitions, helping distinguish an accepted command from actual generation.

## 310.9.1-10: shared engine, two delivery formats

Both packages embed the same NVIDIA 310.9.1 runtime and corrected multiarch packs. The DLL is the previously tested conventional engine; the standalone add-on links that engine with the ReShade panel. SM86 kernels remain unchanged from -9. The pack adds SM89 compilation of the same FP16 model and an experimental SM75 route; Turing has no physical-card validation here. The earlier sections below describe their original releases and are historical evidence, not new performance measurements.

Live commands are queued and applied on the game's next Streamline options call. Saving settings and saving key bindings are independent operations; a failed file replacement preserves the prior file and active state. ReShade Record reads the runtime's captured input API because ReShade suppresses ordinary Win32 key polling while its menu owns the keyboard.

A target accepted by Streamline can still be overridden by NVIDIA's global/per-game dynamic target setting. The user confirmed that removing such an override restored target changes in Wukong. The add-on does not reset NVIDIA profiles automatically.

Telemetry measures successful unique source-frame submissions over about half a second, not GPU completion or latency. [OptiScaler PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156) adds the consumer; it is pending at release time. [Controls](live-controls.en.md) · [Validation scope](validation-summary.json).

## Historical notes through -9


2026-09-11 · release 310.9.1-9 · [English](research.en.md) / [Français](research.fr.md) / [简体中文](research.zh-CN.md)

## New in -9: higher multipliers and native Dynamic MFG

The provider ceiling is configurable up to five generated frames, or X6 total.
The same temporal correction places generated frame i at t=i/(n+1), including
the new X5/X6 cases. A ceiling does not expand an older game's Streamline arrays:
fixed overrides remain bounded by the recognized plugin and reported capacity.

Native Dynamic MFG uses Streamline's eDynamic options and target frame rate.
It does not introduce a separate frame-pacing loop. Activation requires a known
ABI, the adapted provider, DX12 and a positive dynamic-capability report. FG off
remains off. Rejected or unavailable dynamic requests can fall back to the
configured fixed factor when supported. A game's existing dynamic mode is preserved.

### Why an advertised capability was not enough

An integration can query GetState on viewport 0 and submit SetOptions on viewport 1.
Our initial implementation kept system capabilities inside each viewport's state,
so the second view could wait for support that the first view had already reported.
The fix shares system capabilities across views while keeping presentation counters,
fences and activation state local. Capabilities are cleared on provider/device/API
changes and successful shutdown. A later explicit negative report replaces a positive
one. Versioned copies preserve older game structures; no extra GetState call consumes
the game's presentation counters.

### Evidence for this binary

- 213 control/ABI assertions, including guarded older Options/State buffers.
- 16 fixed-mode GPU cases across DX12 and Vulkan, including X5/X6 and options on/off.
- 10 real Streamline scenarios, including an expected failure on the initial
  implementation and successful capability sharing in the corrected implementation.
- Four Vulkan X2–X6 transition sequences, with one explicit feature creation each;
  temporal-position error remains below 0.403 px on the synthetic test image.
- A functional in-game Dynamic MFG report on RTX 3070 Ti Laptop 8 GB, driver 616.92:
  automatic X3/X4/X5 transitions, a dynamic watermark, and a 130 FPS request accepted.

The game report supplies no new FPS, latency or long-session stability benchmark.
The Vulkan transition tests check generated image content, not swapchain presentation
or internal allocation cost. Streamline 2.14.1 reports no native dynamic capability
under Vulkan, consistent with NVIDIA's [Dynamic MFG guide](https://github.com/NVIDIA-RTX/Streamline/blob/v2.14.1/docs/ProgrammingGuideDLSS_G.md#63-enabling-dynamic-multi-frame-generation).
A separate adaptive Vulkan controller is not included.

The control design was informed by [mavismmg / ImDreamt's MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx),
pinned at 7e613b2aadffe936f2ea19df9c71931bbbbae2e6. Its MIT attribution and the
Streamline header notice are included in the distribution.

The sections below retain the history and scope of earlier temporal/loader tests;
their results are not presented as fresh measurements of every -9 configuration.

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

Release -9 `version.dll` SHA256: `114004043035c3f8f91b1b8909bdb8b7e68fa36394aeb339c339e30042684561`.
This is the exact binary with the new in-game dynamic validation, without a rebuild.
Its embedded runtime and both corrected kernel packs are unchanged from -8;
the new work is in host-side frame-generation controls and capability handling.
Renaming the DLL does not change its hash. Prior named-game results above remain
attributed to their original releases. Releases -0 through -6 were withdrawn.
Only the public technical summary accompanies the binary, not development logs
or test programs. See [validation scope](validation-summary.json).

[DLSS render scale](super-resolution.en.md) · [Release notes](../RELEASE-NOTES.md)
