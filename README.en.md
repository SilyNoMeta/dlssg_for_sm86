<div align="center">

<h1>DLSS Frame Generation</h1>
<p>Your frames. Your settings. Now with live ReShade controls.</p>
<p><img alt="310.9.1-11" src="https://img.shields.io/badge/release-310.9.1--11-76b900?style=flat-square"> <img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square"> <img alt="DX12 and Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square"></p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-11/dlssg-310.9.1-11-win64.zip">Download 310.9.1-11</a></strong></p>
<p><a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.zh-CN.md">简体中文</a></p>

</div>

---


**310.9.1-11 keeps the engine in an early-loading DLL and makes ReShade an optional control panel.** Use the DLL on its own, or add the panel to change settings while playing. The previous standalone add-on could load too late for some games. Built on [sdli1995’s original project](https://github.com/sdli1995/dlssg_for_sm86).

## One download, with or without ReShade

The ZIP contains **`version.dll`**, **`dlssg_sm86.ini`** and the optional **`DLSSGControls.addon64`** panel, plus the guides.

| Your setup | How to use it |
|---|---|
| **Without ReShade** | Install the DLL and INI. Edit the INI by hand and restart the game to apply changes. |
| **With ReShade** | Install the same files plus the add-on. With full add-on support, the panel lets you change the multiplier and compatible DMFG settings, record shortcuts, and save those settings to the INI. |

The panel covers part of the INI: optimization switches, ceiling, logging and telemetry still require manual editing and a restart. ReShade and OptiScaler are not bundled. Without ReShade, the add-on is simply unused; the DLL still provides generation. When upgrading, remove only our old `DLSSG.addon64`; keep ReShade and unrelated add-ons.

Close the game, back up existing files, and install beside the actual executable (Wukong: `b1/Binaries/Win64`). Enable DLSS Frame Generation in the game. Install only one copy of our engine, and keep your own INI after checking the migration below.


[DLL / ASI installation](docs/install-loaders.en.md) · [ReShade installation and panel](docs/reshade-controls.en.md)

## What you can do

| Feature | In practice |
|---|---|
| **X2–X6** | Choose a fixed multiplier within the loaded plugin's support. X4 is one rendered frame plus three generated frames. |
| **Native Dynamic MFG** | Choose a target and let NVIDIA adjust the multiplier on compatible **DX12** integrations. |
| **Live controls** | Use the ReShade panel for changes during gameplay. DLL-only hotkeys currently fail in Wukong and are not validated as a reliable alternative. |
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

Manual INI changes require a restart. ReShade's **Apply for this session** is temporary; **Apply & save settings** persists the mode and target. **Record** captures a shortcut, and **Save keyboard shortcuts** saves bindings independently. Defaults: **Ctrl+F2–F6** for X2–X6, **Ctrl+F10** for dynamic, **Ctrl+F11** to follow the game, **Ctrl+F12** to restore INI settings. All can be rebound or disabled. [All controls and key syntax](docs/live-controls.en.md).

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

## DLSS image quality: apply, verify, save

The optional panel now offers **DLAA, Quality, Balanced, Performance and Ultra Performance**, plus a **50–100% custom slider**. These controls are mainly useful when DLSS is injected and the game has no quality menu. **If the game already offers DLSS quality or render scale, use its own settings.**

Apply a scale for the session first. **Save render scale** unlocks only after eight consecutive successful DLSS frames use the requested dimensions. An ignored request cannot be saved through the panel or its API. Actual input/output dimensions are shown separately from the request. Turning the override off can always be saved; manual INI editing bypasses verification. Live application is game-dependent. [Resolution controls and recovery](docs/super-resolution.en.md).

## Experimental quality options

Three independent options are available in the INI and are **off by default**:

| Key | What it changes |
|---|---|
| `[Quality] QualityValidWarp=1` | Trusts accepted warped color candidates more strongly; aims to preserve thin details. |
| `[Experimental] BlackwellBlend=1` | Selects a Blackwell-derived blend kernel ported to the supported architectures. |
| `[Experimental] BlackwellScatter=1` | Selects a Blackwell-derived intermediate-motion scatter kernel. |

The Blackwell name identifies the kernel's origin, not a hardware requirement. These variants have SM75, SM86 and SM89 ports. They can be combined, require a full restart, and may worsen ghosting or stability. Intermittent GPU hangs were observed during Wukong experiments; keep them off for the established path. No universal image-quality or FPS improvement is claimed.

This release still embeds the NVIDIA **310.9.1** FG runtime and adapted kernels. It does **not** claim compatibility with fourteen different provider versions, automatic UIR unlocking, DirectInput8 proxy support, or Proton support.

## OptiScaler and companion tools

**OptiScaler support is awaiting [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156).** The producer is included here, but a consumer build containing that change is required. Turning telemetry on alone will not update an older OptiScaler. The reading is CPU source-frame submission cadence, not GPU completion or latency. Our ReShade panel can display it independently when available.

New to DLSS modding? Start with **[RHI](https://github.com/RankFTW/RHI)** for managing DLSS and companion tools, then use the download above. The tester reports very good compatibility with ShortFuse's [DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315) and [Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884), also available through RHI. Their NR support is separate from this project's FG compatibility. Give [RHI](https://github.com/RankFTW/RHI) and [ShortFuse's RenoDX](https://github.com/clshortfuse/renodx) a star if they help you!

## Versions and feedback

| Release | Difference |
|---|---|
| **[310.9.1-11](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11)** | Recommended: early-loading DLL with optional ReShade panel; loader routing hardened against overlay interception. |
| [310.9.1-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10) | Previous standalone ReShade engine; migrate to the DLL + control panel for more reliable startup. |
| [310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) | First native dynamic / X6 release, original INI ceiling syntax. |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | Universal DLL naming, corrected X2–X4. |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | First corrected MFG motion, `version.dll` only. |

Releases -0 through -6 were withdrawn for incorrect MFG motion. The white rectangle over Wukong's benchmark chart remains a known issue. Live controls and dynamic target changes have been user-confirmed in Wukong; this is not universal game validation. Linux/Proton and DXVK are unvalidated.

[Report an issue](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) with GPU/VRAM, driver, game/API, loaded Streamline version, installation method, INI and NR settings. More configurations — especially RTX 20 — are welcome.

---

Credits: [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) · [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75) · [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) · [MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) · Tony Joaca (DLSSG-Transfusion) · [Matias Lombo](https://github.com/matiasLombo/mfg-unlock) · [ReShade](https://reshade.me/) · [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader). [Third-party notices](THIRD_PARTY_NOTICES.txt) · [Checksums](SHA256SUMS.txt)
