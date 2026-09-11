# DLSSG 310.9.1-6 — DirectX 12 + Vulkan, optional INI

## English

**Start here: [310.9.1-6 — DX12 + Vulkan + configurable optimizations](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-6/dlssg-sm86-310.9.1-6-win64.zip).**
One `version.dll` includes both API paths and all four released optimizations.
The ZIP includes the optional `dlssg_sm86.ini`. All four options default to on.
Use the profiles below to compare earlier kernel combinations without swapping DLLs.
This is an experimental prerelease; a higher revision does not guarantee higher FPS.

| Option | What it controls |
|---|---|
| `HardwareBilinear` | Hardware bilinear filtering during final reconstruction; small pixel differences are possible. |
| `Conv13SharedInput` | Shared-memory reuse of FP16 inputs in one convolution. |
| `Conv0SharedInput` | The same reuse in a second reconstruction convolution. |
| `ResidualVectorLoads` | Vectorized input loads in two residual convolutions. |

The INI configures optimizations on both APIs. The game selects DX12 or Vulkan;
there is no API-switch setting here. These switches do not select X2/X3/X4 or
control a separate Neural Rendering / NR Cost Scaler mod.

Testing so far uses one **RTX 3070 Ti Laptop GPU with 8 GB VRAM**, driver 616.92.
Earlier DX12 versions have user reports from Wukong and Palworld. The same Vulkan
implementation and kernels have a positive No Man's Sky X2/X3/X4 report using a
preview with additional diagnostic logging. Controlled cross-version game
benchmarks are still in progress; no overall speedup is promised.

Hardware bilinear adapts the original project's [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) option. No FP8, INT8, workspace compression or smaller neural model is included. Fully restart the game after changing the INI. Vulkan requires an existing NGX FG integration; this does not add DX11 support.

The exact distributed DLL passed fresh offline checks on both APIs, including
all 16 INI combinations and the supplied INI file. Vulkan X2/X3/X4, history
reset/recovery and the DX12 comparison passed. Matched outputs equal their
corresponding reference paths; loading and cache checks also passed.
These checks do not establish compatibility with every game or an FPS gain.

## 简体中文

**推荐从这里开始：[310.9.1-6 — DX12 + Vulkan + 可配置优化](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-6/dlssg-sm86-310.9.1-6-win64.zip)。**
一个 `version.dll` 包含两种 API 路径和全部四项已发布优化。
ZIP 内含可选的 `dlssg_sm86.ini`，四项优化默认全部开启。
下方配置可重现此前版本的内核组合，无需反复替换 DLL。
本版本仍为实验预发布；版本号更高不保证 FPS 更高。

| 选项 | 作用 |
|---|---|
| `HardwareBilinear` | 最终重建使用硬件双线性过滤，可能出现细微像素差异。 |
| `Conv13SharedInput` | 在共享内存中复用一个卷积的 FP16 输入。 |
| `Conv0SharedInput` | 在第二个重建卷积中复用 FP16 输入。 |
| `ResidualVectorLoads` | 在两个残差卷积中使用向量化输入读取。 |

INI 对两种 API 的优化均有效。DX12 或 Vulkan 由游戏选择，INI 不提供 API 切换。
这些开关不选择 X2/X3/X4，也不控制独立的 Neural Rendering / NR Cost Scaler 模组。

目前测试设备为一台 **RTX 3070 Ti Laptop、8 GB 显存的笔记本**，驱动 616.92。
早期 DX12 版本已有《黑神话：悟空》和《幻兽帕鲁》的用户反馈。
相同 Vulkan 实现与内核的诊断预览版已有《无人深空》X2/X3/X4 成功运行反馈。
该预览版额外记录诊断日志。跨版本受控游戏基准测试仍在进行，不承诺整体性能提升。

硬件双线性借鉴原项目的 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) 选项。不包含 FP8、INT8、工作缓冲区压缩或更小的神经模型。修改 INI 后需完全重启游戏。Vulkan 需要现有的 NGX 帧生成集成，不会添加 DX11 支持。

