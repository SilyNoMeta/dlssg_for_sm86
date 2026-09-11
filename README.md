# DLSSG 310.9.1 for SM86

English | [简体中文](README.zh-CN.md) | [Français](README.fr.md)

Experimental adaptation of DLSS Frame Generation **310.9.1** for NVIDIA SM86
GPUs, based on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
Install a single file: **`version.dll`**.


**Start here: [310.9.1-6 — DX12 + Vulkan + configurable optimizations](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-6/dlssg-sm86-310.9.1-6-win64.zip).**
One `version.dll` includes both API paths and all four released optimizations.
The ZIP includes the optional `dlssg_sm86.ini`. All four options default to on.
Use the profiles below to compare earlier kernel combinations without swapping DLLs.
This is an experimental prerelease; a higher revision does not guarantee higher FPS.

## Choose a version

All versions use DLSSG 310.9.1 and install with one `version.dll`.
**Try the variants in the same scene and keep the one that suits you best.**
A higher revision number does not guarantee higher FPS or a better feel.

| Version / download | Main difference | What to expect |
|---|---|---|
| [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0) | Baseline with manual bilinear interpolation. | Reference for comparing image reconstruction. |
| [310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1) | Hardware bilinear filtering for final reconstruction. | Small pixel differences are possible; a marginal improvement was reported. |
| [310.9.1-2](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-2) | Everything in `-1`, plus FP16 input reuse in one convolution. | Tested in games by one user; no obvious visual issue reported, improvement hard to judge. |
| [310.9.1-3](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-3) | Everything in `-2`, plus FP16 input reuse in a second reconstruction convolution. | Offline image checks match `-2`; no consistent total GPU-time improvement established. |
| [310.9.1-4](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-4) | Everything in `-3`, plus vectorized input loads in two residual convolutions. | Offline image checks match `-2`; total GPU-time changes remain small and variable. |
| [310.9.1-5](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-5) | The `-4` kernels, with an optional INI to switch four optimizations on/off. | Same default image path as `-4`; convenient for comparing the earlier kernel combinations. |
| [310.9.1-6](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-6) | **Unified DirectX 12 + Vulkan**, with all four INI switches. | Recommended starting package; same default kernels as `-4`/`-5`, with the Vulkan path added. |

The bilinear optimization adapts the idea of the original project's
[HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) option. It can slightly change pixels versus `-0`.
The later memory-access optimizations preserve FP16 arithmetic. **No FP8 or INT8
is included in these releases.**

Testing so far uses one **RTX 3070 Ti Laptop GPU with 8 GB VRAM**, driver 616.92.
Earlier DX12 versions have user reports from Wukong and Palworld. The same Vulkan
implementation and kernels have a positive No Man's Sky X2/X3/X4 report using a
preview with additional diagnostic logging. Controlled cross-version game
benchmarks are still in progress; no overall speedup is promised.

Exit the game before switching DLLs or settings. Compare image quality,
responsiveness and smoothness, as well as FPS, at identical settings.

### Optional configuration (`-5` / `-6`)

Copy `dlssg_sm86.ini` beside `version.dll`, edit values to `1` (on) or `0` (off),
and fully restart the game. Without the file, or when a key is missing, that
optimization defaults to on. These are this bridge's settings; it does not read
the upstream native-host INI.

```ini
[Optimizations]
HardwareBilinear=1
Conv13SharedInput=1
Conv0SharedInput=1
ResidualVectorLoads=1
```

| Option | What it controls |
|---|---|
| `HardwareBilinear` | Hardware bilinear filtering during final reconstruction; small pixel differences are possible. |
| `Conv13SharedInput` | Shared-memory reuse of FP16 inputs in one convolution. |
| `Conv0SharedInput` | The same reuse in a second reconstruction convolution. |
| `ResidualVectorLoads` | Vectorized input loads in two residual convolutions. |

The INI configures optimizations on both APIs. The game selects DX12 or Vulkan;
there is no API-switch setting here. These switches do not select X2/X3/X4 or
control a separate Neural Rendering / NR Cost Scaler mod.

Kernel combinations for comparison (same image path, not the same DLL binary):

| Profile | HardwareBilinear | Conv13SharedInput | Conv0SharedInput | ResidualVectorLoads |
|---|---:|---:|---:|---:|
| `-0` | 0 | 0 | 0 | 0 |
| `-1` | 1 | 0 | 0 | 0 |
| `-2` | 1 | 1 | 0 | 0 |
| `-3` | 1 | 1 | 1 | 0 |
| `-4` | 1 | 1 | 1 | 1 |

The exact distributed DLL passed fresh offline checks on both APIs, including
all 16 INI combinations and the supplied INI file. Vulkan X2/X3/X4, history
reset/recovery and the DX12 comparison passed. Matched outputs equal their
corresponding reference paths; loading and cache checks also passed.
These checks do not establish compatibility with every game or an FPS gain.

## Requirements

- Windows x64, a Direct3D 12 or native Vulkan game, and an NVIDIA driver providing NGX and the required API extensions.
- SM86 GPU (GeForce RTX 30 family). Tested on a laptop with an RTX 3070 Ti Laptop GPU (**8 GB VRAM**) and driver
  616.92; this is a tested driver, not a minimum driver requirement.
- The game must integrate DLSS Frame Generation and load the `version.dll` proxy.
- X2, X3 and X4 depend on the controls exposed by the game.
- No Python or CUDA Toolkit installation is needed to play.

