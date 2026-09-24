# Installation — v0.3.5-3

[README](../README.md) · [Français](INSTALL.md)

## What you need

- Windows x64 and a game with **DLSS Frame Generation** (D3D12 or Vulkan).
- An RTX 30 GPU (tested) or RTX 20 (experimental).
- Optional: **ReShade 6.8 with full add-on support**, only for the live panel and shortcuts.

`version.dll` works on its own, without ReShade. `optional-panel/DLSSG-SM86-75-COMPANION.addon64` only adds the panel and shortcuts. Settings are read from `ReShade.ini` even when ReShade is not installed: keep that file name and its `[DLSSG-SM86-75-COMPANION]` section.

## Install

1. Close the game and find its rendering executable (for example `b1/Binaries/Win64` in Wukong, `Binaries` in No Man's Sky).
2. Back up any file you are about to replace. Keep other mods.
3. Copy `version.dll` beside that executable. Copy the panel from `optional-panel/` only if you use ReShade.
4. Pick one folder in `config/` and copy its `dlssg_sm86.ini`. Copy its `ReShade.ini` if you have none; otherwise merge only our section into yours.
5. If our companion is listed in `ADDON.LoadFromDllMain`, remove that entry.
6. Vulkan only: install the matching NVIDIA runtime (next section).
7. Start the game and enable DLSS Frame Generation in its graphics settings.

| Template | Use it for |
|---|---|
| `config/d3d12` | D3D12 games |
| `config/vulkan-sm86` | Vulkan games on RTX 30 |
| `config/vulkan-sm75` | Vulkan games on RTX 20 (experimental) |

On Vulkan, install ReShade the usual way for that game; do not use a D3D12 ReShade DLL instead.

## Vulkan: matching NVIDIA runtime

Vulkan needs NVIDIA `nvngx_dlssg.dll` **310.9.1** with this SHA256:

```text
ff6e90eb78b827927dff5b4ecc6b1c870c2e9bca29ed9f48c7d348cc9e170b82
```

If the game's copy does not match, extract the one bundled in our proxy (needs Python and `pefile`):

```powershell
python -m pip install pefile
python extract_runtime.py --proxy version.dll --out nvngx_dlssg.extracted.dll
Get-FileHash nvngx_dlssg.extracted.dll -Algorithm SHA256
```

Back up the game's `nvngx_dlssg.dll`, then put the extracted file in its place under that name. Do not replace other Streamline DLLs or the Vulkan loader.

## Settings

`dlssg_sm86.ini` (restart the game after editing):

| Key | Meaning |
|---|---|
| `Optimized=1` | Optimized kernels and image-quality improvements. `0` uses the reference kernels. |
| `MaxGeneratedFrames=5` | Up to five generated frames (X6) when the game's plugin allows it. |

`ReShade.ini`, section `[DLSSG-SM86-75-COMPANION]`:

| Key | Meaning |
|---|---|
| `Multiplier=0` | Follow the game; `2`–`6` requests a fixed factor when `Dynamic=0`. |
| `Dynamic=1` | Native dynamic mode on D3D12, adaptive mode on Vulkan. |
| `TargetFPS=0` | Display refresh target; `1`–`1000` sets an explicit target (not a hard cap). |
| `UIRecomposition=1` | Automatic interface handling (recommended). `0` follows the game, `2` forces it. |
| `DLSSRenderScale=0` | No render-scale override; prefer the game's own DLSS settings. |
| `HotkeyX2`…`HotkeyX6` | Ctrl+F2 to Ctrl+F6: fixed X2 to X6. |
| `HotkeyDynamic`, `HotkeyFollowGame`, `HotkeyRestoreINI` | Ctrl+F10, Ctrl+F11, Ctrl+F12. |

In the panel, **Apply for this session** is temporary and **Apply & save settings** keeps the choice. Shortcuts need the panel; an empty binding disables a shortcut. Edit the INIs by hand only while the game is closed.

On Vulkan, NVIDIA's overlay shows the factor our adaptive mode selected (for example X4); this is expected.

## Proxy file names

| Name | When to use it |
|---|---|
| `version.dll` | First choice for most games, including Unreal Engine 4/5. |
| `dinput8.dll` | Games loading DirectInput8. |
| `dxgi.dll` | Games loading DXGI early (do not overwrite an existing ReShade `dxgi.dll`). |
| `winmm.dll` | Games loading WinMM (do not overwrite another mod's `winmm.dll`). |
| any `.asi` name | With an ASI loader. |

Install a single copy and rename only the proxy. The game must actually load that name.

## Upgrading

Replace `version.dll`, then replace our old companion with the new optional panel (or remove it). Set aside an old `DLSSG-SM86-75-RUNTIME.dll` if present. Never keep two versions of our add-ons active; old `DLSSGControls.addon64`, `DLSSG.addon64`, `dlssg-035-companion.addon64` or `renodx-rtx-unlocker.addon64` from this project can be disabled.

Settings from release 11 builds:

| Old | New |
|---|---|
| `MaxInterpolatedFrames=N` | `[FrameGeneration] MaxGeneratedFrames=N` |
| `MaxMultiplier=M` | `MaxGeneratedFrames=M-1` |
| `ForceMultiplier` | `Multiplier` (ReShade.ini) |
| `DynamicMFG` / `DynamicTargetFPS` | `Dynamic` / `TargetFPS` (ReShade.ini) |
| `[DLSSG-035-COMPANION]` | `[DLSSG-SM86-75-COMPANION]` |

## Troubleshooting and removal

- **The panel does not appear:** check that the add-on sits beside the executable and that ReShade has full add-on support. The engine keeps working without it.
- **The multiplier stays pending:** enable Frame Generation in the game; a factor the game's plugin does not support cannot be forced.
- **Reporting a problem:** include GPU, driver, game and API, both INIs, and `DLSSG-SM86-75-runtime.log`. Remove personal paths before sharing.
- **Cache:** a verified component is stored under `%LOCALAPPDATA%\DLSSG-SM86-75\proxy`. Close the games before deleting it.

To uninstall, close the game and restore your backups. Remove only our proxy, panel and INI section; if you replaced a Vulkan runtime, restore its backup too.
