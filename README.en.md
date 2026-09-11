# DLSSG 310.9.1 for SM86

English | [简体中文](README.zh-CN.md) | [Français](README.fr.md)

Experimental DLSS Frame Generation **310.9.1** adaptation for NVIDIA SM86/RTX 30,
based on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86). One standalone DLL contains
**DirectX 12 + Vulkan**, the MFG temporal correction and four optional optimizations.

## Download 310.9.1-8

**[Download the universal DLL + optional INI](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-8/dlssg-sm86-310.9.1-8-win64.zip)** · [Release notes](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8)

One package, one **`version.dll`**. Choose its filename to suit your installation:

| Filename | Installation |
|---|---|
| `version.dll` | Direct version proxy, the default name. |
| `dxgi.dll` | Rename the same file; direct DXGI proxy, no ASI loader required. |
| `dxgi.asi` | Rename the same file; load it with Ultimate ASI Loader x64. |

**Install only one copy of our bridge.** The ZIP also contains the optional INI,
documentation, checksums and licenses. -8 adds DXGI forwarding and ASI startup to
the corrected -7 runtime and kernels; all four INI options are preserved.

**Earlier -0 through -6 releases were withdrawn
because their X3/X4 images could remain near the motion midpoint despite high FPS.**
In an 8-pixel translation test, old X4 outputs were near 4/4/4 pixels; the corrected
outputs are near 2/4/6. Wukong X4 is now reported substantially smoother on an
**RTX 3070 Ti Laptop GPU, 8 GB**, driver 616.92. This is a correctness fix;
an FPS increase is not promised. The white rectangle over Wukong's benchmark
chart remains a known issue.

The temporal correction is always enabled, including with all INI options off.
See [technical findings, architecture and validation](docs/research.en.md).

## Installation

1. Close the game. Back up the existing `version.dll` and `dlssg_sm86.ini`.
2. Copy `version.dll` beside the actual rendering executable: Wukong
   `b1/Binaries/Win64`.
3. Optionally copy `dlssg_sm86.ini` there. Start the game and compare X2/X3/X4.

If another mod owns `version.dll`, use DXGI or ASI mode and follow the
[generic installation guide](docs/install-loaders.en.md). With Ultimate ASI Loader,
the loader is `version.dll` and our DLL becomes `dxgi.asi`.
Keep the INI named `dlssg_sm86.ini`. These renaming modes require -8;
the original -7 binary must keep its `version.dll` name. Never rename the bridge
to `nvngx_dlssg.dll`.
For rollback, close the game and restore the backed-up files.

Windows x64, an SM86 GPU and an existing DLSS FG game integration are required.
Vulkan additionally needs the NGX extensions and frame presentation supplied by
the game. Copying the DLL does not add FG to an arbitrary game. DX11, Linux/Proton,
DXVK and RTX 20 are not validated. No Python/CUDA installation
is needed to play. Tested driver 616.92 is not a minimum-version requirement.

## Optional optimizations

```ini
[Optimizations]
HardwareBilinear=1
Conv13SharedInput=1
Conv0SharedInput=1
ResidualVectorLoads=1
```

| Option | Effect |
|---|---|
| `HardwareBilinear` | Hardware filtering during final reconstruction; small pixel differences are possible. Related to upstream's [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) option. |
| `Conv13SharedInput` | Reuse one convolution's FP16 inputs in shared memory. |
| `Conv0SharedInput` | Reuse a second reconstruction convolution's FP16 inputs. |
| `ResidualVectorLoads` | Vectorized input reads in two residual convolutions. |

`1` enables and `0` disables an option. Missing file/keys default to `1`.
Restart the game after editing. These settings apply to both APIs; they do not
select X2/X3/X4 or control Neural Rendering / NR Cost Scaler. This bridge reads
its own `[Optimizations]` section, not upstream's native-host settings.
All-zero selects the corrected reference kernels; it does not restore an old DLL.
No FP8, INT8 or neural-quality reduction is included.

## Companion tools and game reports

**Beginners: use [RHI](https://github.com/RankFTW/RHI) to install/manage the companion tools**, following its
instructions, then install this FG DLL. Our laptop tester reports very good
compatibility with [ShortFuse's DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315) and
[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884), also available through RHI.
Discord links may require server membership. The NR patch's RTX20/30/40 support
does not extend this FG bridge's SM86 support.
Please star **[RHI](https://github.com/RankFTW/RHI)** and **[ShortFuse's RenoDX](https://github.com/clshortfuse/renodx)** to support their authors.

| Game | Evidence |
|---|---|
| Black Myth: Wukong / DX12 | Corrected X4 reported much smoother; direct `dxgi.dll` also confirmed working on the laptop. White benchmark chart still present. |
| Palworld | Positive reports on earlier builds; corrected release needs a fresh test. |

Reports so far primarily concern one **laptop**, not desktop GPU benchmarks.
Other configurations are welcome: GPU/VRAM, driver, game/API, resolution, mode,
NR/Cost Scaler settings, motion quality and responsiveness. Use [Issues](https://github.com/SilyNoMeta/dlssg_for_sm86/issues).

## Diagnostics and credits

The DLL embeds the unchanged NVIDIA 310.9.1 runtime and SM86 kernels. It verifies
and caches the runtime under `%LOCALAPPDATA%/DLSSG-SM86/<SHA256>/`; kernels remain
embedded. Its log is `dlssg3109.log` beside the proxy. Vulkan log events confirm
execution, not displayed FPS. A corrupt cache is rejected; with the game closed,
move that cache subfolder aside so it can be recreated.

Thanks to [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) and to the
[RTX40MFG-Unlock temporal correction](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp) by Michael Robles (MIT).
See [third-party notices](THIRD_PARTY_NOTICES.txt) and `SHA256SUMS.txt`.
