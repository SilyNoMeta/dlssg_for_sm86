# DLSSG 310.9.1 pour SM86

[English](README.md) | [简体中文](README.zh-CN.md) | Français

Adaptation expérimentale de DLSS Frame Generation **310.9.1** pour les GPU
NVIDIA SM86, basée sur le travail de
[sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
Installation avec un seul fichier : **`version.dll`**.

[Télécharger la release 310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1)

## Nouveautés de 310.9.1-1

Cette révision active le **filtrage bilinéaire matériel** dans l'étape finale de
reconstruction de l'image. Des lectures de texture filtrées par le matériel
remplacent l'interpolation bilinéaire manuelle pour réduire le travail effectué.
Cet échantillonnage est approximatif : les pixels générés peuvent légèrement
différer de ceux de 310.9.1-0.

Le principe rejoint l'option
[`HardwareBilinear` du projet original](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md),
avec une implémentation adaptée à notre pont 310.9.1. Ici, il est **toujours actif**,
sans réglage INI. Revenir à [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)
permet de retrouver l'échantillonnage précédent.

Notre testeur rapporte une **petite amélioration ressentie** sur son portable
RTX 3070 Ti mobile, 8 Go. Aucun gain global reproductible n'est établi ; le
résultat dépend du jeu et de la scène. Les retours d'autres configurations sont
bienvenus. X2/X3/X4 passent les contrôles hors jeu. De faibles écarts sur des
images synthétiques ne garantissent pas une qualité identique dans tous les
jeux, notamment en mouvement ou en HDR.

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

Selon le retour de notre testeur, cette version fonctionne très bien avec
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

Il n'y a pas de fichier INI requis. Les options du host natif amont, dont
`HardwareBilinear`, ne sont pas lues par cette variante. Ne pas renommer cette
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

La version `310.9.1-1` utilise le runtime 310.9.1. L’empreinte de la DLL figure
dans `SHA256SUMS.txt`.

Merci à [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) pour le projet
original et le travail SM86. Voir [les attributions tierces](THIRD_PARTY_NOTICES.txt).
