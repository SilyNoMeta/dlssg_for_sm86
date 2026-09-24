<div align="center">

# DLSS Frame Generation pour RTX 20 / 30

**Multi Frame Generation jusqu’à X6, une interface plus stable et des détails fins plus nets — avec ou sans ReShade.**

<a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v0.3.5-3/DLSSG-RTX20-30-v0.3.5-3-clean-win64.zip"><img alt="Télécharger 0.3.5-3" src="https://img.shields.io/badge/T%C3%A9l%C3%A9charger-0.3.5--3-76b900?style=for-the-badge&logo=nvidia&logoColor=white"></a>

<img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-0078D4?style=flat-square&logo=windows&logoColor=white"> <img alt="DX12 et Vulkan" src="https://img.shields.io/badge/API-DX12%20%7C%20Vulkan-30363d?style=flat-square"> <img alt="RTX 30" src="https://img.shields.io/badge/RTX%2030-pris%20en%20charge-76b900?style=flat-square"> <img alt="RTX 20" src="https://img.shields.io/badge/RTX%2020-exp%C3%A9rimental-d29922?style=flat-square"> <img alt="NVIDIA FG 310.9.1" src="https://img.shields.io/badge/NVIDIA%20FG-310.9.1-555?style=flat-square">

[English](README.en.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [Guide d’installation](docs/INSTALL.md) · [Notes de version](RELEASE-NOTES.md)

</div>

> [!IMPORTANT]
> Expérimental. Fonctionne uniquement dans les jeux qui proposent déjà **DLSS Frame Generation**, et ne débloque jamais ce que le plugin du jeu ne prend pas en charge.

## ✨ Nouveautés de la 0.3.5-3

| | Ce que vous devriez remarquer |
|---|---|
| 🧭 **Interface stable** | Minimaps, jauges et textes ne scintillent plus et ne bavent plus sur les images générées, dans les jeux qui ne donnent pas à DLSS Frame Generation une vue propre de la scène (par exemple **Crimson Desert**). |
| 🪟 **Panneaux translucides nets** | Plus d’image dédoublée ni de fond déformé derrière les panneaux et minimaps translucides (par exemple **Cyberpunk 2077**). |
| 🪄 **Entièrement automatique** | Aucun nouveau réglage. Actif avec `UIRecomposition=1` (par défaut) en DX12. Les jeux qui gèrent déjà correctement leur interface ne sont pas modifiés. |

## 🚀 Démarrage rapide

1. Fermer le jeu et sauvegarder les fichiers qui seront remplacés.
2. Copier **`version.dll`** à côté de l’exécutable de rendu du jeu.
3. Depuis `config/d3d12`, `config/vulkan-sm86` ou `config/vulkan-sm75`, copier **`dlssg_sm86.ini`** et fusionner notre section dans **`ReShade.ini`** (garder ce fichier même sans ReShade : il contient nos réglages).
4. Pour le panneau et les raccourcis : installer ReShade 6.8 avec prise en charge complète des add-ons et ajouter `optional-panel/DLSSG-SM86-75-COMPANION.addon64`.
5. Activer DLSS Frame Generation dans le jeu.

Vulkan nécessite aussi le runtime NVIDIA correspondant : voir le [guide d’installation](docs/INSTALL.md).

## 🎛️ Ce que vous obtenez

| | |
|---|---|
| **X2 – X6** | Suivre le jeu ou choisir un multiplicateur fixe. X4 = une image rendue et trois générées. |
| **Mode dynamique (DX12)** | Fixer un objectif de FPS et laisser NVIDIA ajuster la génération dans les jeux compatibles. |
| **Mode adaptatif (Vulkan)** | Le multiplicateur suit votre fréquence d’images et l’objectif, de X2 à X6. |
| **Qualité d’image** | Grillages, câbles et végétation plus nets, interface plus stable sur les images générées. |
| **Contrôles en jeu** | Modifier et sauvegarder les réglages par jeu depuis le panneau ReShade, ou avec Ctrl+F2…F12. |
| **Échelle de rendu DLSS** | De DLAA à Ultra Performance ou échelle personnalisée, vérifiée avant sauvegarde. |
| **Correctifs par jeu** | Activation du DLSS de REANIMAL, identité de FINAL FANTASY VII REBIRTH, démarrage de Black Myth: Wukong. |

<details>
<summary><b>⚙️ Réglages</b></summary>

`dlssg_sm86.ini` — relancer le jeu après modification :

```ini
[FrameGeneration]
Optimized=1            ; kernels optimisés et améliorations de qualité (0 = référence)
MaxGeneratedFrames=5   ; jusqu'à X6 si le plugin du jeu le permet
```

`ReShade.ini` — utilisé aussi sans ReShade :

```ini
[DLSSG-SM86-75-COMPANION]
Multiplier=0           ; 0 = suivre le jeu, 2-6 = facteur fixe
Dynamic=0              ; 1 = dynamique (DX12) / adaptatif (Vulkan)
TargetFPS=0            ; 0 = fréquence de l'écran, sinon objectif (pas un plafond)
UIRecomposition=1      ; gestion automatique de l'interface (0 = suivre le jeu, 2 = forcer)
```

Raccourcis (avec le panneau) : **Ctrl+F2–F6** X2–X6 · **Ctrl+F10** mode automatique · **Ctrl+F11** suivre le jeu · **Ctrl+F12** restaurer les réglages sauvegardés.

</details>

<details>
<summary><b>🔌 Noms du proxy</b></summary>

Le même fichier peut être renommé selon ce que charge le jeu. Une seule copie.

| Nom | Quand |
|---|---|
| `version.dll` | Premier choix, Unreal Engine 4/5 compris |
| `dinput8.dll` | Jeux utilisant DirectInput8 |
| `dxgi.dll` | Jeux chargeant DXGI tôt — ne jamais écraser un `dxgi.dll` ReShade existant |
| `winmm.dll` | Jeux utilisant WinMM |
| n’importe quel `.asi` | Avec un chargeur ASI |

</details>

<details>
<summary><b>⬆️ Mise à jour depuis une ancienne version</b></summary>

Remplacer `version.dll`, remplacer notre ancien compagnon par le nouveau panneau facultatif (ou le retirer) et mettre de côté un éventuel ancien `DLSSG-SM86-75-RUNTIME.dll`. Ne jamais garder deux versions de nos add-ons actives. La migration des réglages de la release 11 est dans le [guide d’installation](docs/INSTALL.md#mise-à-jour).

</details>

## 🎮 Testé en jeu

**Crimson Desert · Cyberpunk 2077 · FINAL FANTASY VII REBIRTH · Onimusha: Way of the Sword · Bodycam · REANIMAL (démo)** — RTX 3070 Ti Laptop, DX12. D’autres jeux et le matériel RTX 20 peuvent se comporter différemment ; vos retours sont bienvenus.

## 📦 Versions

| Version | |
|---|---|
| [**0.3.5-3**](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v0.3.5-3) | Version actuelle : interface stable et panneaux translucides nets, avec le moteur intégré et le panneau facultatif. |
| [310.9.1-11](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11) · [-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10) · [-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) · [-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) · [-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | Génération précédente archivée, avec son propre format et ses réglages. |

## 💬 Retours

[Ouvrir un ticket](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) avec GPU et pilote, jeu et API, nom du proxy, les deux INI et `DLSSG-SM86-75-runtime.log`.

---

<div align="center">

Basé sur [sdli1995 / dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) (upstream 0.3.5) · inclut des travaux adaptés de [Tony Joaca / DLSSG-Transfusion](https://github.com/TonyJoaca/DLSSG-Transfusion) (MIT)<br>
Merci à [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75), [Matias Lombo](https://github.com/matiasLombo/mfg-unlock) et [ReShade](https://reshade.me/)<br>
[Mentions tierces](THIRD_PARTY_NOTICES.txt) · [Sommes de contrôle](SHA256SUMS.txt) · non affilié à NVIDIA

</div>
