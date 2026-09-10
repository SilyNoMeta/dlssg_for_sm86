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
