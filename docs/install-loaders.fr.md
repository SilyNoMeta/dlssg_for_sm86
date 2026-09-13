# Installation DLL / ASI — 310.9.1-11

Télécharger **dlssg-310.9.1-11-win64.zip** depuis la [release](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11). Pour le panneau facultatif, utiliser le [panneau ReShade inclus](reshade-controls.fr.md).

Fermer le jeu et sauvegarder les fichiers à remplacer. Copier **un seul** moteur et `dlssg_sm86.ini` près du véritable exécutable (Wukong : `b1/Binaries/Win64`). Activer DLSS FG dans le jeu.

| Méthode | Installation |
|---|---|
| Proxy version direct | Installer notre `version.dll` sans le renommer. Le jeu doit charger ce nom. |
| Proxy DXGI direct | Renommer le même fichier en `dxgi.dll`, sans loader ASI. |
| Ultimate ASI Loader | Installer [UAL x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader) en `version.dll`, puis renommer notre fichier en `dxgi.asi`. |

C'est le même moteur sous ces noms. Garder l'INI nommé `dlssg_sm86.ini`, à côté. Ne jamais renommer notre bridge en `nvngx_dlssg.dll`. Préserver les proxies ReShade et des autres mods en choisissant une méthode libre. Notre proxy DXGI relaie vers Windows, pas automatiquement vers un autre mod DXGI.

UAL peut charger d'autres noms ASI via `InitializeASI` ; `dlssg_sm86.asi` a été vérifié dans le test de chargement. Avec un loader qui n'appelle pas cet export, utiliser `dxgi.asi`. Dans un sous-dossier ASI, garder l'INI près du plugin. REFramework peut conserver son `dinput8.dll`.

Le panneau facultatif `DLSSGControls.addon64` fonctionne avec cette DLL/ASI. Retirer l’ancien moteur autonome `DLSSG.addon64` avant la migration. Conserver ReShade et les add-ons NR indépendants, avec un seul moteur de compatibilité MFG.

**Passage de FSR FG à DLSS FG ?** Si le choix change mais que la génération reste inactive, enregistrez DLSS FG comme mode sélectionné, fermez complètement le jeu puis relancez-le avant de tester. Un redémarrage a rétabli le fonctionnement lors d’un essai ; le changement de fournisseur sans redémarrage n’est pas garanti.

## Configuration et vérification

Par défaut, le jeu choisit le mode, avec `MaxInterpolatedFrames=5` (plafond X6 si le plugin le permet). Voir [commandes, migration, journaux et télémétrie](live-controls.fr.md). L'édition manuelle de l'INI demande un redémarrage ; utilisez le panneau ReShade pour les raccourcis en direct. Ceux de la DLL seule ont échoué dans Wukong et ne sont pas une alternative validée. Le dynamique natif nécessite DX12 compatible ; les commandes fixes peuvent utiliser les chemins DX12/Vulkan reconnus.

Avec le journal actif, `proxy_attached`, `dxgi_attached` ou `asi_attached` identifient le chargement ; `installed_310_9_1` identifie le traitement du runtime. `sl_native_dynamic_accepted` signifie acceptation SDK, pas preuve du respect de la cible par le pilote. L'override NVIDIA de cible dynamique, global ou par jeu, peut être prioritaire. Le filigrane NVIDIA peut afficher `Dyn DRV` et facteur actuel/maximal ; le paquet ne l'active pas automatiquement.

Un chargement réussi ne prouve pas la présentation des images générées. Pour revenir en arrière, fermer le jeu, retirer seulement notre moteur installé et restaurer les sauvegardes. Aucun toolkit CUDA ni outil de compilation n'est nécessaire pour jouer.