实际分发的 DLL 已重新通过两种 API 的离线检查，包括全部 16 种 INI
组合和附带的 INI 文件。Vulkan X2/X3/X4、历史重置与恢复以及 DX12 对比均通过。
输出图像与各自参考路径一致，加载和缓存检查也已通过。
这些检查不保证所有游戏兼容，也不代表 FPS 一定提高。

## Français

**Commencez ici : [310.9.1-6 — DX12 + Vulkan + optimisations configurables](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-6/dlssg-sm86-310.9.1-6-win64.zip).**
Une seule `version.dll` contient les deux chemins API et les quatre optimisations publiées.
Le ZIP fournit le fichier facultatif `dlssg_sm86.ini`. Les quatre options sont actives par défaut.
Les profils ci-dessous permettent de comparer les anciennes combinaisons sans changer de DLL.
Cette préversion reste expérimentale ; un numéro plus élevé ne garantit pas plus de FPS.

| Option | Fonction |
|---|---|
| `HardwareBilinear` | Filtrage bilinéaire matériel à la reconstruction finale ; de petits écarts de pixels sont possibles. |
| `Conv13SharedInput` | Réutilisation des entrées FP16 d'une convolution en mémoire partagée. |
| `Conv0SharedInput` | Même réutilisation dans une seconde convolution de reconstruction. |
| `ResidualVectorLoads` | Lectures vectorisées dans deux convolutions résiduelles. |

L'INI règle les optimisations pour les deux API. Le jeu choisit DX12 ou Vulkan ;
il n'y a pas de sélection d'API dans ce fichier. Ces options ne choisissent pas
X2/X3/X4 et ne contrôlent pas les mods Neural Rendering / NR Cost Scaler.

Les essais utilisent un seul **portable RTX 3070 Ti mobile avec 8 Go de VRAM**, pilote 616.92.
Les premières versions DX12 ont des retours sur Wukong et Palworld. La même
implémentation Vulkan et les mêmes kernels ont un premier retour positif X2/X3/X4
dans No Man's Sky, avec une préversion ajoutant des journaux de diagnostic.
Les benchmarks comparatifs en jeu sont en cours ; aucun gain global n'est promis.

Le bilinéaire adapte l'option [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) du projet original. Ni FP8, ni INT8, compression des buffers ou modèle neuronal réduit ne sont inclus. Redémarrez le jeu après modification de l'INI. Vulkan nécessite une intégration NGX FG existante ; cela n'ajoute pas le support DX11.

La DLL distribuée passe de nouvelles vérifications hors jeu sur les deux API,
dont les 16 combinaisons INI et le fichier INI fourni. Vulkan X2/X3/X4,
la remise à zéro de l'historique et sa reprise ainsi que la comparaison DX12 passent.
Les images correspondent aux chemins de référence respectifs ; les contrôles de
chargement et de cache passent aussi. Cela ne garantit ni tous les jeux ni un gain de FPS.

`version.dll` SHA256: `cb471f9606e41049a48ee4c5405d420e662dd264622ccbc87990903e3f03c69b`

---

# DLSSG 310.9.1-5 — Optional INI controls

## English

The `-4` kernels, with an optional INI to switch four optimizations on/off. Same default image path as `-4`; convenient for comparing the earlier kernel combinations.

Experimental prerelease, checked offline on an RTX 3070 Ti Laptop (8 GB).
The added memory-access changes preserve FP16 arithmetic, and tested outputs
match `-2` with hardware bilinear enabled. There is no consistent measured
overall performance gain and no game validation yet for this revision.
No FP8 or INT8 is included. Keep your working DLL to compare and revert.
Hardware bilinear follows the idea of upstream's [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) option; small
differences versus the manual bilinear path in `-0` remain possible.

Optional `dlssg_sm86.ini` beside the DLL: four 0/1 switches, all enabled by default; fully restart the game after edits. All 16 combinations passed offline checks. Profiles for `-0` through `-4` are documented in the README.

