# DLSSG 310.9.1 pour SM86

[English](README.md) | [简体中文](README.zh-CN.md) | Français

Adaptation expérimentale de DLSS Frame Generation **310.9.1** pour les GPU
NVIDIA SM86, basée sur le travail de
[sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
Installation avec un seul fichier : **`version.dll`**.


## Choisir une version

Toutes les versions utilisent DLSSG 310.9.1 et s'installent avec un seul `version.dll`.
**Essayez les variantes dans la même scène et gardez celle qui vous convient le mieux.**
Un numéro plus élevé ne garantit ni plus de FPS ni un meilleur ressenti.

| Version / téléchargement | Différence principale | À quoi s'attendre |
|---|---|---|
| [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0) | Base avec interpolation bilinéaire manuelle. | Référence pour comparer la reconstruction d'image. |
| [310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1) | Filtrage bilinéaire matériel pour la reconstruction finale. | De petits écarts de pixels sont possibles ; une amélioration marginale a été rapportée. |
| [310.9.1-2](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-2) | Tout le contenu de la `-1`, plus la réutilisation des entrées FP16 d'une convolution. | Essayée en jeu par un utilisateur ; aucun problème visuel évident, gain difficile à juger. |
| [310.9.1-3](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-3) | Tout le contenu de la `-2`, plus la réutilisation des entrées FP16 d'une seconde convolution de reconstruction. | Images identiques à la `-2` dans les tests hors jeu ; aucun gain constant sur le temps GPU total établi. |
| [310.9.1-4](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-4) | Tout le contenu de la `-3`, plus des lectures vectorisées dans deux convolutions résiduelles. | Images identiques à la `-2` dans les tests hors jeu ; variations du temps GPU total faibles et irrégulières. |
| [310.9.1-5](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-5) | Les kernels de la `-4`, avec un INI facultatif pour activer ou désactiver quatre optimisations. | Même traitement d'image par défaut que la `-4` ; permet de comparer les combinaisons des versions précédentes. |

Le bilinéaire adapte l'idée de l'option [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) du projet original.
Il peut modifier légèrement les pixels par rapport à la `-0`.
Les optimisations suivantes de lecture mémoire conservent les calculs FP16.
**Ces releases ne contiennent ni FP8 ni INT8.**

Les retours en jeu concernent pour l'instant les versions `-0` à `-2`, sur un
**portable RTX 3070 Ti mobile avec 8 Go de VRAM**. Les nouvelles révisions passent
les vérifications hors jeu d'images, de chargement et de gestion des ressources,
mais **n'ont pas encore été essayées en jeu**. Un kernel plus rapide isolément
ne garantit pas un gain global mesurable. Gardez votre version fonctionnelle
en secours ; les retours d'autres configurations sont les bienvenus.

Fermez le jeu avant de changer de DLL ou de réglages. Comparez la qualité d'image,
la réactivité et la fluidité, ainsi que les FPS, à réglages identiques.

### Configuration facultative (`-5`)

Copiez `dlssg_sm86.ini` à côté de `version.dll`, choisissez `1` (actif) ou `0`
(inactif), puis redémarrez complètement le jeu. Sans fichier, ou si une clé
manque, l'optimisation correspondante est active par défaut. Ce sont les réglages
de ce pont ; l'INI de l'hôte natif du projet original n'est pas lu.

```ini
[Optimizations]
HardwareBilinear=1
Conv13SharedInput=1
Conv0SharedInput=1
ResidualVectorLoads=1
```

Combinaisons à comparer (même traitement d'image, pas le même fichier DLL) :

| Profil | HardwareBilinear | Conv13SharedInput | Conv0SharedInput | ResidualVectorLoads |
|---|---:|---:|---:|---:|
| `-0` | 0 | 0 | 0 | 0 |
| `-1` | 1 | 0 | 0 | 0 |
| `-2` | 1 | 1 | 0 | 0 |
| `-3` | 1 | 1 | 1 | 0 |
| `-4` | 1 | 1 | 1 | 1 |

Les 16 combinaisons et le fonctionnement sans fichier ont été vérifiés hors jeu. Cela ne garantit pas la compatibilité avec tous les jeux.

## Compatibilité

- Windows x64, jeu Direct3D 12 et pilote NVIDIA fournissant NGX/NVAPI.
- GPU SM86 (famille GeForce RTX 30). Essais réalisés sur un portable avec RTX 3070 Ti mobile
  (**8 Go de VRAM**), pilote 616.92 ; ce numéro n'est pas une exigence minimale de pilote.
- Le jeu doit intégrer DLSS Frame Generation et charger le proxy `version.dll`.
- Modes X2, X3 et X4, selon les choix proposés par le jeu.
- Python et CUDA Toolkit ne sont pas nécessaires pour jouer.

Cette release ne fournit pas de route SM75/RTX 20, de prise en charge Vulkan,
ni de DLL proxy sous d'autres noms.

## Installation et mise à jour

### Pour débuter : RHI et les outils de ShortFuse

**Pour les néophytes, nous recommandons [RHI — ReShade HDR Installer](https://github.com/RankFTW/RHI)**
pour installer et gérer les outils complémentaires. RHI propose notamment
ShortFuse DLSS Tool et NR Cost Scaler dans son interface de gestion du DLSS.
Suivre les instructions de RHI pour son jeu, puis installer le `version.dll`
de cette release selon les étapes ci-dessous.

Selon le retour de notre testeur sur les versions précédentes, la compatibilité est très bonne avec
**[DLSS Tool de ShortFuse](https://discord.com/channels/1408098019194310818/1543975158937821315)**
et son **[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884)**,
également installable via [RHI](https://github.com/RankFTW/RHI).
Ces liens Discord peuvent nécessiter de rejoindre le serveur.

Le support RTX20/30/40 indiqué dans le nom du patch NR concerne cet outil
complémentaire ; ce pont de génération d'images reste destiné à SM86/RTX 30.
Il s'agit d'un retour de compatibilité sur la configuration testée.

**Pour soutenir leurs auteurs, pensez à mettre une étoile ⭐ aux dépôts
[RHI](https://github.com/RankFTW/RHI) et [RenoDX de ShortFuse](https://github.com/clshortfuse/renodx) !**

### Installer le pont de génération d'images

1. Fermer complètement le jeu.
2. Sauvegarder un éventuel `version.dll` déjà présent. Si un autre mod utilise
   ce nom, ne pas l'écraser : cette release ne gère pas le chaînage de proxies.
3. Copier le `version.dll` de la release près de l'exécutable qui effectue le
   rendu. Pour Black Myth: Wukong : `b1/Binaries/Win64`, près de
   `b1-Win64-Shipping.exe`.
4. Relancer le jeu et activer DLSS Frame Generation. Commencer par X2, puis
   comparer X3/X4 dans une même scène en mouvement.

L'INI est facultatif dans la `-5` ; voir la configuration plus haut.
L'INI de l'hôte natif du projet original n'est pas lu. Ne pas renommer cette
DLL en `nvngx_dlssg.dll` ni remplacer les DLL NVIDIA originales du jeu.

Lors d'une mise à jour depuis le premier paquet 310.9.1 à deux éléments,
sauvegarder l'ancien `version.dll` et le dossier `dlssg3109` hors du jeu.
Le nouveau fichier unique suffit.

## Fonctionnement

Le proxy embarque le runtime NVIDIA 310.9.1 inchangé et les kernels adaptés
à SM86. Au premier chargement, le runtime est extrait automatiquement dans
`%LOCALAPPDATA%/DLSSG-SM86/<SHA256>/nvngx_dlssg.dll` et vérifié avant utilisation.
Les kernels sont lus directement depuis la DLL. Un cache corrompu est refusé.
Le journal de diagnostic est `dlssg3109.log`, près du proxy.

Cette architecture diffère du host natif 310.1 du projet amont. Les réglages,
mesures de performance et routes GPU de ce dernier ne décrivent pas cette
release. Aucun réglage global du pilote ou indicateur DLSS n'est activé
automatiquement par l'installation.

## Retours en jeu et limites

Les retours ci-dessous proviennent d’un seul **ordinateur portable avec une
RTX 3070 Ti mobile et 8 Go de VRAM**. Ils ne représentent pas des essais sur GPU de bureau.

| Jeu | Retour utilisateur |
|---|---|
| Black Myth: Wukong | X2 agréable, X3 acceptable ; X4 fonctionne mais mauvais ressenti de fluidité. |
| Palworld | Bon fonctionnement, y compris X4 ; dégradation visuelle sensible en X4. |

Ces retours ne constituent pas un benchmark contrôlé ou une garantie sur
toutes les configurations. Un compteur de FPS plus élevé ne garantit pas
une meilleure réactivité. Comparer aussi les artefacts et la régularité en
mouvement ; la cause précise des défauts observés en X4 n'est pas établie.

**Les retours d’autres configurations sont les bienvenus !** Préciser le GPU,
la VRAM, le modèle de portable ou de PC fixe, le pilote, la version du jeu,
la résolution de sortie et le mode X2/X3/X4. Avec Neural Rendering, indiquer aussi
la version NR et le réglage NR Cost Scaler. Décrire la qualité d’image et la
réactivité en plus des FPS, idéalement dans une même scène.
Partager ces essais dans les [Issues GitHub](https://github.com/SilyNoMeta/dlssg_for_sm86/issues).

[Voir les captures de Palworld et la configuration RHI](GALLERY.fr.md) : NR
activé/désactivé et résolution de traitement NR pleine/réduite. Toutes les captures
de jeu fournies affichent X2 ; la valeur exacte du Cost Scaler n’est pas confirmée.

## Dépannage et désinstallation

Si les options restent absentes, vérifier le dossier de l'exécutable et la
présence de `dlssg3109.log`. Fermer le jeu avant toute modification. Si le
journal signale un cache corrompu, déplacer le sous-dossier concerné de
`%LOCALAPPDATA%/DLSSG-SM86` pour permettre sa recréation au prochain lancement.

Pour désinstaller, retirer uniquement le `version.dll` de cette release,
puis remettre le fichier sauvegardé s'il y en avait un. Le journal et le cache
DLSSG-SM86 peuvent être retirés quand les jeux qui l'utilisent sont fermés.

Pour signaler un problème, préciser le jeu, le GPU, le pilote et le mode testé.
Vérifier les chemins personnels avant de partager un journal.

## Version et crédits

La version `310.9.1-5` utilise le runtime 310.9.1. L’empreinte de la DLL figure
dans `SHA256SUMS.txt`.

Merci à [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) pour le projet
original et le travail SM86. Voir [les attributions tierces](THIRD_PARTY_NOTICES.txt).
