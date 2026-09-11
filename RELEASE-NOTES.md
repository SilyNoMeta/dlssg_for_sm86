# 310.9.1-8 — One DLL, three loader modes / Une DLL, trois modes / 一个 DLL，三种加载方式

## English

**One `version.dll`: keep that name, rename it to `dxgi.dll` for direct loading, or to `dxgi.asi` for Ultimate ASI Loader x64. Install only one bridge copy.** For ASI, the loader itself occupies `version.dll`; our renamed bridge sits beside it. Keep the configuration named `dlssg_sm86.ini`. Other ASI names work with loaders calling `InitializeASI` (`dlssg_sm86.asi` tested with UAL).

Fixes the separate ASI startup defect: loading the old renamed DLL did not initialize the bridge. Adds real Windows DXGI export forwarding. Retains -7's mandatory X3/X4 temporal correction, DX12 + Vulkan, and all four INI options, including upstream-inspired HardwareBilinear. No model, weights or kernel changes; no new FPS gain is claimed.

The exact binary is user-confirmed working directly as `dxgi.dll` in Wukong on RTX 3070 Ti Laptop 8 GB. Automated checks cover real DXGI factories, concurrent loading, UAL startup and DX12/Vulkan image equivalence to corrected -7. The white Wukong benchmark chart remains a known issue; this release's Vulkan game validation remains pending. [Installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/install-loaders.en.md) · [Technical findings](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/research.en.md).

## Français

**Une seule `version.dll` : garder ce nom, la renommer en `dxgi.dll` pour un chargement direct, ou en `dxgi.asi` avec Ultimate ASI Loader x64. Installer une seule copie du bridge.** En ASI, le loader occupe `version.dll` et notre bridge renommé se place à côté. Conserver `dlssg_sm86.ini`. D'autres noms ASI fonctionnent si le loader appelle `InitializeASI` (`dlssg_sm86.asi` testé avec UAL).

Corrige le démarrage ASI : l'ancienne DLL renommée était chargée mais le bridge restait inactif. Ajoute les véritables exports DXGI Windows. Conserve la correction temporelle X3/X4 obligatoire de la -7, DX12 + Vulkan et les quatre options INI, dont HardwareBilinear inspiré de l'original. Modèle, poids et kernels inchangés ; aucun nouveau gain de FPS annoncé.

Ce binaire exact est confirmé fonctionnel dans Wukong sous `dxgi.dll`, sur RTX 3070 Ti Laptop 8 Go. Factories DXGI réelles, chargement concurrent, démarrage UAL et équivalence des images DX12/Vulkan à la -7 corrigée vérifiés. Le graphique blanc Wukong reste connu ; la validation Vulkan en jeu de cette release reste à confirmer. [Installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/install-loaders.fr.md) · [Détails techniques](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/research.fr.md).

## 简体中文

**仅提供一个 `version.dll`：保留名称，或改名为 `dxgi.dll` 直接加载，或改名为 `dxgi.asi` 配合 Ultimate ASI Loader x64。只安装一份桥接文件。** ASI 方式中，加载器名为 `version.dll`，本项目桥接文件放在旁边。配置名称始终为 `dlssg_sm86.ini`。若加载器调用 `InitializeASI`，也可使用其他 ASI 名称（UAL 已测试 `dlssg_sm86.asi`）。

修复独立的 ASI 启动问题：旧文件改名后虽被加载，桥接却未初始化。新增真实 Windows DXGI 导出转发。保留 -7 的强制 X3/X4 时间修正、DX12 + Vulkan 和四项 INI 选项，包括参考原项目的 HardwareBilinear。模型、权重及内核未变，不宣称新的 FPS 提升。

用户已在 RTX 3070 Ti Laptop 8 GB 上确认，此准确二进制文件以 `dxgi.dll` 在悟空中正常工作。真实 DXGI factory、并发加载、UAL 启动及 DX12/Vulkan 输出与修正 -7 的逐字节一致性均已验证。悟空白色基准图表仍是已知问题；本版本 Vulkan 游戏验证待确认。[安装指南](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/install-loaders.zh-CN.md) · [技术记录](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/research.zh-CN.md)。

Thanks to [sdli1995](https://github.com/sdli1995/dlssg_for_sm86), [Michael Robles / RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp), [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader), and the reporter of [issue #2](https://github.com/SilyNoMeta/dlssg_for_sm86/issues/2).

`version.dll` SHA256 (unchanged when renamed): `a19c3b7b65d3e485674377c8b2c8d71407179d7da314c6f9ccd691b03951fe75`
