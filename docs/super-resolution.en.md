# DLSS rendering resolution — experimental controls

The **DLSS image quality** controls remain available in every game. They are
experimental and mainly useful when DLSS is injected into a game that provides
no DLSS quality or render-scale controls of its own.

**If the game offers these settings, use its graphics menu and leave our override
off (`RenderScale=0`).** We cannot reliably detect the presence of a menu from
DLSS calls. Injecting DLSS alone does not guarantee override compatibility.

Choose a preset or custom scale, then use **Apply scale for this session**.
Then use **Save render scale** to keep the request in `dlssg_sm86.ini`.
Saving a nonzero scale is enabled only after **eight consecutive successful DLSS
frames at the requested resolution**, within two pixels per axis for engine rounding.
The engine enforces the same check: pending, ignored, mismatched or stale requests
cannot be saved. Changing the requested percentage requires applying it again.
These saves are independent of Frame Generation and keyboard shortcuts.

| Button | Width and height rendered |
|---|---:|
| DLAA | 100% |
| Quality | 66.667% |
| Balanced | 58.824% |
| Performance | 50% |
| Ultra Performance | 33.333% |

The slider covers **50–100%**. Ultra Performance is a separate fixed preset;
intermediate values below 50% are unsupported. Percentages apply to each axis:
50% width and height means one quarter of the output pixel count.

**Check “Observed DLSS”.** It reports dimensions from successful DLSS evaluations.
Accepting or saving a request does not prove the game applied it. A validated
engine adapter can apply changes live; other games may cache or ignore the
resolution recommendation. Saving and restarting is not a guaranteed workaround.

A startup failure was reported after saving an override in a game with native
DLSS controls; its exact cause is unconfirmed. **If this happens, close the game
and set `RenderScale=0` in the INI before trying again.** Turn the override off
and apply to return control to the game during a session. With a live adapter,
the previous game scale is restored; other hosts decide when to query again.

Without ReShade, edit this INI section, then restart to read the new setting:

```ini
[SuperResolution]
RenderScale=0
```

`0` follows the game; `50` through `100` select a custom scale; `33.333` selects
Ultra Performance. Missing or invalid values fall back to `0`. Manual edits bypass runtime verification and need a restart to be read; use the
panel when possible. Restarting does not establish game compatibility.
Saving `0` to disable an override is always allowed, even without active DLSS.

DLSS must already be active. These controls change rendering resolution, not the
K/M neural model preset, and do not add DLSS to a game. Use the matching engine
DLL and `DLSSGControls.addon64`; the add-on is an optional control panel.
