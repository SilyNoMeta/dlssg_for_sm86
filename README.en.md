<div align="center">

# DLSS Frame Generation for RTX 20 / 30

**Multi Frame Generation up to X6, a steadier HUD and sharper fine detail — with or without ReShade.**

<a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v0.3.5-3/DLSSG-RTX20-30-v0.3.5-3-clean-win64.zip"><img alt="Download 0.3.5-3" src="https://img.shields.io/badge/Download-0.3.5--3-76b900?style=for-the-badge&logo=nvidia&logoColor=white"></a>

<img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-0078D4?style=flat-square&logo=windows&logoColor=white"> <img alt="DX12 and Vulkan" src="https://img.shields.io/badge/API-DX12%20%7C%20Vulkan-30363d?style=flat-square"> <img alt="RTX 30" src="https://img.shields.io/badge/RTX%2030-supported-76b900?style=flat-square"> <img alt="RTX 20" src="https://img.shields.io/badge/RTX%2020-experimental-d29922?style=flat-square"> <img alt="NVIDIA FG 310.9.1" src="https://img.shields.io/badge/NVIDIA%20FG-310.9.1-555?style=flat-square">

[English](README.en.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [Installation guide](docs/INSTALL.en.md) · [Release notes](RELEASE-NOTES.md)

</div>

> [!IMPORTANT]
> Experimental. It needs a game that ships **NVIDIA DLSS Frame Generation** (Streamline), even when the game's menus do not offer it: the REANIMAL demo, for example, gets it activated.

## ✨ New in 0.3.5-3

| | What you should notice |
|---|---|
| 🧭 **Steadier HUD** | Minimaps, gauges and text no longer shimmer or smear on generated frames in games that give DLSS Frame Generation no clean view of the scene (for example **Crimson Desert**). |
| 🪟 **Clean translucent panels** | No more double image or warped background behind translucent panels and minimaps (for example **Cyberpunk 2077**). |
| 🪄 **Fully automatic** | No new setting. Active with the default `UIRecomposition=1` on DX12. Games that already handle their interface properly are left untouched. |

## 🚀 Quick start

1. Close the game and back up the files you are about to replace.
2. Copy **`version.dll`** beside the game's rendering executable.
3. From `config/d3d12`, `config/vulkan-sm86` or `config/vulkan-sm75`, copy **`dlssg_sm86.ini`** and merge our section into **`ReShade.ini`** (keep that file even without ReShade: it holds our settings).
4. Want the live panel and shortcuts? Install ReShade 6.8 with full add-on support and add `optional-panel/DLSSG-SM86-75-COMPANION.addon64`.
5. Enable DLSS Frame Generation in the game.

Vulkan also needs the matching NVIDIA runtime: see the [installation guide](docs/INSTALL.en.md).

## 🎛️ What you get

| | |
|---|---|
| **X2 – X6** | Follow the game, or pick a fixed multiplier. X4 = one rendered frame plus three generated ones. |
| **Dynamic mode (DX12)** | Set a target FPS and let NVIDIA adjust generation in compatible games. |
| **Adaptive mode (Vulkan)** | The multiplier follows your frame rate and target, from X2 to X6. |
| **Image quality** | Cleaner fences, wires and foliage, steadier interface on generated frames. |
| **Live controls** | Change and save settings per game from the ReShade panel, or with Ctrl+F2…F12. |
| **DLSS render scale** | DLAA to Ultra Performance or a custom scale, checked before it is saved. |
| **Game fixes** | REANIMAL DLSS activation, FINAL FANTASY VII REBIRTH identity handling, Black Myth: Wukong startup. |

<details>
<summary><b>⚙️ Settings</b></summary>

`dlssg_sm86.ini` — restart the game after editing:

```ini
[FrameGeneration]
Optimized=1            ; optimized kernels and image-quality improvements (0 = reference)
MaxGeneratedFrames=5   ; up to X6 when the game's plugin allows it
```

`ReShade.ini` — also used without ReShade:

```ini
[DLSSG-SM86-75-COMPANION]
Multiplier=0           ; 0 = follow the game, 2-6 = fixed factor
Dynamic=0              ; 1 = dynamic (DX12) / adaptive (Vulkan)
TargetFPS=0            ; 0 = display refresh, otherwise a target (not a hard cap)
UIRecomposition=1      ; automatic interface handling (0 = follow game, 2 = force)
```

Shortcuts (with the panel): **Ctrl+F2–F6** X2–X6 · **Ctrl+F10** automatic mode · **Ctrl+F11** follow the game · **Ctrl+F12** restore saved settings.

</details>

<details>
<summary><b>🔌 Proxy file names</b></summary>

The same file can be renamed to match what the game loads. Install one copy only.

| Name | When |
|---|---|
| `version.dll` | First choice, including Unreal Engine 4/5 |
| `dinput8.dll` | Games using DirectInput8 |
| `dxgi.dll` | Games loading DXGI early — never overwrite an existing ReShade `dxgi.dll` |
| `winmm.dll` | Games using WinMM |
| any `.asi` | With an ASI loader |

</details>

<details>
<summary><b>⬆️ Upgrading from an older release</b></summary>

Replace `version.dll`, replace our old companion with the new optional panel (or remove it) and set aside any old `DLSSG-SM86-75-RUNTIME.dll`. Never keep two versions of our add-ons active. Setting migration from release 11 is in the [installation guide](docs/INSTALL.en.md#upgrading).

</details>

## 🎮 Tested in play

**Crimson Desert · Cyberpunk 2077 · FINAL FANTASY VII REBIRTH · Onimusha: Way of the Sword · Bodycam · REANIMAL (demo)** — RTX 3070 Ti Laptop, DX12. Other games and RTX 20 hardware may behave differently; reports are welcome.

## 📦 Versions

| Version | |
|---|---|
| [**0.3.5-3**](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v0.3.5-3) | Current release: steadier HUD and clean translucent panels, on top of the integrated engine and optional panel. |
| [310.9.1-11](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11) · [-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10) · [-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) · [-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) · [-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | Archived previous generation, with its own layout and settings. |

## 💬 Feedback

[Open an issue](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) with your GPU and driver, the game and API, the proxy file name, both INIs and `DLSSG-SM86-75-runtime.log`.

---

<div align="center">

Built on [sdli1995 / dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) (upstream 0.3.5) · includes work adapted from [Tony Joaca / DLSSG-Transfusion](https://github.com/TonyJoaca/DLSSG-Transfusion) (MIT)<br>
Thanks to [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75), [Matias Lombo](https://github.com/matiasLombo/mfg-unlock) and [ReShade](https://reshade.me/)<br>
[Third-party notices](THIRD_PARTY_NOTICES.txt) · [Checksums](SHA256SUMS.txt) · not affiliated with NVIDIA

</div>