[Version comparison and installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-5/README.en.md)

## 简体中文

使用 `-4` 内核，通过可选 INI 开关控制四项优化。 默认图像处理路径与 `-4` 相同，便于对比此前版本的内核组合。

实验预发布版本，已在 RTX 3070 Ti Laptop（8 GB）上进行离线检查。
新增内存读取改动保留 FP16 运算；启用硬件双线性时，已测试的输出与 `-2` 一致。
尚未确认整体性能有稳定提升，本修订版也尚未进行游戏实测。
不含 FP8 或 INT8。请保留已验证可用的 DLL，便于对比和回退。
双线性优化借鉴原项目的 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) 选项，与 `-0` 手动双线性路径相比仍可能有细微像素差异。

可选的 `dlssg_sm86.ini` 放在 DLL 旁：四项 0/1 开关，默认全部开启；修改后需完全重启游戏。16 种组合均通过离线检查。README 提供 `-0` 至 `-4` 的配置组合。

[版本对比与安装](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-5/README.zh-CN.md)

## Français

Les kernels de la `-4`, avec un INI facultatif pour activer ou désactiver quatre optimisations. Même traitement d'image par défaut que la `-4` ; permet de comparer les combinaisons des versions précédentes.

Préversion expérimentale vérifiée hors jeu sur une RTX 3070 Ti mobile (8 Go).
Les nouvelles lectures mémoire conservent les calculs FP16 ; les sorties testées
correspondent à la `-2` lorsque le bilinéaire matériel est actif. Aucun gain
global constant n'est établi et cette révision n'a pas encore été essayée en jeu.
Ni FP8 ni INT8. Conservez votre DLL fonctionnelle pour comparer et revenir en arrière.
Le bilinéaire reprend l'idée de l'option [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) du projet original ; de petits
écarts avec le bilinéaire manuel de la `-0` restent possibles.

`dlssg_sm86.ini` facultatif à côté de la DLL : quatre interrupteurs 0/1, tous actifs par défaut ; redémarrez le jeu après modification. Les 16 combinaisons passent les vérifications hors jeu. Le README donne les profils `-0` à `-4`.

[Comparatif et installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-5/README.fr.md)

`version.dll` SHA256: `4e0d1ed6068a7e9cb13789e72b02001b39ed83575e84a5754a5dc3761e91d4fe`

---

# DLSSG 310.9.1-4 — Vectorized residual input loads

## English

Everything in `-3`, plus vectorized input loads in two residual convolutions. Offline image checks match `-2`; total GPU-time changes remain small and variable.

Experimental prerelease, checked offline on an RTX 3070 Ti Laptop (8 GB).
The added memory-access changes preserve FP16 arithmetic, and tested outputs
match `-2` with hardware bilinear enabled. There is no consistent measured
overall performance gain and no game validation yet for this revision.
No FP8 or INT8 is included. Keep your working DLL to compare and revert.
Hardware bilinear follows the idea of upstream's [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) option; small
differences versus the manual bilinear path in `-0` remain possible.

[Version comparison and installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-4/README.en.md)

## 简体中文

包含 `-3`，并在两个残差卷积中使用向量化输入读取。 离线图像与 `-2` 一致；GPU 总耗时变化较小且存在波动。

实验预发布版本，已在 RTX 3070 Ti Laptop（8 GB）上进行离线检查。
新增内存读取改动保留 FP16 运算；启用硬件双线性时，已测试的输出与 `-2` 一致。
尚未确认整体性能有稳定提升，本修订版也尚未进行游戏实测。
不含 FP8 或 INT8。请保留已验证可用的 DLL，便于对比和回退。
双线性优化借鉴原项目的 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) 选项，与 `-0` 手动双线性路径相比仍可能有细微像素差异。

[版本对比与安装](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-4/README.zh-CN.md)

## Français

Tout le contenu de la `-3`, plus des lectures vectorisées dans deux convolutions résiduelles. Images identiques à la `-2` dans les tests hors jeu ; variations du temps GPU total faibles et irrégulières.

