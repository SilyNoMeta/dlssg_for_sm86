# DLSSG for RTX 20 / 30 — v0.3.5-4

## English

**No more doubled shadows on generated frames.**

- 🌗 **Doubled shadows fixed.** A moving character's shadow could appear twice on generated frames, for example when running with the sun behind you in **Cyberpunk 2077**. It now stays single, and fences, wires and foliage stay as sharp as before.
- Includes everything from 0.3.5-3: steadier HUD in games that give DLSS Frame Generation no clean view of the scene (**Crimson Desert**), and clean translucent panels (**Cyberpunk 2077**), fully automatic with `UIRecomposition=1`.
- ✅ Tested in play on RTX 3070 Ti Laptop: Cyberpunk 2077 and Crimson Desert for this build; FINAL FANTASY VII REBIRTH, Onimusha: Way of the Sword, Bodycam and REANIMAL (demo) with 0.3.5-3.
- Everything else is unchanged: X2–X6, dynamic (DX12) and adaptive (Vulkan) modes, optional ReShade panel, five proxy names. NVIDIA FG runtime 310.9.1.

**Upgrade:** replace `version.dll` and the optional panel. Keep your INIs.

## Français

**Plus d’ombres dédoublées sur les images générées.**

- 🌗 **Ombres dédoublées corrigées.** L’ombre d’un personnage en mouvement pouvait apparaître en double sur les images générées, par exemple en courant dos au soleil dans **Cyberpunk 2077**. Elle reste désormais unique, et grillages, câbles et végétation restent aussi nets qu’avant.
- Inclut tout le contenu de la 0.3.5-3 : interface stable dans les jeux qui ne donnent pas à DLSS Frame Generation une vue propre de la scène (**Crimson Desert**) et panneaux translucides nets (**Cyberpunk 2077**), automatiquement avec `UIRecomposition=1`.
- ✅ Testé en jeu sur RTX 3070 Ti Laptop : Cyberpunk 2077 et Crimson Desert pour cette version ; FINAL FANTASY VII REBIRTH, Onimusha: Way of the Sword, Bodycam et REANIMAL (démo) avec la 0.3.5-3.
- Le reste est inchangé : X2–X6, modes dynamique (DX12) et adaptatif (Vulkan), panneau ReShade facultatif, cinq noms de proxy. Runtime NVIDIA FG 310.9.1.

**Mise à jour :** remplacer `version.dll` et le panneau facultatif. Conserver vos INI.

---

## Earlier 0.3.5 builds / Versions 0.3.5 précédentes

| Version | Summary |
|---|---|
| 0.3.5-3 | Steadier HUD where games give DLSS Frame Generation no clean scene view; clean translucent panels. |
| 0.3.5-2 | Engine built into the proxy; the ReShade panel became optional. |
| 0.3.5-1 | Image-quality improvements for fine detail and moving shadows, automatic interface handling, five proxy names. |
| 0.3.5-0 | Rebased on upstream 0.3.5; adaptive Vulkan mode and ReShade 6.8 controls. |

These builds are superseded by 0.3.5-4.
