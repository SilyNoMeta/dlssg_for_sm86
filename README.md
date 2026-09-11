<div align="center">

<h1>DLSS Frame Generation<br>for RTX 30 Series</h1>
<p>More frames. Better motion. A multiplier that can follow your game.</p>
<p>
<img alt="Release 310.9.1-9" src="https://img.shields.io/badge/release-310.9.1--9-76b900?style=flat-square">
<img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square">
<img alt="DirectX 12 and Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square">
<img alt="SM86" src="https://img.shields.io/badge/GPU-SM86-30363d?style=flat-square">
</p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-9/dlssg-sm86-310.9.1-9-win64.zip">Download 310.9.1-9</a></strong> · <a href="RELEASE-NOTES.md">What's new</a> · <a href="docs/install-loaders.en.md">Installation guide</a></p>
<p><strong>English</strong> · <a href="README.fr.md">Français</a> · <a href="README.zh-CN.md">简体中文</a></p>

</div>

---

Bring **DLSS Frame Generation 310.9.1** to supported **Ampere SM86 / RTX 30-series** GPUs. This experimental adaptation builds on [sdli1995's original project](https://github.com/sdli1995/dlssg_for_sm86), with corrected multi-frame motion, optional optimizations and a single DLL for **DirectX 12 and Vulkan**.

**New in -9:** fixed multipliers up to **X6**, **native Dynamic MFG on compatible DX12 integrations**, and controls in one editable INI. The game still needs an existing DLSS Frame Generation integration.

## What you can do

| Feature | What it means when you play |
|---|---|
| **Choose X2 to X6** | Try more generated frames per rendered frame, within the loaded plugin's capabilities. X4 means one rendered frame plus three generated frames. |
| **Let Dynamic MFG choose** | Give the NVIDIA runtime a target of your choice and let it change the multiplier as the workload changes. Requires compatible DX12 Streamline and driver support. |
| **Get properly spaced motion** | Generated frames occupy different points along the movement. The temporal correction fixes the old “high FPS, poor smoothness” MFG defect and is always active. |
| **Use DX12 or Vulkan** | Both use the same corrected SM86 kernels. Fixed X5/X6 depends on the game's plugin; native Dynamic MFG is DX12-only. |
| **Fit your mod setup** | Keep `version.dll`, rename it to `dxgi.dll`, or use it as an ASI plugin. Same file, same features. |
| **Tune four optimizations** | Enable or disable individual GPU optimizations in an INI. No build tools or CUDA installation needed to play. |

More generated frames can improve visual fluidity, but **X6 is not automatically the best choice**. Responsiveness still depends on the rendered frame rate, and artifacts can become more noticeable at higher factors. Start with X2 or X3, then compare during movement.

## Start here

1. **Download and extract** the [release ZIP](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-9/dlssg-sm86-310.9.1-9-win64.zip).
2. **Close the game and back up** any files you will replace. Copy `version.dll` and `dlssg_sm86.ini` beside the actual game executable. For Wukong, this is `b1/Binaries/Win64`.
3. **Enable DLSS Frame Generation in the game.** The supplied INI leaves the game's mode selection in charge and allows a ceiling of X6 where supported.
4. **Edit the INI** to choose a fixed multiplier or enable Dynamic MFG on compatible games. Restart after configuration changes.

> **New to DLSS modding?** [RHI](https://github.com/RankFTW/RHI) is a convenient starting point for managing DLSS versions and companion tools. Follow its instructions, then install this project's DLL using the steps above.

Already using another mod? Pick one loading method:

| File to install | When to use it |
|---|---|
| `version.dll` | Default direct loading. |
| `dxgi.dll` | Rename the same DLL for direct DXGI loading. No ASI loader needed. |
| `dxgi.asi` | Rename the same DLL and load it with [Ultimate ASI Loader x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader). The loader itself can occupy `version.dll`. |

**Install only one copy of our DLL.** Keep the configuration named `dlssg_sm86.ini`, beside our DLL/ASI. Preserve existing ReShade or other proxies; the [installation guide](docs/install-loaders.en.md) explains coexistence, other ASI names and rollback. Do not rename this file to `nvngx_dlssg.dll`.

## Set it up your way

Edit **`dlssg_sm86.ini`** beside our DLL with a text editor. Choose the settings you want, save, and **restart the game**. The supplied file contains:

```ini
[FrameGeneration]
MaxMultiplier=6
ForceMultiplier=0
DynamicMFG=0
DynamicTargetFPS=0
```

| Setting | What to put in it |
|---|---|
| `MaxMultiplier` | Your ceiling, from **2 to 6**. The loaded plugin must support the requested factor. |
| `ForceMultiplier` | **0** lets the game choose; **2 to your ceiling** requests that fixed multiplier. |
| `DynamicMFG` | **1** requests native dynamic mode on compatible DX12 integrations; **0** leaves it unrequested by our DLL. |
| `DynamicTargetFPS` | **0** uses the display refresh target. Set **your own target FPS** (integer 1–1000) when using dynamic mode. |

**Want a fixed X5?** Set `MaxMultiplier=6`, `ForceMultiplier=5` and `DynamicMFG=0`. For X2, X3, X4 or X6, use that value instead.

**Want automatic adjustment?** Set `DynamicMFG=1` and choose your `DynamicTargetFPS`. With `ForceMultiplier=0`, the game remains the fallback. You can instead choose a fixed fallback, such as `ForceMultiplier=4`, used when dynamic is unavailable and the fixed override is supported.

The target is an aim, **not a guarantee of constant FPS**; VSync can take precedence. FG must be enabled in the game, but the menu does not need a “Dynamic” entry. These settings do not create new menu buttons.

Native dynamic needs a compatible **DX12 Streamline integration and driver**. Fixed overrides also need a recognized Streamline path; direct NGX integrations remain game-controlled. On **Vulkan**, use fixed mode; native dynamic is not enabled there. A game's own native dynamic selection is preserved, including when our dynamic request is off.

**Keeping an older INI?** Add the section above to access these controls. Without it, the defaults are `MaxMultiplier=4` and `0` for the other three keys. The supplied new INI explicitly allows X6 while leaving the game's mode selection in charge.

## Small optimizations, your choice

All four are enabled by default. Set a value to `0` to compare, then restart. Gains can be modest and depend on the workload.

| INI setting | What changes |
|---|---|
| `HardwareBilinear` | Uses hardware filtering for final reconstruction. Small pixel differences are possible. Inspired by the original project's [HardwareBilinear option](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md). |
| `Conv13SharedInput` | Reuses input data in fast shared GPU memory for one convolution. |
| `Conv0SharedInput` | Applies shared-input reuse to another reconstruction convolution. |
| `ResidualVectorLoads` | Groups memory reads in two residual convolutions. |

They live in `[Optimizations]` and apply to both APIs. Missing optimization keys default to `1`. Turning all four off keeps the temporal correction active. They do not change Neural Rendering or NR Cost Scaler settings; no FP8/INT8 mode or smaller neural model is included.

## Compatibility and useful tools

**Windows x64 · supported SM86 GPU · an existing DLSS FG game integration.** The game supplies motion/depth information and presentation. This DLL does not add FG to arbitrary games or provide a DX11 backend. Linux/Proton, DXVK and RTX 20 are not validated.

Native Dynamic MFG has a functional in-game report on an **RTX 3070 Ti Laptop GPU with 8 GB VRAM**, driver **616.92**. That is one laptop configuration, not a claim covering every RTX 30 card or game. The tested driver is not a minimum-version statement. Higher multipliers and dynamic mode depend on the **actually loaded Streamline plugin and driver**, not just the DLL filename.

The tester also reports very good compatibility with **[ShortFuse's DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315)** and **[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884)**, available through RHI. Their NR support does not expand this FG bridge's GPU support. Discord links may require server membership.

If these tools help you, give **[RHI](https://github.com/RankFTW/RHI)** and **[ShortFuse's RenoDX](https://github.com/clshortfuse/renodx)** a star. Their work makes the setup much easier.

## Which version should I try?

| Version | Main difference | Choose it for |
|---|---|---|
| **[310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9)** | Dynamic MFG on compatible DX12 integrations, fixed X5/X6, INI controls, universal loader. | **Start here.** Includes the previous corrections and four optimizations. |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | Corrected X2–X4 with `version.dll` / `dxgi.dll` / ASI loading. | Compare or fall back without the new MFG controls. |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | First release with corrected MFG motion; `version.dll` only. | Historical comparison of the temporal correction. |

Releases -0 through -6 were withdrawn because of incorrect MFG motion. The white rectangle over Wukong's benchmark chart remains a separate known issue.

## Look closer · help improve it

The [technical notes](docs/research.en.md) explain the temporal fix, the new capability-sharing correction, what was tested and what remains unmeasured. For troubleshooting, see the [log guide](docs/install-loaders.en.md#configuration-and-verification). In an available NVIDIA watermark, `Dyn DRV` indicates driver dynamic mode; `4x/6x` means current X4 with an X6 ceiling.

**Reports from other configurations are welcome.** Include GPU/VRAM, driver, game/API, loaded Streamline version, resolution, INI settings and any NR/Cost Scaler settings. Describe motion and responsiveness; FrameView/PresentMon traces are especially useful. [Share a report →](https://github.com/SilyNoMeta/dlssg_for_sm86/issues)

---

Built on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86). Thanks to [Michael Robles / RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) for the temporal correction, [mavismmg / ImDreamt's MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) for the extended/dynamic MFG reference, and [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) for ASI loading. NVIDIA's runtime and assets retain their original rights. [Third-party notices](THIRD_PARTY_NOTICES.txt) · [Checksums](SHA256SUMS.txt)