Préversion expérimentale vérifiée hors jeu sur une RTX 3070 Ti mobile (8 Go).
Les nouvelles lectures mémoire conservent les calculs FP16 ; les sorties testées
correspondent à la `-2` lorsque le bilinéaire matériel est actif. Aucun gain
global constant n'est établi et cette révision n'a pas encore été essayée en jeu.
Ni FP8 ni INT8. Conservez votre DLL fonctionnelle pour comparer et revenir en arrière.
Le bilinéaire reprend l'idée de l'option [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) du projet original ; de petits
écarts avec le bilinéaire manuel de la `-0` restent possibles.

[Comparatif et installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-4/README.fr.md)

`version.dll` SHA256: `ebecb4044384ca283bfa77d033fec9a25db376d8ee3a98378dde659b28266d9c`

---

# DLSSG 310.9.1-3 — FP16 reconstruction input reuse

## English

Everything in `-2`, plus FP16 input reuse in a second reconstruction convolution. Offline image checks match `-2`; no consistent total GPU-time improvement established.

Experimental prerelease, checked offline on an RTX 3070 Ti Laptop (8 GB).
The added memory-access changes preserve FP16 arithmetic, and tested outputs
match `-2` with hardware bilinear enabled. There is no consistent measured
overall performance gain and no game validation yet for this revision.
No FP8 or INT8 is included. Keep your working DLL to compare and revert.
Hardware bilinear follows the idea of upstream's [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) option; small
differences versus the manual bilinear path in `-0` remain possible.

[Version comparison and installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-3/README.en.md)

## 简体中文

包含 `-2`，并在第二个重建卷积中复用 FP16 输入。 离线图像与 `-2` 一致；尚未确认 GPU 总耗时有稳定改善。

实验预发布版本，已在 RTX 3070 Ti Laptop（8 GB）上进行离线检查。
新增内存读取改动保留 FP16 运算；启用硬件双线性时，已测试的输出与 `-2` 一致。
尚未确认整体性能有稳定提升，本修订版也尚未进行游戏实测。
不含 FP8 或 INT8。请保留已验证可用的 DLL，便于对比和回退。
双线性优化借鉴原项目的 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) 选项，与 `-0` 手动双线性路径相比仍可能有细微像素差异。

[版本对比与安装](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-3/README.zh-CN.md)

## Français

Tout le contenu de la `-2`, plus la réutilisation des entrées FP16 d'une seconde convolution de reconstruction. Images identiques à la `-2` dans les tests hors jeu ; aucun gain constant sur le temps GPU total établi.

Préversion expérimentale vérifiée hors jeu sur une RTX 3070 Ti mobile (8 Go).
Les nouvelles lectures mémoire conservent les calculs FP16 ; les sorties testées
correspondent à la `-2` lorsque le bilinéaire matériel est actif. Aucun gain
global constant n'est établi et cette révision n'a pas encore été essayée en jeu.
Ni FP8 ni INT8. Conservez votre DLL fonctionnelle pour comparer et revenir en arrière.
Le bilinéaire reprend l'idée de l'option [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) du projet original ; de petits
écarts avec le bilinéaire manuel de la `-0` restent possibles.

