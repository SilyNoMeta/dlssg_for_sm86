# DLSSG 310.9.1-0 for SM86

Current documentation and screenshots:
[English](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/README.md)
| [简体中文](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/README.zh-CN.md)
| [Français](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/README.fr.md).

The original release ZIP and DLL are unchanged; the linked documentation is updated separately.

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

SHA256 of `version.dll`:
`81f70a21f207bc9773275cb8343c95e41c18545190a05efbb2e4de650991c4b0`

Based on [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).

## Compatibility update / Mise à jour / 兼容性更新

**English:** Game reports come from an RTX 3070 Ti **Laptop, 8 GB VRAM**.
Our tester also reports very good compatibility with ShortFuse's DLSS Tool
and Patched DLSS-NR for RTX20/30/40. Beginners are encouraged to start with
[RHI](https://github.com/RankFTW/RHI) for these companion tools. Reports from
other configurations are welcome. Please star RHI and
[ShortFuse's RenoDX](https://github.com/clshortfuse/renodx) to support their authors.

**Français :** Les retours proviennent d'un **portable RTX 3070 Ti mobile, 8 Go**.
Notre testeur rapporte aussi une très bonne compatibilité avec DLSS Tool de
ShortFuse et Patched DLSS-NR for RTX20/30/40. Nous recommandons
[RHI](https://github.com/RankFTW/RHI) aux débutants pour ces outils complémentaires.
Les essais d'autres configurations sont les bienvenus. Pensez à mettre une
étoile à RHI et [RenoDX de ShortFuse](https://github.com/clshortfuse/renodx).

**简体中文：** 游戏反馈来自配备 **RTX 3070 Ti Laptop、8 GB 显存的笔记本**。
测试用户还反馈，本版本与 ShortFuse 的 DLSS Tool 和 Patched DLSS-NR for RTX20/30/40
配合良好。推荐新手通过 [RHI](https://github.com/RankFTW/RHI) 安装配套工具，
欢迎其他配置的用户分享结果。请为 RHI 和
[ShortFuse 的 RenoDX](https://github.com/clshortfuse/renodx) 点亮 Star，支持作者。
