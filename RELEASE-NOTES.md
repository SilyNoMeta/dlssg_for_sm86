# DLSSG for RTX 20 / 30 — v0.3.5-3

## English

**Steadier HUD and clean translucent panels on generated frames.**

- 🧭 **HUD flicker fixed in more games.** Some games give DLSS Frame Generation no clean view of the scene, so minimaps, gauges and text shimmered or smeared on generated frames. This is now handled automatically on DX12 (validated in **Crimson Desert**).
- 🪟 **No more double image behind translucent UI.** Translucent panels and minimaps could show a doubled or warped background on generated frames. They now stay clean (validated in **Cyberpunk 2077** and Crimson Desert).
- 🪄 **Nothing to configure.** Active with the default `UIRecomposition=1`. Games that already handle their interface properly are left untouched; `UIRecomposition=0` restores the game's own behavior.
- ✅ Tested in play on RTX 3070 Ti Laptop: Crimson Desert, Cyberpunk 2077, FINAL FANTASY VII REBIRTH, Onimusha: Way of the Sword, Bodycam, REANIMAL (demo).
- Everything else is unchanged: X2–X6, dynamic (DX12) and adaptive (Vulkan) modes, image-quality improvements, optional ReShade panel, five proxy names. NVIDIA FG runtime 310.9.1.

**Upgrade:** replace `version.dll` and the optional panel. Keep your INIs.

## Français

**Interface stable et panneaux translucides nets sur les images générées.**

- 🧭 **Scintillement de l’interface corrigé dans davantage de jeux.** Certains jeux ne donnent pas à DLSS Frame Generation une vue propre de la scène : minimaps, jauges et textes scintillaient ou bavaient sur les images générées. C’est désormais géré automatiquement en DX12 (validé dans **Crimson Desert**).
- 🪟 **Plus d’image dédoublée derrière l’interface translucide.** Les panneaux et minimaps translucides pouvaient laisser voir un fond dédoublé ou déformé sur les images générées. Ils restent désormais nets (validé dans **Cyberpunk 2077** et Crimson Desert).
- 🪄 **Rien à configurer.** Actif avec `UIRecomposition=1` (par défaut). Les jeux qui gèrent déjà correctement leur interface ne sont pas modifiés ; `UIRecomposition=0` rétablit le comportement du jeu.
- ✅ Testé en jeu sur RTX 3070 Ti Laptop : Crimson Desert, Cyberpunk 2077, FINAL FANTASY VII REBIRTH, Onimusha: Way of the Sword, Bodycam, REANIMAL (démo).
- Le reste est inchangé : X2–X6, modes dynamique (DX12) et adaptatif (Vulkan), améliorations de qualité d’image, panneau ReShade facultatif, cinq noms de proxy. Runtime NVIDIA FG 310.9.1.

**Mise à jour :** remplacer `version.dll` et le panneau facultatif. Conserver vos INI.

---

## Earlier 0.3.5 builds / Versions 0.3.5 précédentes

| Version | Summary |
|---|---|
| 0.3.5-2 | Engine built into the proxy; the ReShade panel became optional. |
| 0.3.5-1 | Image-quality improvements for fine detail and moving shadows, automatic interface handling, five proxy names. |
| 0.3.5-0 | Rebased on upstream 0.3.5; adaptive Vulkan mode and ReShade 6.8 controls. |

These builds are superseded by 0.3.5-3.