[Comparatif et installation](https://github.com/SilyNoMeta/dlssg_for_sm86/blob/v310.9.1-3/README.fr.md)

`version.dll` SHA256: `88590393c03366f0744c77006310573fc6d96ca968669a267459128ca47fb2ec`

---

# DLSSG 310.9.1-2 — FP16 input reuse

## English

This revision keeps the hardware bilinear optimization from `-1` and adds
shared-memory reuse of FP16 inputs in one convolution to reduce repeated
global-memory reads. FP16 arithmetic is preserved; FP8 is not used.

The effect is modest: offline X4 measurements suggest around **0.4–0.5% less
total GPU generation time**, with variability, not an in-game FPS claim.
On an **RTX 3070 Ti Laptop, 8 GB**, our tester could not clearly tell whether
it felt better or worse and reported no obvious visual issue. Comparisons
for the added optimization produced identical images in the tested cases.
It is an experimental option to try, not a promise of a noticeable improvement.

The global README now compares [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0), [310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1) and [310.9.1-2](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-2).
Try them with the same settings and keep the version you prefer. Reports from
other GPUs, laptops/desktops and games are welcome.

## 简体中文

本版本保留 `-1` 的硬件双线性优化，并在一个卷积中利用共享内存复用 FP16 输入，
减少重复的全局内存读取。FP16 运算保持不变，没有使用 FP8。

效果较小：离线 X4 测量显示，**GPU 帧生成总耗时大约减少 0.4–0.5%**，但存在波动，
这不是游戏内 FPS 提升的承诺。在 **RTX 3070 Ti Laptop、8 GB 显存的笔记本**上，
测试用户无法明确判断体验更好还是更差，也未发现明显画面问题。新增优化在已测试
案例中的图像对比完全一致。这是供尝试的实验选项，不保证能感受到明显改善。

README 现已提供 [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)、[310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1) 和 [310.9.1-2](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-2) 的对比表。
建议使用相同设置分别尝试，选择自己更喜欢的版本。欢迎其他显卡、笔记本、台式机及游戏的反馈。

## Français

Cette révision conserve le bilinéaire matériel de la `-1` et réutilise les
entrées FP16 d'une convolution en mémoire partagée pour réduire les lectures
répétées en mémoire globale. Les calculs FP16 sont conservés ; aucun FP8 n'est ajouté.

L'effet est modeste : les mesures X4 hors jeu suggèrent environ **0,4 à 0,5 %
de temps GPU total de génération en moins**, avec de la variabilité. Ce n'est
pas une promesse de gain de FPS en jeu. Sur son **portable RTX 3070 Ti mobile,
8 Go**, notre testeur ne distingue pas clairement si le ressenti est meilleur
ou moins bon, et ne rapporte aucun problème visuel évident. Les comparaisons
de l'optimisation ajoutée donnent des images identiques dans les cas testés.
C'est une option expérimentale à essayer, sans amélioration perceptible garantie.

Le README global compare maintenant les versions [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0), [310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1) et [310.9.1-2](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-2).
Essayez-les à réglages identiques et gardez celle qui vous convient le mieux.
Les retours d'autres GPU, portables, PC fixes et jeux sont les bienvenus.

## HardwareBilinear

**EN:** `-1` and `-2` follow the idea of the original project's [`HardwareBilinear`](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md)
option with a bridge-specific implementation, always enabled and without an INI
switch. `-0` retains the previous sampling path. Bilinear sampling can cause
small pixel differences versus `-0`; the new FP16 input reuse is a separate change.

**中文：** `-1` 和 `-2` 的双线性实现借鉴原项目的上述选项，并针对本桥接进行了适配，
始终启用且没有 INI 开关。`-0` 保留原采样路径。双线性优化可能导致与 `-0` 的轻微像素差异；
本次 FP16 输入复用是另一项独立改动。

**FR :** Les `-1` et `-2` adaptent le principe de cette option amont à notre pont,
toujours actif et sans INI. La `-0` conserve l'échantillonnage précédent. Le
bilinéaire peut modifier légèrement les pixels par rapport à la `-0` ; la
réutilisation des entrées FP16 est une modification distincte.

## Installation / 安装 / Installation

- **EN:** Exit the game, back up your current `version.dll`, then replace it with
  this release's DLL. See the [version comparison and installation instructions](README.md).
- **中文：** 退出游戏并备份当前 `version.dll`，然后替换为本版本 DLL。
  参阅[版本对比及安装说明](README.zh-CN.md)。
- **FR :** Fermez le jeu, sauvegardez votre `version.dll` actuel, puis remplacez-le
  par celui de cette release. Voir le [comparatif et les instructions](README.fr.md).

`version.dll` SHA256: `836b8af6f9e27ea24cbbdcc8b2d9073cb4670edf31699c9fd44ef8df0f3de905`

---

# DLSSG 310.9.1-1 — Hardware Bilinear

## English

This revision enables **hardware bilinear filtering** in the final output
reconstruction stage. Hardware-filtered texture reads replace manual bilinear
interpolation to reduce work. This is an approximate sampling path: generated
pixels can differ slightly from 310.9.1-0.

It follows the same optimization idea as the original project's
[`HardwareBilinear` option](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md),
with an implementation adapted to our 310.9.1 bridge. Here it is **always enabled**;
there is no INI switch. Use [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)
to return to the previous sampling path.

Our tester reports a **small subjective improvement** on an RTX 3070 Ti Laptop
with 8 GB VRAM. A repeatable overall performance gain has not been established;
results depend on the game and scene. Other configurations' reports are welcome.
X2/X3/X4 passed offline checks. Small differences in synthetic images do not
guarantee identical quality in every game, especially in motion or HDR.

## 简体中文

本次更新在最终图像重建阶段启用**硬件双线性过滤**，用硬件过滤的纹理读取
替代手动双线性插值，以减少计算工作。这是一条近似采样路径，生成帧的像素
可能与 310.9.1-0 略有不同。

其优化思路与原项目的
[`HardwareBilinear` 选项](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md)
相同，但实现针对本项目的 310.9.1 桥接架构进行了适配。本版本**始终启用**
该路径，没有 INI 开关。如需恢复此前的采样方式，请使用
[310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)。

测试用户在配备 RTX 3070 Ti Laptop、8 GB 显存的笔记本上反馈有**轻微的主观改善**。
目前尚未确认可重复的整体性能提升，效果取决于游戏和场景。欢迎其他配置的反馈。
X2/X3/X4 已通过离线检查。合成图像中的微小差异并不保证所有游戏、运动场景或 HDR
下的画质均相同。

## Français

Cette révision active le **filtrage bilinéaire matériel** dans l'étape finale de
reconstruction de l'image. Des lectures de texture filtrées par le matériel
remplacent l'interpolation bilinéaire manuelle pour réduire le travail effectué.
Cet échantillonnage est approximatif : les pixels générés peuvent légèrement
différer de ceux de 310.9.1-0.

Le principe rejoint l'option
[`HardwareBilinear` du projet original](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md),
avec une implémentation adaptée à notre pont 310.9.1. Ici, il est **toujours actif**,
sans réglage INI. Revenir à [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)
permet de retrouver l'échantillonnage précédent.

Notre testeur rapporte une **petite amélioration ressentie** sur son portable
RTX 3070 Ti mobile, 8 Go. Aucun gain global reproductible n'est établi ; le
résultat dépend du jeu et de la scène. Les retours d'autres configurations sont
bienvenus. X2/X3/X4 passent les contrôles hors jeu. De faibles écarts sur des
images synthétiques ne garantissent pas une qualité identique dans tous les
jeux, notamment en mouvement ou en HDR.

## Installation / 安装 / Installation

- **English:** Exit the game, back up the current `version.dll`, then replace it
  with this release's DLL. One file is sufficient; do not add the upstream INI.
  Keep 310.9.1-0 as a rollback. See the [English README](README.md).
- **简体中文：** 退出游戏并备份现有 `version.dll`，然后替换为本版本 DLL。
  只需一个文件，无需添加上游 INI。保留 310.9.1-0 以便回退。参阅[中文说明](README.zh-CN.md)。
- **Français :** Fermer le jeu, sauvegarder le `version.dll` actuel puis le remplacer
  par celui de cette release. Un seul fichier suffit, sans INI amont. Conserver
  310.9.1-0 pour revenir en arrière. Voir le [README français](README.fr.md).

The runtime remains DLSSG 310.9.1. Windows x64, Direct3D 12, SM86/RTX 30;
game integration determines the available multipliers.

`version.dll` SHA256: `fb600773397b54e2fd68f18541e4115cb9a67a0cb24d5198d7e7d40337e3d425`
