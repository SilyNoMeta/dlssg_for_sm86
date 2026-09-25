# DLSSG for RTX 20 / 30 — v0.3.5-5

## English

**Sharper fine detail on generated frames.**

- 🌿 **Fine detail is back.** Grass, bushes, fences, wires and fine ground textures keep their detail on generated frames instead of shimmering, as in 310.9.1-11.
- 🌗 **Moving shadows stay single**; small specks can remain at the tips of fast-moving limbs.
- 🧭 **Steadier HUD and clean translucent panels**, automatic with `UIRecomposition=1` on DX12, including games that give DLSS Frame Generation no clean view of the scene.
- ✅ Tested in play in **Cyberpunk 2077** on RTX 3070 Ti Laptop and confirmed by a tester. Replaces 0.3.5-3, 0.3.5-4 and the 0.3.5-5b1 beta.
- Everything else is unchanged: X2–X6, dynamic (DX12) and adaptive (Vulkan) modes, optional ReShade panel, five proxy names. NVIDIA FG runtime 310.9.1.

**Upgrade:** replace `version.dll` and the optional panel. Keep your INIs.

## Français

**Détail fin plus net sur les images générées.**

- 🌿 **Le détail fin revient.** Herbe, buissons, grillages, câbles et textures fines du sol gardent leur détail sur les images générées au lieu de scintiller, comme en 310.9.1-11.
- 🌗 **Les ombres en mouvement restent uniques** ; de petites mouchetures peuvent subsister au bout des membres qui bougent vite.
- 🧭 **Interface stable et panneaux translucides nets**, automatiquement avec `UIRecomposition=1` en DX12, y compris dans les jeux qui ne donnent pas à DLSS Frame Generation une vue propre de la scène.
- ✅ Testé en jeu dans **Cyberpunk 2077** sur RTX 3070 Ti Laptop et confirmé par un testeur. Remplace les 0.3.5-3, 0.3.5-4 et la bêta 0.3.5-5b1.
- Le reste est inchangé : X2–X6, modes dynamique (DX12) et adaptatif (Vulkan), panneau ReShade facultatif, cinq noms de proxy. Runtime NVIDIA FG 310.9.1.

**Mise à jour :** remplacer `version.dll` et le panneau facultatif. Conserver vos INI.

---

## Earlier 0.3.5 builds / Versions 0.3.5 précédentes

| Version | Summary |
|---|---|
| 0.3.5-4 | Single shadows on generated frames (withdrawn, superseded by 0.3.5-5). |
| 0.3.5-3 | Steadier HUD and clean translucent panels (withdrawn, superseded by 0.3.5-5). |
| 0.3.5-2 | Engine built into the proxy; the ReShade panel became optional. |
| 0.3.5-1 | Image-quality improvements for fine detail and moving shadows, automatic interface handling, five proxy names. |
| 0.3.5-0 | Rebased on upstream 0.3.5; adaptive Vulkan mode and ReShade 6.8 controls. |

These builds are superseded by 0.3.5-5.
