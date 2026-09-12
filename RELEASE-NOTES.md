# 310.9.1-10 — Live controls, ReShade & RTX 40

[English](README.en.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md)

## English

One release, two alternative packages:

| Download | Contents | Choose it for |
|---|---|---|
| **dlssg-310.9.1-10-dll-win64.zip** | `version.dll` + INI + guides | DLL/ASI loading, INI and optional hotkeys; no ReShade required. |
| **dlssg-310.9.1-10-reshade-win64.zip** | `DLSSG.addon64` + INI + guides | Standalone ReShade panel, live settings, key recording and separate save buttons. |

**Install only one engine.** The add-on already contains the DLL's compatibility functionality. ReShade with full add-on support is required for the second package and is not bundled. No screenshots, test tools or modified OptiScaler are included.

- Live X2–X6 controls and native Dynamic MFG on compatible DX12 integrations. Fixed Vulkan controls require a recognized Streamline path.
- RTX 40 / SM89 route with user-confirmed fixed and dynamic operation; RTX 30 / SM86 retained. RTX 20 / SM75 is included experimentally, without physical Turing validation.
- `MaxInterpolatedFrames` replaces `MaxMultiplier`: generated-frame ceiling 1–5 = X2–X6; default 5. A value of 1 keeps X2 and required patches. `ForceMultiplier` still uses the displayed factor.
- `[Logging] Enabled=0` disables our logging. `[Telemetry] Enabled=1` opts into CPU source-frame submission cadence (not GPU completion or latency).
- [OptiScaler PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156) is awaiting upstream review. A consumer build containing the change is needed; the INI alone will not update existing OptiScaler builds.
- ReShade Record uses captured ReShade input, fixing ignored function keys. **Apply for this session**, **Apply & save settings**, and **Save keyboard shortcuts** serve separate purposes. No default keybindings or FPS target.

**Dynamic target stuck?** NVIDIA's global/per-game **Override DLSSG Target Frame Rate** can take priority over the panel/INI, separately from a normal FPS limit. Disable the relevant override and restart if you want to set the target here. The dynamic shortcut uses the saved INI target; save session edits if you want that shortcut to reuse them.

The corrected temporal motion and four optional optimizations remain, including HardwareBilinear inspired by the original project. No new FP8/INT8 mode or smaller model. Standalone controls and target changes were confirmed in Wukong on RTX 3070 Ti Laptop 8 GB. These are functional reports, not new performance benchmarks. The Wukong benchmark chart's white rectangle remains a known issue.

[Installation and migration](README.en.md) · [Key syntax and telemetry](docs/live-controls.en.md) · [Technical notes](docs/research.en.md)

## Français

**Une release, deux ZIP au choix : DLL/ASI ou ReShade autonome. Ne pas installer les deux moteurs.** L'add-on contient déjà le moteur et demande ReShade avec le support complet des add-ons.

Cette version apporte les réglages en direct et raccourcis facultatifs, le panneau ReShade avec enregistrement des touches et sauvegardes séparées, ainsi que le chemin RTX 40. RTX 30 reste pris en charge ; RTX 20 est expérimental, sans test sur carte physique.

Migrer `MaxMultiplier=M` vers `MaxInterpolatedFrames=M-1` : 1–5 correspond à X2–X6, défaut 5. La valeur 1 conserve X2 et ses correctifs. `ForceMultiplier` garde le facteur affiché. `[Logging] Enabled=0` coupe notre journal ; `[Telemetry] Enabled=1` active la cadence CPU des images source. La PR OptiScaler #1156 attend encore sa fusion et un binaire consommateur compatible.

Aucun raccourci ni objectif FPS imposé. L'override NVIDIA **Override DLSSG Target Frame Rate** peut remplacer la cible du panneau : désactiver l'override concerné et relancer pour piloter la cible ici. Le raccourci dynamique utilise la cible sauvegardée dans l'INI. Le dynamique natif reste limité à DX12 compatible ; Vulkan conserve les contrôles fixes sur Streamline reconnu.

Les optimisations et la correction temporelle sont conservées. Pas de nouveau benchmark ni de mode FP8/INT8. Les commandes de l'add-on et changements de cible ont été confirmés dans Wukong ; le rectangle blanc de son graphique de benchmark reste connu.

[Installation et migration](README.fr.md) · [Référence des commandes](docs/live-controls.fr.md)

## 简体中文

**一个版本，两个可选 ZIP：DLL/ASI 或独立 ReShade。不要同时安装两个引擎。** add-on 已含完整兼容引擎，需要支持完整 add-on 的 ReShade。

新增实时控制、自选快捷键、ReShade 按键录制与独立保存按钮，以及 RTX 40 路径。保留 RTX 30；RTX 20 为实验支持，尚未在实体卡验证。

将 `MaxMultiplier=M` 改为 `MaxInterpolatedFrames=M-1`：1–5 对应 X2–X6，默认 5。1 保留 X2 和必要补丁；`ForceMultiplier` 仍使用显示倍率。`[Logging] Enabled=0` 关闭本项目日志；`[Telemetry] Enabled=1` 开启 CPU 源帧提交速率。OptiScaler PR #1156 仍待合并及包含该改动的读取端构建。

无默认快捷键或目标 FPS。NVIDIA 全局/游戏级 **Override DLSSG Target Frame Rate** 可覆盖面板目标；禁用相关覆盖并重启后才能在这里控制。动态快捷键使用 INI 中保存的目标。原生动态仅限兼容 DX12；Vulkan 固定控制需要识别到 Streamline 路径。

保留时序修正和四项优化，不增加 FP8/INT8 模式，也不声称新的性能基准。独立控制与目标切换已在《黑神话：悟空》确认，基准图表白色矩形仍为已知问题。

[安装与迁移](README.zh-CN.md) · [控制参考](docs/live-controls.zh-CN.md)
