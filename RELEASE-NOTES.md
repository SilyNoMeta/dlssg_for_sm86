# 310.9.1-11 — live controls, verified render scale and quality experiments

## English

One download: **version.dll**, **dlssg_sm86.ini**, and the optional **DLSSGControls.addon64** ReShade panel. The engine loads early; the panel controls it. Replace the old standalone DLSSG.addon64 when upgrading, keeping ReShade and unrelated add-ons. No ASI loader is required when our engine uses version.dll beside ReShade's dxgi.dll.

- Fixed X2–X6 and native Dynamic MFG on compatible DX12 integrations; fixed controls on recognized Vulkan paths.
- ReShade controls, key recording and independent saves for FG settings, shortcuts and DLSS render scale.
- **DLAA / Quality / Balanced / Performance / Ultra Performance**, plus a 50–100% custom slider. Apply for the session first: a nonzero scale can only be saved after eight consecutive successful DLSS frames match it. Prefer the game's own quality menu when available. If a saved override causes startup trouble, set RenderScale=0.
- **Ctrl+F2–F6**: X2–X6; **Ctrl+F10**: dynamic; **Ctrl+F11**: follow game; **Ctrl+F12**: restore INI. All bindings are configurable; a blank value disables one. No fixed target FPS is supplied.
- Optional **QualityValidWarp**, **BlackwellBlend** and **BlackwellScatter**, with SM75/86/89 ports. All three default to off. They can affect image quality and stability; intermittent GPU hangs occurred during Wukong experiments. No universal improvement is claimed.
- Loader/interposer and device initialization corrections accumulated during testing; compatible control paths no longer depend on the game querying capabilities first.

The established four performance switches and corrected MFG temporal motion remain included. The package **still embeds NVIDIA DLSS-G 310.9.1** and adapted kernels. Supporting external provider versions is future work, not part of this release.

RTX 3070 Ti Laptop 8 GB and RTX 4090 contributed user reports; RTX 20 remains experimental without physical-card validation. The current binaries passed 472 FG assertions, 106 SR assertions, SDK ABI and persistence checks. This is not a complete game matrix or a new benchmark. DLL-only input remains integration-dependent; it previously failed in Wukong, so use the panel if shortcuts do not respond. FSR FG → DLSS FG switching may require a full restart. Native dynamic is DX12-only. Linux/Proton is unvalidated.

OptiScaler telemetry requires a consumer including [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156), still open when checked for this release. No modified OptiScaler is bundled.

[Install](docs/install-loaders.en.md) · [ReShade](docs/reshade-controls.en.md) · [INI](docs/live-controls.en.md) · [Render scale](docs/super-resolution.en.md)

## Français

Un seul ZIP : **version.dll**, **dlssg_sm86.ini** et le panneau ReShade facultatif **DLSSGControls.addon64**. La DLL charge le moteur tôt ; le panneau le contrôle. Remplacez l'ancien DLSSG.addon64 autonome, en conservant ReShade et les autres add-ons.

- X2–X6 et DMFG natif sur les intégrations DX12 compatibles ; réglages fixes sur les chemins Vulkan reconnus.
- Réglages en direct, enregistrement des touches et sauvegardes indépendantes.
- Préréglages DLAA / Quality / Balanced / Performance / Ultra Performance et curseur 50–100 %. Appliquez pour la session : la sauvegarde n'est permise qu'après huit images DLSS consécutives à la bonne résolution. Privilégiez les menus du jeu s'ils proposent déjà ce réglage. Récupération en cas de problème au lancement : RenderScale=0.
- Ctrl+F2–F6 : X2–X6 ; Ctrl+F10 : dynamique ; Ctrl+F11 : suivre le jeu ; Ctrl+F12 : restaurer l'INI. Tous sont modifiables ou désactivables. Aucune cible FPS fixe imposée.
- QualityValidWarp, BlackwellBlend et BlackwellScatter optionnels, portés sur SM75/86/89 et désactivés par défaut. Des blocages GPU intermittents ont été observés pendant les expériences Wukong : aucun gain universel de qualité ou de performances n'est revendiqué.
- Correctifs de chargement, d'initialisation et de contrôles accumulés pendant les essais.

Le runtime NVIDIA 310.9.1 reste embarqué dans cette release. La compatibilité avec des fournisseurs externes viendra séparément. Retours sur RTX 3070 Ti Laptop 8 Go et RTX 4090 ; RTX 20 toujours expérimental sans carte physique testée. Les raccourcis de la DLL seule dépendent de l'intégration et avaient échoué sur Wukong : utilisez le panneau si nécessaire. Le passage FSR FG → DLSS FG peut demander un redémarrage. DMFG natif limité à DX12, Proton non validé. OptiScaler nécessite une version intégrant la PR #1156, encore ouverte lors de la vérification.

[Installation](docs/install-loaders.fr.md) · [ReShade](docs/reshade-controls.fr.md) · [INI](docs/live-controls.fr.md) · [Résolution](docs/super-resolution.fr.md)

## 简体中文

一个 ZIP 包含 **version.dll**、**dlssg_sm86.ini** 和可选 ReShade 面板 **DLSSGControls.addon64**。DLL 提前加载兼容引擎，面板负责控制。升级时移除旧的独立 DLSSG.addon64，保留 ReShade 和其他插件。

- 在兼容 DX12 集成中使用 X2–X6 和原生动态 MFG；Vulkan 的已识别路径支持固定倍率。
- 实时调节、快捷键录制和独立保存。
- DLAA / Quality / Balanced / Performance / Ultra Performance，以及 50–100% 滑块。先应用到会话，连续八帧成功 DLSS 计算与请求分辨率匹配后才能保存。优先使用游戏已有画质菜单。若保存后启动异常，将 RenderScale 设回 0。
- Ctrl+F2–F6：X2–X6；Ctrl+F10：动态；Ctrl+F11：跟随游戏；Ctrl+F12：恢复 INI。均可修改或禁用，不指定固定目标 FPS。
- QualityValidWarp、BlackwellBlend、BlackwellScatter 提供 SM75/86/89 移植，默认关闭。Wukong 实验中出现过间歇性 GPU 挂起，不承诺普遍的画质或性能提升。
- 包含测试期间积累的加载、初始化和控制修正。

本版本仍内置 NVIDIA DLSS-G 310.9.1，外部提供方兼容工作将单独进行。用户反馈来自 RTX 3070 Ti Laptop 8 GB 和 RTX 4090；RTX 20 尚无实体卡验证。仅用 DLL 的快捷键依赖游戏集成，在 Wukong 中曾失败，必要时使用面板。FSR FG 切换至 DLSS FG 可能需要完整重启；原生动态仅限兼容 DX12，Proton 未验证。OptiScaler 需要包含 PR #1156 的版本，该 PR 在发布核查时仍未合并。

[安装](docs/install-loaders.zh-CN.md) · [ReShade](docs/reshade-controls.zh-CN.md) · [INI](docs/live-controls.zh-CN.md) · [分辨率](docs/super-resolution.zh-CN.md)
