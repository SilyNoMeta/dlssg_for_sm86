# Installation: version.dll, ASI or dxgi.dll

Release **310.9.1-8** — [download the universal package](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8).
It contains one `version.dll` that can also be named `dxgi.dll` or `dxgi.asi`.
These modes require -8; the original -7 binary must keep its `version.dll` name.

All names use the same DX12/Vulkan runtime, kernels, temporal fix and
INI options. Close the game and back up existing files before choosing **one**
installation method beside the actual game executable. Install only one copy
of our bridge and preserve your INI when switching modes.

## With Ultimate ASI Loader

1. Install [Ultimate ASI Loader x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader)
   as `version.dll`.
2. Rename **our** `version.dll` to `dxgi.asi` and place it beside the loader.
3. Place `dlssg_sm86.ini` in the same directory, keeping its original name.
4. Restart the game and enable DLSS Frame Generation in its settings.

```text
Game.exe
version.dll       <- Ultimate ASI Loader x64
dxgi.asi          <- our bridge
dlssg_sm86.ini     <- bridge configuration
```

REFramework can keep its `dinput8.dll`. The loader and bridge are two different
binaries here. UAL also supports another `.asi` filename through `InitializeASI`;
we verified `dlssg_sm86.asi` in an isolated loader test. With a loader that does
not call that export, use `dxgi.asi`, which also starts automatically on load.
If you put the plugin in an ASI subdirectory, keep the INI beside the plugin.

## Direct dxgi.dll proxy

Rename our `version.dll` to `dxgi.dll` and place it beside the game executable
with `dlssg_sm86.ini`. This mode does not require an ASI loader.

```text
Game.exe
dxgi.dll          <- our bridge, also forwarding DXGI calls to Windows
dlssg_sm86.ini
```

If another mod, such as ReShade, already uses `dxgi.dll`, keep that mod and
choose ASI mode instead. Our DXGI proxy forwards to Windows; it does not
automatically chain another DXGI proxy.

## Direct version.dll proxy

Place our `version.dll` and `dlssg_sm86.ini` beside the executable without an
additional ASI loader. Choose another mode if that filename is already used.
The game must load the chosen DLL name for the bridge to start.
Never rename the bridge to `nvngx_dlssg.dll`.

## Configuration and verification

The configuration filename is always **`dlssg_sm86.ini`**, regardless of the
bridge filename. Its four `[Optimizations]` options accept `1` or `0`; missing
files or keys default to `1`. Restart the game after changing them.
The X3/X4 temporal correction is always enabled.

Look for `asi_attached`, `dxgi_attached` or `proxy_attached` in `dlssg3109.log`,
followed by `installed_310_9_1` when the runtime is handled. An ASI loader does
not need to display an overlay. Loading a plugin alone does not prove that
frame generation is running.

The universal binary passes automated loader and DX12/Vulkan image checks.
Direct `dxgi.dll` operation is user-confirmed in Wukong on RTX 3070 Ti Laptop
8 GB. This is a functional report, not a new performance benchmark.
The filename does not add frame generation to games without an integration,
or add DX11 DLSSG support. To roll back, close the game, remove the installed
bridge copy and restore your backed-up files.
