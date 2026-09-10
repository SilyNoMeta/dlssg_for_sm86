# DLSSG 310.9.1 for SM86

English | [简体中文](README.zh-CN.md) | [Français](README.fr.md)

Experimental adaptation of DLSS Frame Generation **310.9.1** for NVIDIA SM86
GPUs, based on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
Install a single file: **`version.dll`**.

[Download release 310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1)

## What's new in 310.9.1-1

This revision enables **hardware bilinear filtering** in the final output
reconstruction stage. Hardware-filtered texture reads replace manual bilinear
interpolation to reduce work. This is an approximate sampling path: generated
pixels can differ slightly from 310.9.1-0.

It follows the same optimization idea as the original project's
[`HardwareBilinear` option](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md),
with an implementation adapted to our 310.9.1 bridge. Here it is **always enabled**;
there is no INI switch. Use [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)
to return to the previous sampling path.

Our tester reports a **small subjective improvement** on an RTX 3070 Ti Laptop
with 8 GB VRAM. A repeatable overall performance gain has not been established;
results depend on the game and scene. Other configurations' reports are welcome.
X2/X3/X4 passed offline checks. Small differences in synthetic images do not
guarantee identical quality in every game, especially in motion or HDR.

## Requirements

- Windows x64, a Direct3D 12 game and an NVIDIA driver providing NGX/NVAPI.
- SM86 GPU (GeForce RTX 30 family). Tested on a laptop with an RTX 3070 Ti Laptop GPU (**8 GB VRAM**) and driver
  616.92; this is a tested driver, not a minimum driver requirement.
- The game must integrate DLSS Frame Generation and load the `version.dll` proxy.
- X2, X3 and X4 depend on the controls exposed by the game.
- No Python or CUDA Toolkit installation is needed to play.

This release does not provide an SM75/RTX 20 route, Vulkan support or alternate
proxy DLL names.

## Installation and updates

### New users: start with RHI and ShortFuse's tools

**We recommend [RHI — ReShade HDR Installer](https://github.com/RankFTW/RHI)
for beginners** to install and manage the companion tools. RHI exposes
ShortFuse DLSS Tool and NR Cost Scaler through its DLSS management interface.
Follow RHI's instructions for your game, then install this release's
`version.dll` using the steps below.

Our tester reports that this release works very well with
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
   `b1-Win64-Shipping.exe`.
4. Start the game and enable DLSS Frame Generation. Start with X2, then compare
   X3/X4 in the same moving scene.

No INI file is required. Upstream native-host settings, including
`HardwareBilinear`, are not read by this variant. Do not rename this DLL to
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

If options are missing, check the executable directory and `dlssg3109.log`.
Exit the game before changing files. If the log reports a corrupt cache, move
the affected subfolder out of `%LOCALAPPDATA%/DLSSG-SM86` so it can be recreated.

To uninstall, remove this release's `version.dll` and restore your backed-up
file if applicable. Its log and DLSSG-SM86 cache can be removed once games using
them are closed.

When reporting a problem, include the game, GPU, driver and selected mode.
Review personal paths before sharing logs.

## Version and credits

`310.9.1-1` uses the 310.9.1 runtime. The DLL checksum is listed in `SHA256SUMS.txt`.

Thanks to [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) for the original
project and SM86 work. See [third-party notices](THIRD_PARTY_NOTICES.txt).
