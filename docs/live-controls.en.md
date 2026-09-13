# Live controls and INI reference — 310.9.1-11

The single ZIP includes the DLL/ASI engine and optional ReShade control panel. Without ReShade, edit the INI manually and restart. Keep `dlssg_sm86.ini` beside the engine and enable FG in the game first. RTX 20 remains experimental without a physical Turing test.

## Default hotkeys and customization

**Known limitation:** DLL-only hotkeys failed in the current Wukong gameplay test, despite valid bindings being loaded. Automated parser/control tests do not establish in-game input detection. Use the ReShade panel for live changes; DLL-only users can edit the INI and restart. The binding syntax below documents the implemented interface, not a guarantee that keys work in every integration.

The supplied `[Hotkeys]` section uses **Ctrl+F2 through Ctrl+F6** for X2–X6,
**Ctrl+F10** for dynamic, **Ctrl+F11** to follow the game and **Ctrl+F12** to
restore INI settings. Change any binding or leave it empty to disable that action:

| Entry | Action |
|---|---|
| `ForceX2` … `ForceX6` | Request a fixed multiplier, within the INI and plugin ceiling. |
| `RestoreINI` | Restore `ForceMultiplier`, `DynamicMFG` and `DynamicTargetFPS` read at launch. |
| `FollowGame` | Follow the game's own mode, including its native dynamic mode, ignoring our force/dynamic settings. |
| `ActivateDynamicMFG` | Request native dynamic mode using the INI's `DynamicTargetFPS`. Compatible DX12 only. |

Default configuration for the next package:

```ini
[Hotkeys]
ForceX2=Ctrl+F2
ForceX3=Ctrl+F3
ForceX4=Ctrl+F4
ForceX5=Ctrl+F5
ForceX6=Ctrl+F6
ActivateDynamicMFG=Ctrl+F10
FollowGame=Ctrl+F11
RestoreINI=Ctrl+F12
```

Use `+` between modifiers and **one** key. Names ignore case and surrounding
spaces. Modifiers: `Ctrl`, `Alt`, `Shift`, `Win`. Keys: `F1`–`F24`, `A`–`Z`,
`0`–`9`, `Insert`, `Delete`, `Home`, `End`, `PageUp`, `PageDown`, `Space`, `Tab`,
`Enter`, `Escape`, `Up`, `Down`, `Left`, `Right`, `Backspace`, `Pause`.
Advanced users can use a two-digit Windows virtual-key code, e.g. `0x41` for A;
see Microsoft's [virtual-key table](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes).
Letter bindings use Windows virtual keys, so check the result on your keyboard layout.

Only the exact modifiers match: `F8` and `Ctrl+F8` are different bindings. A held
key does not repeat. The game must be the foreground application; switching
back with a key already held does not fire it. Invalid chords are disabled,
and duplicate bindings disable **all** conflicting actions. Keys are not consumed:
avoid game, Steam, ReShade or other mod shortcuts. Prefer combinations; a bare
letter can also fire while typing in an in-game chat or another overlay.

Restart once after editing bindings. Using a configured shortcut does not edit
the INI or require a restart in integrations that regularly submit FG options.

## ReShade or keyboard controls

For an in-game panel, use the **ReShade controls ZIP**, which contains the engine DLL and `DLSSGControls.addon64`. Follow the [panel guide](reshade-controls.en.md). The add-on controls the DLL; it does not replace it.

The panel offers **Apply for this session**, **Apply & save settings**, and a separate **Save keyboard shortcuts** button. A successful save updates both the INI and the saved settings used by this session. `RestoreINI` restores those saved settings; it does not reread a manually edited file. The `ActivateDynamicMFG` shortcut uses the saved INI target, so save a session target first if you want that shortcut to reuse it.

Requests apply on the next game submission of Streamline FG options. If a request remains pending, apply an FG setting in the game menu. A successful SDK submission does not prove the driver used the target or that generated images were presented. Fixed Vulkan overrides require a recognized Streamline path; native dynamic is DX12-only. Direct NGX paths remain game-controlled. The panel does not change NR, Reflex, VSync or NVIDIA profiles.

## Set the generated-frame ceiling

Use `MaxInterpolatedFrames` in `[FrameGeneration]`. It counts **generated** frames;
add one rendered frame to obtain the displayed multiplier.

| MaxInterpolatedFrames | Maximum mode |
|---|---|
| 1 | X2 |
| 2 | X3 |
| 3 | X4 |
| 4 | X5 |
| 5 | X6 |

Missing or invalid values default to **5**. The loaded plugin can impose a lower
ceiling. A value of 1 retains X2 and all required compatibility/temporal patches.
`ForceMultiplier` still uses the displayed factor: `4` requests X4, `0` follows the game.

**Migration:** replace an old `MaxMultiplier=M` with `MaxInterpolatedFrames=M-1`.
For example, `MaxMultiplier=6` becomes `MaxInterpolatedFrames=5`. The old key is
no longer read. Also rename `[Hotkeys] DynamicMFG` to `ActivateDynamicMFG`.
Keep `[FrameGeneration] DynamicMFG` beside `DynamicTargetFPS`: this is the startup
switch, while `ActivateDynamicMFG` is an optional keyboard shortcut.

## Optional source-frame telemetry

```ini
[Telemetry]
Enabled=1
```

Default is `0`; restart after changing it. This measures successful, unique
Streamline source-frame submissions over approximately half a second. Duplicate
submissions for the same frame are ignored. It measures CPU submission cadence,
not GPU completion or input latency. Stale or ambiguous data is unavailable.
Direct NGX integrations without intercepted Streamline constants are unsupported.

OptiScaler needs a build containing [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156), which is still awaiting upstream review at release time. This ZIP does not include a modified OptiScaler. Existing unmodified builds do not read the interface simply because this INI key is enabled. When supported, the second FPS value comes from this source cadence; managed OptiScaler FG backends keep their own display path. The ReShade panel can also show source cadence independently. [Consumer setup](standalone-reshade.en.md#optiscaler-only-testing-the-counter).

## Disable the bridge log

```ini
[Logging]
Enabled=0
```

Restart after editing. Default is `1`; `0` stops creating/appending
`dlssg3109.log`. An old log is left intact, so its mere presence does not mean
logging is still enabled. Other tools' and NVIDIA's logs are unaffected. Enable
logging again before collecting a diagnostic report.

## Dynamic target does not match the INI?

Check NVIDIA's **DLSSG dynamic target override**, both global and per-game,
as well as the ordinary FPS limit and VSync. They are separate settings. A
driver override can supersede a target accepted by Streamline. Save the profile
before changing the relevant override; do not reset unrelated settings.


With logging enabled, `hotkey_bindings_loaded` gives the number of valid bindings. `hotkey_action_triggered=0` identifies ForceX2 (1–4 identify X3–X6). A `live_multiplier_requested` event proves the request was queued; `sl_forced_multiplier_accepted` means Streamline accepted it. This does not replace checking actual presentation. For a single F4 binding, use `ForceX2=F4` under `[Hotkeys]`, then restart.
