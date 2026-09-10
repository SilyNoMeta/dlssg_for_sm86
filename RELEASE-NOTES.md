# DLSSG 310.9.1-0 for SM86

First experimental distribution of the 310.9.1 SM86 bridge.

- One `version.dll` to install; runtime and SM86 kernels are embedded.
- Verified runtime cache created automatically on first use.
- X2/X3/X4 selectable where supported by the game integration.
- User reports: Black Myth: Wukong and Palworld work. X2 is preferred in Wukong;
  Palworld also feels good in X4, with visibly degraded image quality.
- No INI or `HardwareBilinear` option in this variant.

Requires Windows x64, Direct3D 12, an SM86 NVIDIA GPU and a compatible game.
See the README for installation and limitations. This is an experimental
release, not a performance-optimized revision.

The DLL is byte-for-byte identical to the locally validated 0.1.0 binary.
Windows file metadata remains 0.1.0; `310.9.1-0` is the distribution tag.

SHA256 of `version.dll`:
`81f70a21f207bc9773275cb8343c95e41c18545190a05efbb2e4de650991c4b0`

Based on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
