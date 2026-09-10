# DLSSG 310.9.1 pour SM86

Français | [English](README.en.md)

Adaptation expérimentale de DLSS Frame Generation **310.9.1** pour les GPU
NVIDIA SM86, basée sur le travail de
[sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86).
Installation avec un seul fichier : **`version.dll`**.

[Télécharger la release 310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)

## Compatibilité

- Windows x64, jeu Direct3D 12 et pilote NVIDIA fournissant NGX/NVAPI.
- GPU SM86 (famille GeForce RTX 30). Essais réalisés sur RTX 3070 Ti Laptop,
  pilote 616.92 ; ce numéro n'est pas une exigence minimale de pilote.
- Le jeu doit intégrer DLSS Frame Generation et charger le proxy `version.dll`.
- Modes X2, X3 et X4, selon les choix proposés par le jeu.
- Python et CUDA Toolkit ne sont pas nécessaires pour jouer.

Cette release ne fournit pas de route SM75/RTX 20, de prise en charge Vulkan,
ni de DLL proxy sous d'autres noms.

## Installation et mise à jour

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

| Jeu | Retour utilisateur |
|---|---|
| Black Myth: Wukong | X2 agréable, X3 acceptable ; X4 fonctionne mais mauvais ressenti de fluidité. |
| Palworld | Bon fonctionnement, y compris X4 ; dégradation visuelle sensible en X4. |

Ces retours ne constituent pas un benchmark contrôlé ou une garantie sur
toutes les configurations. Un compteur de FPS plus élevé ne garantit pas
une meilleure réactivité. Comparer aussi les artefacts et la régularité en
mouvement ; la cause précise des défauts observés en X4 n'est pas établie.

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

`310.9.1-0` désigne le runtime 310.9.1 et la première révision distribuée de ce
pont. Les propriétés Windows du fichier indiquent `0.1.0` : il s'agit du même
binaire, conservé sans recompilation. Son empreinte figure dans `SHA256SUMS.txt`.

Merci à [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) pour le projet
original et le travail SM86. Voir [les attributions tierces](THIRD_PARTY_NOTICES.txt).
