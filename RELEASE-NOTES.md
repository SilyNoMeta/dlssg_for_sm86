# 310.9.1-9 · Dynamic MFG & X6

[English](#english) · [Français](#français) · [简体中文](#简体中文)

## English

**Let the multiplier follow the scene.** This release adds native Dynamic MFG on
compatible DX12 integrations, fixed multipliers up to X6, and controls in one
editable INI. Set your own target, enable FG in the game, and let the NVIDIA
runtime choose the multiplier. Targets do not guarantee constant FPS.

- **Fixed X2–X6:** constrained by the loaded plugin's capabilities.
- **Native Dynamic MFG:** DX12, with capability checks and a supported fixed fallback.
- **Activation fix:** system capabilities now carry across different views used
  to query support and configure rendering; each view retains its own presentation state.
- **One universal DLL:** `version.dll`, `dxgi.dll` or ASI. DX12 + Vulkan, corrected
  temporal placement and all four optional optimizations are retained.
- **Your settings:** edit one INI to follow the game, request fixed X2–X6, or set a dynamic target.

The root INI leaves the game in charge, with an X6 ceiling where supported.
Edit `dlssg_sm86.ini` beside our DLL to choose your own values, then restart.
Keeping an old INI without `[FrameGeneration]` retains the X4 ceiling
and does not request the new modes. Fixed overrides require recognized Streamline.
Native dynamic is not enabled on Vulkan; no separate adaptive Vulkan controller is included.

Functional dynamic switching is user-confirmed on RTX 3070 Ti Laptop 8 GB,
driver 616.92. The exact binary also passed control/ABI, real Streamline and GPU
image checks. This is not a new FPS/latency benchmark or validation of every game.
The known white Wukong benchmark chart is not fixed by this release.

## Français

**Un multiplicateur qui suit la scène.** Cette release ajoute le Dynamic MFG natif
sur les intégrations DX12 compatibles, les facteurs fixes jusqu'à X6 et des réglages
dans un seul INI modifiable. Indiquez votre cible, activez FG dans le jeu
et laissez le runtime NVIDIA choisir le multiplicateur. La cible ne garantit pas
des FPS constants.

- **X2–X6 fixe :** dans la limite des capacités du plugin chargé.
- **Dynamic MFG natif :** DX12, avec contrôle de compatibilité et repli fixe si possible.
- **Correction d'activation :** les capacités système passent entre la vue qui les
  consulte et celle qui configure le rendu ; l'état de présentation reste propre à chaque vue.
- **Une DLL universelle :** `version.dll`, `dxgi.dll` ou ASI. DX12 + Vulkan,
  placement temporel corrigé et quatre optimisations facultatives conservés.
- **Vos réglages :** un seul INI pour suivre le jeu, demander X2–X6 fixe ou choisir une cible dynamique.

L'INI principal laisse le jeu décider, avec plafond X6 si compatible. Modifiez
`dlssg_sm86.ini` à côté de notre DLL avec les valeurs de votre choix, puis
relancez. Un ancien INI sans `[FrameGeneration]` conserve le plafond X4 sans
demander les nouveaux modes. Le forçage fixe exige un chemin Streamline reconnu.
Le dynamique natif n'est pas activé sous Vulkan ; aucun contrôleur adaptatif
Vulkan distinct n'est inclus.

Les transitions dynamiques sont confirmées en jeu sur RTX 3070 Ti Laptop 8 Go,
pilote 616.92. Le binaire exact passe aussi les contrôles ABI, Streamline réel et
images GPU. Ce retour n'est pas un nouveau benchmark FPS/latence ni une validation
de tous les jeux. Le graphique blanc du benchmark Wukong n'est pas corrigé ici.

## 简体中文

**让倍率随场景而变。** 本版本新增兼容 DX12 集成中的原生 Dynamic MFG、最高 X6
固定倍率，以及一个可自行编辑的 INI。设置自己的目标，在游戏中启用
FG，再由 NVIDIA 运行库选择倍率。目标并不保证实际 FPS 恒定。

- **固定 X2–X6：** 受实际加载插件的能力限制。
- **原生 Dynamic MFG：** DX12，检查支持能力，并在可用时回退至固定倍率。
- **启用修复：** 在查询能力与配置渲染的不同视图间共享系统能力；呈现状态仍各自独立。
- **一个通用 DLL：** `version.dll`、`dxgi.dll` 或 ASI；保留 DX12 + Vulkan、时间位置修正及四项可选优化。
- **自行配置：** 通过一个 INI 跟随游戏、请求固定 X2–X6，或选择动态目标。

根目录 INI 保留游戏选择，并在兼容时允许 X6 上限。在本项目 DLL 旁编辑
`dlssg_sm86.ini`，填写自己需要的值并重启。保留缺少 `[FrameGeneration]`
的旧 INI 时仍为 X4 上限，不请求新模式。固定覆盖需要已识别的 Streamline 路径。
Vulkan 不启用原生动态，也未包含独立的 Vulkan 自适应控制器。

用户已在 RTX 3070 Ti Laptop 8 GB、驱动 616.92 上确认游戏内动态切换。
同一二进制文件通过 ABI、真实 Streamline 和 GPU 图像检查。这不是新的 FPS/延迟
基准，也不代表所有游戏均已验证。本版本未修复悟空基准图表的白色矩形。

---

[Installation / Installation / 安装](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/README.md)
· [Technical notes / Notes techniques / 技术说明](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/feat/dlssg-310.9.1/docs/research.en.md)

Thanks to [sdli1995](https://github.com/sdli1995/dlssg_for_sm86),
[Michael Robles / RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock),
[mavismmg / ImDreamt's MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx),
and [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader).

`version.dll` SHA256: `114004043035c3f8f91b1b8909bdb8b7e68fa36394aeb339c339e30042684561`
