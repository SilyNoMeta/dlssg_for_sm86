# DLL / ASI installation — 310.9.1-10

Download **dlssg-310.9.1-10-dll-win64.zip** from the [release](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10). For a ReShade panel, choose the [standalone package](standalone-reshade.en.md) instead.

Close the game and back up files before replacing them. Copy **one** engine and `dlssg_sm86.ini` beside the actual game executable (Wukong: `b1/Binaries/Win64`). Enable DLSS FG in the game.

| Method | How |
|---|---|
| Direct version proxy | Install our `version.dll` unchanged. The game must load that name. |
| Direct DXGI proxy | Rename the same file to `dxgi.dll`. No ASI loader required. |
| Ultimate ASI Loader | Install [UAL x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader) as `version.dll`; rename our file to `dxgi.asi`. |

The same engine works under these names. Keep the INI named `dlssg_sm86.ini` beside it. Never rename our bridge to `nvngx_dlssg.dll`. Do not overwrite ReShade's or another mod's proxy: choose a free loading method. Our DXGI proxy forwards to Windows, not automatically to another DXGI mod.

UAL can load other ASI names through `InitializeASI`; `dlssg_sm86.asi` was tested in the loader fixture. With a loader that does not call that export, use `dxgi.asi`. If an ASI subdirectory is used, keep the INI beside our plugin. REFramework can retain its own `dinput8.dll`.

Do not combine this DLL/ASI with `DLSSG.addon64` or another MFG unlock engine. ReShade itself and unrelated NR add-ons can stay. Both packages implement the same features; only the standalone package supplies the ReShade panel.

## Configuration and verification

The default follows the game, with `MaxInterpolatedFrames=5` (X6 ceiling where supported). See [controls, migration, logging and telemetry](live-controls.en.md). Manual INI edits need restart; configured shortcuts apply on the next recognized Streamline options submission. Native dynamic requires compatible DX12; fixed controls can use recognized DX12/Vulkan paths.

With logging enabled, `proxy_attached`, `dxgi_attached` or `asi_attached` identify loading; `installed_310_9_1` identifies runtime handling. `sl_native_dynamic_accepted` means SDK acceptance, not proof the driver followed that target. NVIDIA's global/per-game dynamic target override can take priority. An available watermark can show `Dyn DRV` and current/maximum factor; this package does not enable the watermark automatically.

Loading alone does not prove generated frames are presented. To roll back, close the game, remove only our installed engine and restore your backups. No CUDA toolkit or build tools are needed to play.
