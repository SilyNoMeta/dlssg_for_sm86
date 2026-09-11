# DLSSG 310.9.1 pour SM86

[English](README.md) | [简体中文](README.zh-CN.md) | Français

Adaptation expérimentale de DLSS Frame Generation **310.9.1** pour NVIDIA SM86/RTX 30,
basée sur [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86). Une DLL autonome contient
**DirectX 12 + Vulkan**, la correction temporelle MFG et quatre optimisations facultatives.

## Télécharger 310.9.1-8

**[Télécharger la DLL universelle + l'INI facultatif](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-8/dlssg-sm86-310.9.1-8-win64.zip)** · [Notes de version](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8)

Un paquet, une seule **`version.dll`**. Choisir son nom selon l'installation :

| Nom du fichier | Installation |
|---|---|
| `version.dll` | Proxy de version direct, nom fourni par défaut. |
| `dxgi.dll` | Renommer le même fichier ; proxy DXGI direct, sans loader ASI. |
| `dxgi.asi` | Renommer le même fichier ; chargement par Ultimate ASI Loader x64. |

**Installer une seule copie de notre bridge.** Le ZIP contient aussi l'INI facultatif,
la documentation, les empreintes et les licences. La -8 ajoute les exports DXGI
et le démarrage ASI aux runtime et kernels corrigés de la -7, avec les quatre options INI.

**Les anciennes -0 à -6 ont été retirées : leurs
images X3/X4 pouvaient rester près du milieu du mouvement malgré un compteur FPS élevé.**
Sur un déplacement de 8 pixels, les anciennes sorties X4 se plaçaient vers 4/4/4 pixels,
contre 2/4/6 après correction. Le X4 dans Wukong est désormais décrit comme nettement
plus fluide sur **RTX 3070 Ti Laptop, 8 Go**, pilote 616.92. Il s'agit d'une correction ;
aucun gain de FPS n'est promis. Le rectangle blanc du graphique de benchmark Wukong
reste un problème connu.

La correction reste toujours active, même si toutes les optimisations INI sont désactivées.
Voir les [mécanismes, architecture et validations techniques](docs/research.fr.md).

## Installation

1. Fermer le jeu et sauvegarder les anciens `version.dll` et `dlssg_sm86.ini`.
2. Copier `version.dll` près du véritable exécutable de rendu : Wukong
   `b1/Binaries/Win64`.
3. Y copier éventuellement `dlssg_sm86.ini`, puis relancer et comparer X2/X3/X4.

Si un autre mod utilise `version.dll`, choisir le mode DXGI ou ASI et suivre
le [guide générique](docs/install-loaders.fr.md). Avec Ultimate ASI Loader,
le loader est `version.dll` et notre DLL devient `dxgi.asi`.
Conserver le nom `dlssg_sm86.ini`. Ces renommages nécessitent la -8 ;
le binaire -7 original doit garder son nom `version.dll`. Ne jamais renommer
le bridge en `nvngx_dlssg.dll`.
Pour revenir en arrière, fermer le jeu et restaurer les fichiers sauvegardés.

Windows x64, un GPU SM86 et une intégration DLSS FG existante sont nécessaires.
En Vulkan, le jeu doit fournir les extensions NGX et la présentation des images.
La DLL n'ajoute pas le FG à un jeu quelconque. DX11, Linux/Proton, DXVK et RTX 20
ne sont pas validés. Aucun Python/CUDA à installer
pour jouer. Le pilote testé 616.92 ne constitue pas une version minimale requise.

## Optimisations facultatives

```ini
[Optimizations]
HardwareBilinear=1
Conv13SharedInput=1
Conv0SharedInput=1
ResidualVectorLoads=1
```

| Option | Effet |
|---|---|
| `HardwareBilinear` | Filtrage matériel à la reconstruction finale ; petits écarts de pixels possibles. Lié à [HardwareBilinear de l'original](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md). |
| `Conv13SharedInput` | Réutilisation des entrées FP16 d'une convolution en mémoire partagée. |
| `Conv0SharedInput` | Même principe pour une seconde convolution de reconstruction. |
| `ResidualVectorLoads` | Lectures vectorisées des entrées de deux convolutions résiduelles. |

`1` active et `0` désactive. Fichier ou clé manquants : `1` par défaut.
Relancer le jeu après modification. Les options s'appliquent aux deux API ; elles
ne choisissent pas X2/X3/X4 et ne règlent pas Neural Rendering / NR Cost Scaler.
Le bridge lit sa section `[Optimizations]`, pas les réglages du fournisseur natif
original. Tout à zéro sélectionne les noyaux de référence corrigés, sans rétablir
une ancienne DLL. Aucun FP8, INT8 ou abaissement de qualité neuronale n'est inclus.

## Outils complémentaires et retours

**Débutants : passez par [RHI](https://github.com/RankFTW/RHI) pour gérer les outils complémentaires**, selon
ses instructions, puis installez cette DLL FG. Notre testeur sur portable rapporte
une très bonne compatibilité avec [DLSS Tool de ShortFuse](https://discord.com/channels/1408098019194310818/1543975158937821315) et
[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884), également installables via RHI.
Les liens Discord peuvent nécessiter de rejoindre le serveur. Les GPU cités
par le patch NR n'étendent pas la compatibilité SM86 de ce bridge FG.
Pensez à star **[RHI](https://github.com/RankFTW/RHI)** et **[RenoDX de ShortFuse](https://github.com/clshortfuse/renodx)** pour soutenir leurs auteurs.

| Jeu | État des vérifications |
|---|---|
| Black Myth: Wukong / DX12 | X4 corrigé nettement plus fluide ; chargement direct en `dxgi.dll` également confirmé sur le portable. Graphique toujours blanc. |
| Palworld | Retours positifs sur les anciennes versions ; nouvel essai de la DLL corrigée attendu. |

Les essais portent surtout sur un **portable**, pas sur un GPU de bureau.
Les retours d'autres configurations sont bienvenus : GPU/VRAM, pilote, jeu/API,
résolution, mode, réglages NR/Cost Scaler, qualité du mouvement et réactivité.
Utiliser les [Issues](https://github.com/SilyNoMeta/dlssg_for_sm86/issues).

## Diagnostic et crédits

La DLL contient le runtime NVIDIA 310.9.1 inchangé et les noyaux SM86. Le runtime
est vérifié et mis en cache sous `%LOCALAPPDATA%/DLSSG-SM86/<SHA256>/` ; les noyaux
restent embarqués. Le journal est `dlssg3109.log`, près du proxy. Les événements
Vulkan prouvent l'exécution, pas les FPS affichés. Un cache corrompu est refusé :
jeu fermé, déplacer son sous-dossier permet sa recréation.

Merci à [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) et au
[correctif temporel RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp) de Michael Robles (MIT).
Voir les [mentions tierces](THIRD_PARTY_NOTICES.txt) et `SHA256SUMS.txt`.
