# Installation — v0.3.5-5

[README](../README.fr.md) · [English](INSTALL.en.md)

## Prérequis

- Windows x64 et un jeu qui embarque **NVIDIA DLSS Frame Generation** via Streamline (D3D12 ou Vulkan), même si ses menus ne le proposent pas.
- Une carte RTX 30 (testée) ou RTX 20 (expérimental).
- Facultatif : **ReShade 6.8 avec prise en charge complète des add-ons**, uniquement pour le panneau et les raccourcis.

`version.dll` fonctionne seul, sans ReShade. `optional-panel/DLSSG-SM86-75-COMPANION.addon64` ajoute seulement le panneau et les raccourcis. Les réglages sont lus dans `ReShade.ini` même sans ReShade : conserver ce nom de fichier et sa section `[DLSSG-SM86-75-COMPANION]`.

## Installation

1. Fermer le jeu et repérer son exécutable de rendu (par exemple `b1/Binaries/Win64` pour Wukong, `Binaries` pour No Man's Sky).
2. Sauvegarder les fichiers qui seront remplacés. Conserver les autres mods.
3. Copier `version.dll` à côté de cet exécutable. Copier le panneau de `optional-panel/` seulement si ReShade est utilisé.
4. Choisir un dossier dans `config/` et copier son `dlssg_sm86.ini`. Copier son `ReShade.ini` s'il n'en existe pas ; sinon fusionner uniquement notre section.
5. Si notre compagnon figure dans `ADDON.LoadFromDllMain`, retirer cette entrée.
6. Vulkan uniquement : installer le runtime NVIDIA correspondant (section suivante).
7. Lancer le jeu et activer DLSS Frame Generation dans ses options graphiques.

| Gabarit | Pour |
|---|---|
| `config/d3d12` | jeux D3D12 |
| `config/vulkan-sm86` | jeux Vulkan sur RTX 30 |
| `config/vulkan-sm75` | jeux Vulkan sur RTX 20 (expérimental) |

En Vulkan, installer ReShade de la façon habituelle pour ce jeu ; ne pas utiliser une DLL ReShade D3D12 à la place.

## Vulkan : runtime NVIDIA correspondant

Vulkan nécessite le `nvngx_dlssg.dll` NVIDIA **310.9.1** de SHA256 :

```text
ff6e90eb78b827927dff5b4ecc6b1c870c2e9bca29ed9f48c7d348cc9e170b82
```

Si la copie du jeu ne correspond pas, extraire celle fournie dans notre proxy (Python et `pefile` nécessaires) :

```powershell
python -m pip install pefile
python extract_runtime.py --proxy version.dll --out nvngx_dlssg.extracted.dll
Get-FileHash nvngx_dlssg.extracted.dll -Algorithm SHA256
```

Sauvegarder le `nvngx_dlssg.dll` du jeu, puis le remplacer par le fichier extrait sous ce nom. Ne pas remplacer les autres DLL Streamline ni le chargeur Vulkan.

## Réglages

`dlssg_sm86.ini` (relancer le jeu après modification) :

| Clé | Rôle |
|---|---|
| `Optimized=1` | Kernels optimisés et améliorations de qualité d'image. `0` utilise les kernels de référence. |
| `MaxGeneratedFrames=5` | Jusqu'à cinq images générées (X6) si le plugin du jeu le permet. |

`ReShade.ini`, section `[DLSSG-SM86-75-COMPANION]` :

| Clé | Rôle |
|---|---|
| `Multiplier=0` | Suivre le jeu ; `2` à `6` demande un facteur fixe si `Dynamic=0`. |
| `Dynamic=1` | Mode dynamique natif en D3D12, mode adaptatif en Vulkan. |
| `TargetFPS=0` | Cible de l'écran ; `1` à `1000` fixe une cible (pas un plafond garanti). |
| `UIRecomposition=1` | Gestion automatique de l'interface (recommandé). `0` suit le jeu, `2` la force. |
| `DLSSRenderScale=0` | Aucune modification de l'échelle de rendu ; préférer les réglages DLSS du jeu. |
| `HotkeyX2`…`HotkeyX6` | Ctrl+F2 à Ctrl+F6 : X2 à X6 fixes. |
| `HotkeyDynamic`, `HotkeyFollowGame`, `HotkeyRestoreINI` | Ctrl+F10, Ctrl+F11, Ctrl+F12. |

Dans le panneau, **Apply for this session** est temporaire et **Apply & save settings** conserve le choix. Les raccourcis nécessitent le panneau ; un raccourci vide est désactivé. Ne modifier les INI à la main que jeu fermé.

En Vulkan, l'overlay NVIDIA affiche le facteur choisi par notre mode adaptatif (par exemple X4) : c'est normal.

## Noms du proxy

| Nom | Quand l'utiliser |
|---|---|
| `version.dll` | Premier choix pour la plupart des jeux, Unreal Engine 4/5 compris. |
| `dinput8.dll` | Jeux chargeant DirectInput8. |
| `dxgi.dll` | Jeux chargeant DXGI tôt (ne pas écraser un `dxgi.dll` ReShade existant). |
| `winmm.dll` | Jeux chargeant WinMM (ne pas écraser le `winmm.dll` d'un autre mod). |
| n'importe quel `.asi` | Avec un chargeur ASI. |

Installer une seule copie et ne renommer que le proxy. Le jeu doit réellement charger ce nom.

## Linux (Proton) — non testé par nous

D'autres projets signalent que la génération d'images NVIDIA pour RTX 20/30 fonctionne sous Proton. Installer comme sous Windows, puis ajouter aux options de lancement Steam du jeu :

```text
WINEDLLOVERRIDES="version=n,b" PROTON_ENABLE_NVAPI=1 PROTON_NVIDIA_NVCUDA=1 %command%
```

Remplacer `version` par le nom du proxy utilisé (par exemple `dxgi`). Les retours sont bienvenus.

## Mise à jour

Remplacer `version.dll`, puis remplacer notre ancien compagnon par le nouveau panneau facultatif (ou le retirer). Mettre de côté un ancien `DLSSG-SM86-75-RUNTIME.dll` s'il existe. Ne jamais garder deux versions de nos add-ons actives ; les anciens `DLSSGControls.addon64`, `DLSSG.addon64`, `dlssg-035-companion.addon64` ou `renodx-rtx-unlocker.addon64` de ce projet peuvent être désactivés.

Réglages des versions release 11 :

| Ancien | Nouveau |
|---|---|
| `MaxInterpolatedFrames=N` | `[FrameGeneration] MaxGeneratedFrames=N` |
| `MaxMultiplier=M` | `MaxGeneratedFrames=M-1` |
| `ForceMultiplier` | `Multiplier` (ReShade.ini) |
| `DynamicMFG` / `DynamicTargetFPS` | `Dynamic` / `TargetFPS` (ReShade.ini) |
| `[DLSSG-035-COMPANION]` | `[DLSSG-SM86-75-COMPANION]` |

## Dépannage et désinstallation

- **Le panneau n'apparaît pas :** vérifier que l'add-on est à côté de l'exécutable et que ReShade prend en charge les add-ons. Le moteur fonctionne sans lui.
- **Le multiplicateur reste en attente :** activer Frame Generation dans le jeu ; un facteur non pris en charge par le plugin du jeu ne peut pas être forcé.
- **Signaler un problème :** indiquer GPU, pilote, jeu et API, joindre les deux INI et `DLSSG-SM86-75-runtime.log`. Retirer les chemins personnels avant partage.
- **Jeux Capcom (moteur RE) :** Onimusha: Way of the Sword fonctionne ici. D'autres projets signalent que certains jeux RE Engine plantent au démarrage sans REFramework (`dinput8.dll`) installé à côté du proxy, et que X3 et plus peuvent être instables : utiliser X2 dans ce cas. Ne pas nommer notre proxy `dinput8.dll` dans ce cas.
- **Cache :** un composant vérifié est stocké dans `%LOCALAPPDATA%\DLSSG-SM86-75\proxy`. Fermer les jeux avant de le supprimer.

Pour désinstaller, fermer le jeu et restaurer les sauvegardes. Retirer seulement notre proxy, le panneau et notre section d'INI ; si un runtime Vulkan a été remplacé, restaurer aussi sa sauvegarde.
