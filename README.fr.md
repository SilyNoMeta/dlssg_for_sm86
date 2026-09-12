<div align="center">

<h1>DLSS Frame Generation</h1>
<p>Vos images, vos réglages. Désormais pilotables depuis ReShade.</p>
<p><img alt="310.9.1-10" src="https://img.shields.io/badge/release-310.9.1--10-76b900?style=flat-square"> <img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square"> <img alt="DX12 and Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square"></p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-10/dlssg-310.9.1-10-dll-win64.zip">Télécharger DLL / ASI</a> · <a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-10/dlssg-310.9.1-10-reshade-win64.zip">Télécharger l’add-on ReShade</a></strong></p>
<p><a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.zh-CN.md">简体中文</a></p>

</div>

---


**La 310.9.1-10 propose deux façons d’utiliser le même moteur :** une DLL classique ou un add-on ReShade autonome avec des réglages accessibles pendant le jeu. Basé sur le [projet original de sdli1995](https://github.com/sdli1995/dlssg_for_sm86).

## Choisissez un paquet

| Paquet | Pour quel usage ? | Fichiers à installer |
|---|---|---|
| **DLL / ASI** | Installation légère, INI et raccourcis facultatifs, sans dépendre de ReShade. | `version.dll` + `dlssg_sm86.ini` |
| **ReShade** | Panneau en jeu : multiplicateur, DMFG, enregistrement des touches et sauvegarde. | `DLSSG.addon64` + `dlssg_sm86.ini`, avec ReShade et le support complet des add-ons |

**L’un ou l’autre, pas les deux.** L’add-on contient déjà le moteur : aucune DLL/ASI supplémentaire de notre projet ni `DLSSGControls.addon64` n’est nécessaire. ReShade et OptiScaler ne sont pas inclus dans les ZIP.

Fermez le jeu, sauvegardez les fichiers existants et installez près du véritable exécutable (Wukong : `b1/Binaries/Win64`). Activez la FG dans le jeu. Préservez ReShade, les loaders et les autres add-ons ; en changeant de paquet, retirez uniquement notre ancien moteur. Conservez votre INI après vérification de la migration ci-dessous.

[Installation DLL / ASI](docs/install-loaders.fr.md) · [Installation et panneau ReShade](docs/standalone-reshade.fr.md)

## Ce que vous pouvez faire

| Fonction | En pratique |
|---|---|
| **X2 à X6** | Choisir un multiplicateur dans les limites du plugin chargé. X4 correspond à une image rendue et trois images générées. |
| **Dynamic MFG natif** | Choisir une cible et laisser NVIDIA adapter le multiplicateur sur les intégrations **DX12 compatibles**. |
| **Réglages en direct** | Raccourcis facultatifs dans les deux paquets ; panneau, enregistrement des touches et sauvegarde avec ReShade. |
| **DX12 + Vulkan** | Même moteur de compatibilité et correction temporelle. Vulkan permet les réglages fixes sur les chemins Streamline reconnus ; le dynamique natif reste limité à DX12. |
| **RTX 30 / RTX 40** | Kernels SM86 et SM89, avec retours sur RTX 3070 Ti Laptop 8 Go et RTX 4090. **RTX 20 / SM75 : expérimental, sans essai sur carte Turing physique.** |
| **Télémétrie facultative** | Cadence CPU des images source, accessible aux outils compatibles. Voir OptiScaler ci-dessous. |

Monter le multiplicateur n’améliore pas toujours le ressenti : la réactivité dépend encore des FPS rendus, et les artefacts peuvent augmenter. Une intégration DLSS FG existante est nécessaire ; ce projet n’ajoute pas la FG à n’importe quel jeu ni de backend DX11. Les intégrations NGX directes restent pilotées par le jeu. Cette release ne revendique pas de nouveau benchmark FPS.

## Votre INI, vos réglages

```ini
[FrameGeneration]
MaxInterpolatedFrames=5
ForceMultiplier=0
DynamicMFG=0
DynamicTargetFPS=0
```

- **`MaxInterpolatedFrames`** compte les images générées : **1–5 = X2–X6**, défaut 5. La valeur 1 conserve X2 et ses correctifs nécessaires.
- **`ForceMultiplier`** utilise le facteur affiché : 0 suit le jeu ; 2–6 demande un facteur fixe, dans les limites du plafond.
- **`DynamicMFG=1`** demande le dynamique natif. **`DynamicTargetFPS`** accepte 1–1000 ; 0 utilise la cible de l’écran. Aucun profil FPS n’est imposé.
- **`[Logging] Enabled=0`** coupe notre journal ; défaut 1. Les anciens fichiers sont conservés.
- **`[Telemetry] Enabled=1`** active la cadence source ; défaut 0.

**Migration :** remplacer `MaxMultiplier=M` par `MaxInterpolatedFrames=M-1` (6 devient 5). L’ancienne clé de plafond n’est plus lue. `ForceMultiplier` garde son sens. Dans `[Hotkeys]`, l’action dynamique s’appelle `ActivateDynamicMFG` ; conserver l’activation `DynamicMFG` dans `[FrameGeneration]`.

Les modifications manuelles de l’INI demandent un redémarrage. Dans ReShade, **Apply for this session** est temporaire ; **Apply & save settings** conserve le mode et la cible. **Record** capture une combinaison, puis **Save keyboard shortcuts** sauvegarde les touches séparément. **Aucune touche par défaut.** [Référence et syntaxe des raccourcis](docs/live-controls.fr.md).

**Cible ignorée ?** L’override NVIDIA **Override DLSSG Target Frame Rate**, global ou propre au jeu, peut remplacer une cible acceptée par Streamline. Désactivez l’override concerné pour piloter la cible depuis le panneau, puis relancez le jeu. Ce réglage est distinct du limiteur FPS classique et de VSync. Une cible DMFG ne garantit pas un plafonnement exact des FPS. Le raccourci dynamique reprend la cible sauvegardée dans l’INI : sauvegardez votre cible pour la réutiliser avec cette touche.

## Quatre optimisations facultatives

Toutes valent 1 par défaut dans `[Optimizations]`. Mettre une option à 0 puis redémarrer permet de comparer. Les gains dépendent de la charge et peuvent rester modestes. La correction temporelle reste active même si les quatre options sont coupées.

| Clé | Rôle |
|---|---|
| `HardwareBilinear` | Filtrage matériel pour la reconstruction, inspiré de [l’option originale](https://github.com/sdli1995/dlssg_for_sm86/blob/main/docs/NATIVE_INI.md) ; de petites différences de pixels sont possibles. |
| `Conv13SharedInput` | Réutilisation des entrées d’une convolution en mémoire partagée GPU. |
| `Conv0SharedInput` | Même principe pour une autre convolution. |
| `ResidualVectorLoads` | Regroupement des lectures mémoire dans les convolutions résiduelles. |

Ada utilise le même modèle FP16 compilé pour SM89 ; aucun mode FP8/INT8 ni modèle réduit n’est inclus. [Historique technique et validation](docs/research.fr.md).

## OptiScaler et outils complémentaires

**L’intégration OptiScaler attend la [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156).** Le producteur de données est inclus ici, mais OptiScaler doit être compilé avec ce changement pour les lire. L’INI seul ne met pas à jour un ancien OptiScaler. Il s’agit d’une cadence de soumission CPU, pas d’une mesure de fin de rendu GPU ou de latence. Notre panneau ReShade peut l’afficher indépendamment lorsqu’elle est disponible.

Vous débutez ? **[RHI](https://github.com/RankFTW/RHI)** facilite la gestion des versions DLSS et des outils associés ; choisissez ensuite un paquet ci-dessus. Le testeur rapporte une très bonne compatibilité avec le [DLSS Tool de ShortFuse](https://discord.com/channels/1408098019194310818/1543975158937821315) et son [Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884), également disponibles via RHI. Leur support NR reste distinct du support FG de ce projet. Si ces outils vous aident, laissez une étoile à [RHI](https://github.com/RankFTW/RHI) et [RenoDX de ShortFuse](https://github.com/clshortfuse/renodx) !

## Versions et retours

| Version | Différence |
|---|---|
| **[310.9.1-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10)** | Commencez ici : deux installations, commandes en direct, kernels multiarch, journal désactivable et télémétrie facultative. |
| [310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) | Première version dynamique natif / X6, ancienne syntaxe du plafond INI. |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | DLL renommable, X2–X4 corrigés. |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | Première correction du mouvement MFG, `version.dll` uniquement. |

Les versions -0 à -6 ont été retirées pour un mouvement MFG incorrect. Le rectangle blanc sur le graphique du benchmark Wukong reste un problème connu. Les commandes de l’add-on autonome et les changements de cible dynamique ont été confirmés dans Wukong ; cela ne valide pas tous les jeux. Linux/Proton et DXVK ne sont pas validés.

[Signalez un problème](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) avec GPU/VRAM, pilote, jeu/API, version Streamline chargée, paquet choisi, INI et réglages NR. D’autres configurations, notamment RTX 20, sont les bienvenues.

---

Credits: [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) · [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75) · [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) · [MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) · [ReShade](https://reshade.me/) · [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader). [Third-party notices](THIRD_PARTY_NOTICES.txt) · [Checksums](SHA256SUMS.txt)
