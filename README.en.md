# DLSSG 310.9.1 for SM86

[Français](README.md) | English

Experimental adaptation of DLSS Frame Generation **310.9.1** for NVIDIA SM86
GPUs, based on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
Install a single file: **`version.dll`**.

[Download release 310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)

## Requirements

- Windows x64, a Direct3D 12 game and an NVIDIA driver providing NGX/NVAPI.
- SM86 GPU (GeForce RTX 30 family). Tested on RTX 3070 Ti Laptop with driver
  616.92; this is a tested driver, not a minimum driver requirement.
- The game must integrate DLSS Frame Generation and load the `version.dll` proxy.
- X2, X3 and X4 depend on the controls exposed by the game.
- No Python or CUDA Toolkit installation is needed to play.

This release does not provide an SM75/RTX 20 route, Vulkan support or alternate
proxy DLL names.

## Installation and updates

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

| Game | User report |
|---|---|
| Black Myth: Wukong | X2 feels good, X3 acceptable; X4 works but feels poor. |
| Palworld | Works well, including X4; noticeably worse image quality in X4. |

These are user reports, not controlled benchmarks or compatibility guarantees.
Higher displayed FPS do not guarantee better responsiveness. Compare motion
artifacts and pacing as well; the exact cause of the reported X4 artifacts has
not been established.

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

`310.9.1-0` means runtime 310.9.1, distribution revision 0. Windows file properties
still show `0.1.0`: this is the exact same binary, without recompilation.
Its checksum is listed in `SHA256SUMS.txt`.

Thanks to [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) for the original
project and SM86 work. See [third-party notices](THIRD_PARTY_NOTICES.txt).
