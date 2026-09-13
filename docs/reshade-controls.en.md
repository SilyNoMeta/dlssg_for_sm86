# ReShade control panel — 310.9.1-11

Install **version.dll + DLSSGControls.addon64 + dlssg_sm86.ini**, alongside ReShade with full add-on support. The single release ZIP includes all three project files. The DLL loads the compatibility engine early; the small add-on supplies the interface. The panel alone cannot enable FG compatibility.

Close the game and back up the files you replace. Remove our previous **DLSSG.addon64** if installed, while keeping ReShade and unrelated NR add-ons. Install one engine only. The INI stays beside the engine, even if an ASI loader uses a subdirectory.

If ReShade uses `dxgi.dll`, our engine can remain `version.dll`: Ultimate ASI Loader is not required for this arrangement. For conflicting names or ASI installation, see the [loader guide](install-loaders.en.md). The standalone engine is no longer the recommended distribution because some games initialize DLSS before ReShade loads its add-ons.

## Generation settings

Enable Frame Generation in the game's own menu first. Open ReShade and select
**DLSSG Live Controls**. Choose saved settings, follow game, a fixed multiplier,
or Dynamic MFG. Dynamic requires a compatible DX12 integration.

- **Apply for this session** changes only the current session.
- **Apply & save settings** also writes the chosen force/dynamic mode and target
  to dlssg_sm86.ini. These become the settings used at the next launch.
- An accepted request is the last SDK submission, not a measured live multiplier.
  If it remains pending, apply an FG option in the game's menu.
- The default is to follow the game. No target FPS is imposed; the supplied shortcuts can be rebound or disabled.

## Keyboard shortcuts

In the lower section, click **Record** beside an action, then press a combination
such as Ctrl+Alt+F8. Escape cancels recording. You may also edit the text field;
empty means disabled. Click **Save keyboard shortcuts** to save and activate
all bindings. This button does not save generation settings. No restart is needed.
Invalid or duplicate combinations are rejected without partially saving them.
Existing shortcuts are suspended while recording/editing in the panel, and
held keys must be released before they can trigger again.

Modifiers: Ctrl, Alt, Shift, Win. Keys: F1–F24, A–Z, 0–9, named keys such as
Insert/Delete/Home/End/PageUp/PageDown/Space/Tab/Enter/Escape and arrows, or
Windows virtual-key notation 0xNN. A captured unfamiliar key uses this notation.

## INI settings

MaxInterpolatedFrames is the only ceiling setting: 1..5 = X2..X6; default 5.
ForceMultiplier uses the displayed factor (0 = game, 2..6 = X2..X6).
DynamicMFG and DynamicTargetFPS are startup settings in [FrameGeneration].
ActivateDynamicMFG in [Hotkeys] is the shortcut, not a second startup switch.
The four optimization switches, ceiling, logging and telemetry still require
editing the INI and restarting. Saving from the panel preserves other sections.
The file is written via a temporary copy and replacement; failed saves retain
both the old file and current settings.

## OptiScaler: only testing the counter

Use an OptiScaler build containing [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156). It is pending upstream review at release time; no modified OptiScaler is bundled. The INI alone does not update an older consumer. For an external DLSSG test, choose
**FG Output = None**, then **FG Input = None**. Do not select Nukem's or another
replacement to enable the counter. Keep in-game FG enabled.

1. In our INI, set [Telemetry] Enabled=1 and restart after saving.
2. In OptiScaler, expand **FPS Overlay** on the right.
3. Check **FPS Overlay Enabled**, choose **Overlay Type = Simple**.
4. Click **Save Settings** and restart if backend changes were pending.

Look for two FPS numbers and **DLSSG source telemetry**. The second number is
observed CPU source-frame submission cadence; the first is OptiScaler's existing
counter. The charts at the bottom of its settings window are not this overlay.
Do not divide by the configured maximum in dynamic mode. No extra number means
telemetry is missing/stale/ambiguous or the integration is not observed; it is
not a zero-FPS measurement. Our panel can also show source cadence when available.

## Validation boundary

Standalone loading and two device lifecycles were tested with ReShade 6.8.0.
Settings persistence, error handling and hotkey conflict checks pass. Real
Streamline DX12 and Vulkan command tests pass, with native dynamic limited to
DX12. The isolated UI host uses DX11 only to render a panel: this does not add
DX11 Frame Generation support. The user confirmed standalone controls, key capture and dynamic target changes in Black Myth: Wukong on RTX 3070 Ti Laptop 8 GB. This is a functional report, not a benchmark or validation of all games. This describes earlier component validation; optional kernel experiments are detailed in the current release notes. RTX 20 remains experimental.

## Dynamic target and saved settings

NVIDIA global/per-game **Override DLSSG Target Frame Rate** can supersede the panel target. Disable the relevant override and restart to use your own target. Ordinary FPS limits and VSync are separate. The dynamic shortcut uses the saved INI target; use Apply & save settings to persist it. See the [INI reference](live-controls.en.md).

## DLSS rendering resolution

[DLSS rendering resolution](super-resolution.en.md)