DirectX 12 and native Vulkan are supported paths in `-6`; older `-0` to `-5`
packages are DX12-only. Vulkan requires a game/integration that already supplies
NGX frame-generation inputs, the required extensions and presentation scheduling.
Copying this DLL into an arbitrary Vulkan game does not add frame generation.
DX11, Linux/Proton, DXVK, SM75/RTX 20 and alternate proxy filenames are not supported
or validated by this release. Custom Vulkan resolver paths remain unverified.


## Installation and updates

### New users: start with RHI and ShortFuse's tools

**We recommend [RHI — ReShade HDR Installer](https://github.com/RankFTW/RHI)
for beginners** to install and manage the companion tools. RHI exposes
ShortFuse DLSS Tool and NR Cost Scaler through its DLSS management interface.
Follow RHI's instructions for your game, then install this release's
`version.dll` using the steps below.

For the earlier versions, our tester reports very good compatibility with
**[ShortFuse's DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315)**
and **[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884)**,
which can also be installed through [RHI](https://github.com/RankFTW/RHI).
The Discord links may require joining the server.

RTX20/30/40 in the NR patch's name describes that companion tool; this frame
generation bridge still targets SM86/RTX 30. This compatibility report applies
to the tested setup.

**Support their authors by giving a star ⭐ to
[RHI](https://github.com/RankFTW/RHI) and [ShortFuse's RenoDX](https://github.com/clshortfuse/renodx)!**

### Install the frame generation bridge

1. Fully exit the game.
2. Back up any existing `version.dll`. If another mod uses this filename, do
   not overwrite it: this release does not chain other proxies.
3. Copy the release's `version.dll` next to the actual rendering executable.
   For Black Myth: Wukong, use `b1/Binaries/Win64`, next to
   `b1-Win64-Shipping.exe`. For No Man's Sky, use `Binaries`, next to `NMS.exe`.
4. Start the game and enable DLSS Frame Generation. Start with X2, then compare
   X3/X4 in the same moving scene.

An INI is optional in `-5` and `-6`; see the configuration section above. The upstream
native-host INI is not read. Do not rename this DLL to
`nvngx_dlssg.dll` or replace the game's original NVIDIA libraries.

When upgrading from the initial two-part 310.9.1 package, back up its old
`version.dll` and `dlssg3109` folder outside the game. Only the new DLL is needed.

## How it works

The proxy embeds the unchanged NVIDIA 310.9.1 runtime and SM86 kernel assets.
On first use it extracts the runtime to
`%LOCALAPPDATA%/DLSSG-SM86/<SHA256>/nvngx_dlssg.dll`, verifies it and reuses that
cache. Kernels are read directly from DLL resources. A corrupt cache is rejected.
The diagnostic log is `dlssg3109.log`, next to the proxy.

This architecture differs from upstream's native 310.1 host. Its settings,
performance figures and GPU routes do not describe this release. Installation
does not automatically change global driver settings or enable DLSS indicators.

## Game reports and limitations

The reports below come from one laptop equipped with an **RTX 3070 Ti Laptop
GPU with 8 GB VRAM**. They should not be taken as desktop GPU results.

| Game | User report |
|---|---|
| Black Myth: Wukong | X2 feels good, X3 acceptable; X4 works but feels poor. |
| Palworld | Works well, including X4; noticeably worse image quality in X4. |
| No Man's Sky (Vulkan) | X2/X3/X4 reported working with the diagnostic preview of this Vulkan path; performance scaling is limited on this laptop. |

These are user reports, not controlled benchmarks or compatibility guarantees.
Higher displayed FPS do not guarantee better responsiveness. Compare motion
artifacts and pacing as well; the exact cause of the reported X4 artifacts has
not been established.

**Reports from other configurations are welcome!** Please share your GPU and
VRAM, laptop or desktop model, driver, game version, output resolution and X2/X3/X4
mode. If using Neural Rendering, include the NR version and NR Cost Scaler setting.
Describe image quality and responsiveness as well as FPS, ideally in the same scene.
Submit feedback through [GitHub Issues](https://github.com/SilyNoMeta/dlssg_for_sm86/issues).

[View the Palworld screenshots and RHI setup](GALLERY.en.md): NR enabled/disabled
and full/reduced NR processing resolution. All supplied gameplay screenshots
show X2; the exact Cost Scaler value is not confirmed.

## Troubleshooting and removal

For Vulkan, `vulkan_backend_active` and `vulkan_kernel_launches` in the log
confirm backend execution; they do not measure displayed FPS. Toxic Commando is
not yet validated. Share the actual renderer and whether FG options are available.

If options are missing, check the executable directory and `dlssg3109.log`.
Exit the game before changing files. If the log reports a corrupt cache, move
the affected subfolder out of `%LOCALAPPDATA%/DLSSG-SM86` so it can be recreated.

To uninstall, remove this release's `version.dll` and restore your backed-up
file if applicable. Its log and DLSSG-SM86 cache can be removed once games using
them are closed.

When reporting a problem, include the game, GPU, driver and selected mode.
Review personal paths before sharing logs.

## Version and credits

`310.9.1-6` uses the 310.9.1 runtime. The DLL checksum is listed in `SHA256SUMS.txt`.

Thanks to [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) for the original
project and SM86 work. See [third-party notices](THIRD_PARTY_NOTICES.txt).
