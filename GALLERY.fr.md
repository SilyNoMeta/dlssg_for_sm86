# Palworld : DLSSG, Neural Rendering et RHI

[English](GALLERY.en.md) | [简体中文](GALLERY.zh-CN.md) | Français · [Installation](README.fr.md)

Captures fournies par l’utilisateur sur un **portable RTX 3070 Ti mobile avec
8 Go de VRAM**. Le bandeau du jeu affiche **DLSSG 310.9.1, D3D12, X2**.
L’indicateur NR visible identifie **DLSSNR 310.8.0**. La génération d’images et
Neural Rendering sont deux composants distincts, avec leurs propres versions.

Ces images illustrent leur coexistence et des différences visuelles ; ce n’est
pas un benchmark contrôlé. La caméra, les animations et les effets varient.
Elles ne permettent pas d’évaluer la fluidité en mouvement ou les FPS.
Le `224Hz` du bandeau DLSSG n’est pas une mesure de FPS.

## NR activé, pleine résolution de traitement

L’indicateur NR affiche `ON | 2560x1440`. C’est l’exemple fourni le plus lisible
du traitement NR à pleine résolution ; la capture ne montre pas l’interrupteur du Cost Scaler.

![Palworld avec DLSSG 310.9.1 X2 et DLSSNR 310.8.0 ON en 2560x1440](screenshots/palworld-nr-full.png)

## NR activé, résolution de traitement réduite

L’indicateur NR affiche `ON | 1484x834`, ce qui montre une résolution de traitement
NR réduite. L’utilisateur se souvient d’un essai du NR Cost Scaler autour de
`0,50`, mais le réglage exact n’est pas visible : la légende ne certifie donc pas cette valeur.

![Palworld avec DLSSG X2 et NR ON en 1484x834](screenshots/palworld-nr-reduced.png)

## NR désactivé dans la comparaison utilisateur

L’indicateur NR est absent tandis que DLSSG 310.9.1 X2 reste visible.
L’utilisateur identifie cet essai comme la comparaison sans NR. La caméra
est proche des vues précédentes, mais pas parfaitement identique.

![Comparaison Palworld sans indicateur NR, avec DLSSG X2 toujours visible](screenshots/palworld-nr-off.png)

## Configuration RHI pour Palworld

Le panneau affiche **DLSS Tool (ShortFuse)** sélectionné et **NR Cost Scaler**
marqué comme installé. Aucune valeur numérique du Cost Scaler n’apparaît.
Ce sont les réglages du gestionnaire ; les versions actives citées plus haut
proviennent du bandeau en jeu. En particulier, le NR `0.0.0` affiché par RHI
ne doit pas être interprété comme la version NR utilisée en jeu.

![Configuration RHI de Palworld avec DLSS Tool ShortFuse et NR Cost Scaler installé](screenshots/rhi-palworld.jpg)

Pour l’installation, commencer avec [RHI](https://github.com/RankFTW/RHI).
Soutenez ses auteurs et [RenoDX de ShortFuse](https://github.com/clshortfuse/renodx)
avec une étoile GitHub ⭐.
