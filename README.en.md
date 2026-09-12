<div align="center">

<h1>DLSS Frame Generation</h1>
<p>Your frames. Your settings. Now with live ReShade controls.</p>
<p><img alt="310.9.1-10" src="https://img.shields.io/badge/release-310.9.1--10-76b900?style=flat-square"> <img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square"> <img alt="DX12 and Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square"></p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-10/dlssg-310.9.1-10-dll-win64.zip">Download DLL / ASI</a> · <a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-10/dlssg-310.9.1-10-reshade-win64.zip">Download ReShade add-on</a></strong></p>
<p><a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.zh-CN.md">简体中文</a></p>

</div>

---


**310.9.1-10 brings two ways to use the same compatibility engine:** a conventional DLL, or a standalone ReShade add-on with controls you can change while playing. Built on [sdli1995's original project](https://github.com/sdli1995/dlssg_for_sm86).

## Pick one package

| Package | Best for | Install |
|---|---|---|
| **DLL / ASI** | A compact setup, INI settings and optional hotkeys. ReShade is not required. | `version.dll` + `dlssg_sm86.ini` |
| **ReShade** | A panel for live multipliers, Dynamic MFG, shortcut recording and saving settings. | `DLSSG.addon64` + `dlssg_sm86.ini`, with ReShade full add-on support |

**Choose one, not both.** The add-on already contains the engine. No extra project DLL/ASI or `DLSSGControls.addon64` is needed. Neither ZIP bundles ReShade or OptiScaler.

Close the game, back up existing files, and install beside the actual executable (Wukong: `b1/Binaries/Win64`). Enable DLSS Frame Generation in the game. Keep existing ReShade, loaders and unrelated add-ons; remove only this project's previous engine when switching packages. Keep your own INI after checking the migration below.

[DLL / ASI installation](docs/install-loaders.en.md) · [ReShade installation and panel](docs/standalone-reshade.en.md)

## What you can do

| Feature | In practice |
|---|---|
| **X2–X6** | Choose a fixed multiplier within the loaded plugin's support. X4 is one rendered frame plus three generated frames. |
| **Native Dynamic MFG** | Choose a target and let NVIDIA adjust the multiplier on compatible **DX12** integrations. |
| **Live controls** | Use optional hotkeys in either package. ReShade also offers a panel, key recording and separate save buttons. |
| **DX12 + Vulkan** | Shared compatibility engine and corrected temporal motion. Vulkan supports fixed controls on recognized Streamline paths; native dynamic remains DX12-only. |
| **RTX 30 / RTX 40** | SM86 and SM89 kernels, with user reports on RTX 3070 Ti Laptop 8 GB and RTX 4090. **RTX 20 / SM75 is experimental and not yet tested on a physical Turing card.** |
| **Optional telemetry** | Expose CPU source-frame cadence to a compatible consumer; see the OptiScaler status below. |

Higher multipliers are not always better: rendered FPS still matters for responsiveness, and motion artifacts can increase. This requires an existing DLSS FG integration; it does not add FG to arbitrary games or provide a DX11 backend. Direct NGX integrations remain game-controlled. No new FPS benchmark is claimed for this release.

## Your INI, your choices

```ini
[FrameGeneration]
MaxInterpolatedFrames=5
ForceMultiplier=0
DynamicMFG=0
DynamicTargetFPS=0
```

- **`MaxInterpolatedFrames`** counts generated frames: **1–5 = X2–X6**, default 5. Setting 1 retains X2 and its necessary patches.
- **`ForceMultiplier`** uses the displayed multiplier: 0 follows the game; 2–6 requests a fixed factor, within the ceiling.
- **`DynamicMFG=1`** requests native dynamic mode. **`DynamicTargetFPS`** accepts 1–1000; 0 uses the display target. No preset target is imposed.
- **`[Logging] Enabled=0`** disables our log; default 1. Existing logs are preserved.
- **`[Telemetry] Enabled=1`** enables source cadence; default 0.

**Upgrading:** replace `MaxMultiplier=M` with `MaxInterpolatedFrames=M-1` (for example, 6 becomes 5). The old ceiling key is no longer read. `ForceMultiplier` keeps its old meaning. In `[Hotkeys]`, the dynamic action is `ActivateDynamicMFG`; keep the startup switch `DynamicMFG` in `[FrameGeneration]`.

Manual INI changes require a restart. ReShade's **Apply for this session** is temporary; **Apply & save settings** persists the mode and target. **Record** captures a shortcut, and **Save keyboard shortcuts** saves bindings independently. There are **no default hotkeys**. [All controls and key syntax](docs/live-controls.en.md).

**Target ignored?** NVIDIA's **Override DLSSG Target Frame Rate**, global or per-game, can override even a target accepted by Streamline. Disable the relevant override if you want the panel to control it, then restart. This is distinct from the ordinary FPS limiter and VSync. A DMFG target is not a guaranteed FPS cap. The dynamic hotkey uses the saved INI target; save your target if you want to reuse it through that shortcut.

## Four optional optimizations

All default to 1 under `[Optimizations]`; set individual options to 0 and restart to compare. Gains are workload-dependent and can be modest. The temporal correction remains active with all four disabled.

| Key | Purpose |
|---|---|
| `HardwareBilinear` | Hardware filtering for reconstruction, inspired by the [original option](https://github.com/sdli1995/dlssg_for_sm86/blob/main/docs/NATIVE_INI.md); small pixel differences are possible. |
| `Conv13SharedInput` | Reuse convolution input in shared GPU memory. |
| `Conv0SharedInput` | Shared-input reuse in another convolution. |
| `ResidualVectorLoads` | Group memory reads in residual convolutions. |

Ada uses the same FP16 model with SM89 compilation; no FP8/INT8 acceleration or smaller model is included. [Technical history and validation](docs/research.en.md).

## OptiScaler and companion tools

**OptiScaler support is awaiting [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156).** The producer is included here, but a consumer build containing that change is required. Turning telemetry on alone will not update an older OptiScaler. The reading is CPU source-frame submission cadence, not GPU completion or latency. Our ReShade panel can display it independently when available.

New to DLSS modding? Start with **[RHI](https://github.com/RankFTW/RHI)** for managing DLSS and companion tools, then choose one package above. The tester reports very good compatibility with ShortFuse's [DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315) and [Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884), also available through RHI. Their NR support is separate from this project's FG compatibility. Give [RHI](https://github.com/RankFTW/RHI) and [ShortFuse's RenoDX](https://github.com/clshortfuse/renodx) a star if they help you!

## Versions and feedback

| Release | Difference |
|---|---|
| **[310.9.1-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10)** | Start here: two installation options, live controls, multiarch kernels, logging switch and optional telemetry. |
| [310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) | First native dynamic / X6 release, original INI ceiling syntax. |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | Universal DLL naming, corrected X2–X4. |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | First corrected MFG motion, `version.dll` only. |

Releases -0 through -6 were withdrawn for incorrect MFG motion. The white rectangle over Wukong's benchmark chart remains a known issue. Standalone controls and dynamic target changes have been user-confirmed in Wukong; this is not universal game validation. Linux/Proton and DXVK are unvalidated.

[Report an issue](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) with GPU/VRAM, driver, game/API, loaded Streamline version, chosen package, INI and NR settings. More configurations — especially RTX 20 — are welcome.

---

Credits: [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) · [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75) · [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) · [MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) · [ReShade](https://reshade.me/) · [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader). [Third-party notices](THIRD_PARTY_NOTICES.txt) · [Checksums](SHA256SUMS.txt)
