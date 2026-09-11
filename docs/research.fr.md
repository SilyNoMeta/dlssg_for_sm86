# Justesse temporelle et optimisations incluses

11 septembre 2026 · release 310.9.1-9 · [English](research.en.md) / [Français](research.fr.md) / [简体中文](research.zh-CN.md)

## Nouveautés -9 : facteurs élevés et Dynamic MFG natif

Le plafond du fournisseur est configurable jusqu'à cinq images générées, soit X6
au total. La même correction temporelle place l'image i à t=i/(n+1), y compris
en X5/X6. Ce plafond n'agrandit pas les tableaux d'un ancien plugin Streamline :
le forçage reste limité par la version reconnue et les capacités annoncées.

Le Dynamic MFG natif utilise les options eDynamic et la cible de Streamline.
Il n'ajoute pas de boucle indépendante de régulation de la présentation. Son
activation exige une ABI connue, notre fournisseur, DX12 et une capacité dynamique
positive. FG désactivé reste désactivé. Une demande refusée ou indisponible peut
revenir au facteur fixe configuré si celui-ci est pris en charge. Le choix dynamique
natif déjà effectué par le jeu est conservé.

### Pourquoi une capacité annoncée ne suffisait pas

Une intégration peut appeler GetState sur la vue 0 et SetOptions sur la vue 1.
Notre première implémentation conservait les capacités système dans chaque vue :
la seconde pouvait attendre une capacité déjà signalée par la première.
La correction partage ces capacités, tout en gardant compteurs de présentation,
fences et état d'activation propres à chaque vue. Le cache est effacé lors d'un
changement de fournisseur/périphérique/API et d'un arrêt réussi. Une nouvelle
réponse négative remplace une capacité positive. Les copies versionnées préservent
les anciennes structures du jeu ; aucun appel GetState supplémentaire ne consomme
ses compteurs de présentation.

### Preuves pour ce binaire

- 213 assertions de contrôle/ABI, avec protection des anciens buffers Options/State.
- 16 cas GPU fixes DX12/Vulkan, incluant X5/X6 et optimisations activées/désactivées.
- 10 scénarios Streamline réels, dont l'échec attendu de la première implémentation
  et le partage des capacités réussi dans la version corrigée.
- Quatre séquences Vulkan X2–X6 avec une seule création explicite de feature chacune ;
  erreur de placement inférieure à 0,403 px sur la mire synthétique.
- Retour fonctionnel en jeu sur RTX 3070 Ti Laptop 8 Go, pilote 616.92 : transitions
  automatiques X3/X4/X5, filigrane dynamique et demande acceptée à 130 FPS.

Ce retour ne fournit pas de nouveau benchmark FPS/latence ni de test de longue durée.
Les transitions Vulkan vérifient le contenu des images, pas la présentation par la
swapchain ni le coût des allocations internes. Streamline 2.14.1 annonce l'absence
de capacité dynamique native sous Vulkan, conformément au [guide NVIDIA](https://github.com/NVIDIA-RTX/Streamline/blob/v2.14.1/docs/ProgrammingGuideDLSS_G.md#63-enabling-dynamic-multi-frame-generation).
Aucun contrôleur adaptatif Vulkan distinct n'est inclus.

Le contrôle s'appuie sur l'étude de [MFGAdaUnlock-RenoDx de mavismmg / ImDreamt](https://github.com/mavismmg/MFGAdaUnlock-RenoDx),
commit 7e613b2aadffe936f2ea19df9c71931bbbbae2e6. Son attribution MIT et la mention
des headers Streamline accompagnent la distribution.

Les sections suivantes conservent l'historique et la portée des tests temporels et
de chargement précédents ; elles ne constituent pas de nouvelles mesures de tous
les cas de la -9.

## Observation et hypothèse

L'[issue #2](https://github.com/SilyNoMeta/dlssg_for_sm86/issues/2) décrit 160–170 FPS en X4 mais une mauvaise fluidité
sur RTX 3060 Ti 8 Go. Le mainteneur retrouve ce ressenti
dans Wukong. Hypothèse : le contenu des images intermédiaires progresse mal,
alors que leur génération et leur présentation réussissent.

Une scène 640×360 avance de 8 pixels par image réelle, avec vecteurs de mouvement
connus et profondeur constante. Une rampe rouge permet une mesure analytique du
déplacement, indépendante d'une DLL de référence. La première image réinitialise
l'historique ; les trois groupes suivants sont mesurés hors des bords et de l'interface.

| Fournisseur X4 | Générée 1 | Générée 2 | Générée 3 |
|---|---:|---:|---:|
| Attendu | 2 px | 4 px | 6 px |
| Original natif 310.1, HardwareBilinear=1 | ~2 px | ~4 px | ~6 px |
| Ancienne base 310.9.1 | ~4 px | ~4 px | ~4 px |
| 310.9.1-7 corrigée | ~2 px | ~4 px | ~6 px |

Les anciennes sorties n'étaient pas des copies binaires exactes : leurs empreintes
différaient, mais le mouvement restait au milieu. Les anciens tests comparaient
à une référence employant le même déverrouillage MFG, donc susceptible du même
défaut. Des empreintes cohérentes et davantage de FPS ne prouvent pas la justesse temporelle.

## Mécanisme et correction

Le PTX SM89 utilisé par ce port SM86 contient 104 multiplications de vecteurs par
0,5 dans `Kernel_EstimateIntermMvecsScatter` (k46). Déverrouiller le nombre d'images
côté hôte ne suffit pas à appliquer leur temps respectif. Pour l'indice i et n
images générées, t=i/(n+1) : les 52 premiers facteurs deviennent 1−t, les 52 suivants t.
Les décalages de demi-texel restent inchangés. La transformation adapte le
[correctif RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp) de Michael Robles (MIT), avec vérification
de l'identité exacte du code source.

Un identifiant de noyau change dans chacun des packs de 148 identifiants. La
correction figure dans le pack de référence et le pack optimisé ; l'INI ne peut
pas la désactiver. En X2, t=0,5 : toutes optimisations désactivées, les sorties
restent identiques octet par octet à l'ancienne base. Le modèle, ses poids et la
précision FP16 ne sont pas réduits.

## Validation et limites

Correctif temporel -7 vérifié sur 52 cas hors jeu, RTX 3070 Ti Laptop 8 Go, pilote 616.92 : 49 succès attendus
et 3 échecs attendus détectant les défauts X3/X4 de l'ancienne base, dont avec interface.
Couverture : 16 combinaisons INI en X4 sur DX12/Vulkan ; X2/X3 avec toutes les
options actives ou désactivées sur les deux API ; 1280×720 ; mouvement vers la
gauche ; HUDLess/UIAlpha. Les sorties corrigées comparables DX12/Vulkan sont
identiques. Tolérance de déplacement : 0,5 pixel, car la quantification RGBA8
introduit environ 0,34 pixel d'écart pour les tiers X3, même avec l'original.
L'ancien défaut atteint environ 1,33 pixel en X3 et 2 pixels en X4.
Ressources embarquées, cache froid/concurrent/chaud et refus de cache corrompu
ont aussi été vérifiés. [Périmètre structuré](validation-summary.json).

Ces tests ne mesurent pas la présentation en jeu et ne couvrent pas toutes les
occlusions, caméras, interfaces ou intégrations. Le propriétaire a ensuite confirmé
une forte amélioration de fluidité X4 dans Wukong avec ce binaire -7.
Un nouvel essai Vulkan en jeu reste à confirmer pour cette release.
Le graphique Wukong présente toujours un rectangle blanc. Le test d'interface
synthétique ne le reproduit pas ; ce symptôme n'est donc pas annoncé comme corrigé.

## Optimisations présentes dans la DLL

| Option INI | Mécanisme | Résultat et limite |
|---|---|---|
| HardwareBilinear | Filtrage matériel en reconstruction finale k60, lié à [l'option originale](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md). | Petits écarts de pixels possibles. Amélioration antérieure ressentie comme marginale ; aucun gain global garanti. |
| Conv13SharedInput | Réutilisation des entrées FP16 de k13 en mémoire partagée. | Arithmétique conservée dans les cas testés ; aucun gain en jeu attribué isolément. |
| Conv0SharedInput | Halo d'entrée partagé pour k0 ; ordre des opérations Tensor Core conservé. | Mesure isolée synchronisée : 0,792384→0,698168 ms (−11,89 %). Blocs complets 1440p X4 presque neutres. |
| ResidualVectorLoads | Lectures coopératives vectorisées de k5/k11 ; calcul et barrières conservés. | Mesures isolées : −2,84 % / −6,20 % ; variations globales faibles et non constantes. |

Ces mesures isolées précèdent la correction temporelle. Elles concernent des
noyaux et charges précis, pas des gains de FPS établis pour -7. Les anciennes
comparaisons de sorties restent utiles pour vérifier l'arithmétique d'une
optimisation, mais ne validaient pas le mouvement MFG. Aucun FP8, INT8, LZ4 ou
modèle neuronal réduit n'est inclus. Comparer les options sur le même chemin
corrigé et relancer le jeu entre les modifications.

## Chargement : une DLL présente n'est pas un bridge actif

Dans le binaire -7 original, seul `version.dll` déclenche le démarrage. Un loader ASI peut
charger une DLL renommée sans activer son bridge. Ce problème est distinct du
mauvais placement temporel des images X3/X4.

La release -8 ajoute un démarrage commun et idempotent pour trois
modes : `version.dll` transmet les fonctions d'information de version ;
`dxgi.asi` démarre au chargement et expose `InitializeASI` ; `dxgi.dll` transmet
les véritables exports DXGI de Windows. Ultimate ASI Loader appelle aussi
`InitializeASI` pour les autres noms `.asi` : l'activation ne dépend alors plus
du cas particulier `dxgi.asi`.

Avec UAL, `version.dll` désigne le loader et `dxgi.asi` notre bridge : deux
binaires distincts. Installer une seule copie du bridge. Sa configuration reste
`dlssg_sm86.ini`, à côté du bridge, quel que soit le nom choisi.

Le proxy DXGI charge la bibliothèque réelle par le chemin absolu de son dossier
système, pour éviter de se charger lui-même. La transmission préserve les arguments
entiers, flottants et sur la pile, puis restitue les objets COM Windows sans les
remplacer. DXGI est chargé au premier appel d'export, hors de notre `DllMain` ;
Microsoft précise que [créer une factory depuis DllMain échoue](https://learn.microsoft.com/en-us/windows/win32/api/dxgi/nf-dxgi-createdxgifactory).
La publication atomique du module gère les premiers appels concurrents sans
accumuler de références supplémentaires. Les noms et ordinaux des exports sont
comparés à la bibliothèque Windows testée ; la création réelle des factories
est vérifiée séparément.

**Le paquet -8 contient une seule `version.dll`, renommable pour ces modes.**
Les 20 exports DXGI, trois API de factory, premiers appels concurrents, imports
statiques, exports de version et démarrage par le véritable UAL passent leurs contrôles.
Sur quatre cas X4 (DX12 sous trois noms et Vulkan sous `dxgi.dll`), les 12 images
de chaque cas correspondent octet pour octet à la -7 standard. L'utilisateur a
ensuite confirmé le fonctionnement direct en `dxgi.dll` dans Wukong sur RTX 3070 Ti
Laptop 8 Go. Il s'agit d'une validation fonctionnelle, pas d'un nouveau benchmark
FPS ou d'une validation de tous les jeux.
Un événement de démarrage ne prouve pas à lui seul la présentation d'images générées.

## Les mêmes kernels pour deux API graphiques

Les deux backends conservent le graphe hôte et les poids 310.9.1. Le chemin DX12
intercepte la création des kernels de calcul NvAPI ; le chemin Vulkan adapte
la création des modules CUDA NVX et leurs lancements. Les deux substituent les
images SM86 vérifiées issues des mêmes packs corrigés. La liaison à l'API change,
mais l'arithmétique neuronale et la correction temporelle restent communes.
Le jeu fournit toujours mouvement, profondeur et présentation des images ; un
renommage ne remplace pas une intégration absente et n'ajoute pas de backend DX11.

## Traçabilité

SHA256 de `version.dll` -9 : `114004043035c3f8f91b1b8909bdb8b7e68fa36394aeb339c339e30042684561`.
Il s'agit du binaire exact validé en dynamique en jeu, sans reconstruction.
Le runtime embarqué et les deux packs corrigés sont inchangés depuis la -8 ;
les nouveaux travaux concernent les contrôles hôtes de génération et les capacités.
Le renommage ne change pas son empreinte. Les validations de jeux nommés ci-dessus
restent attribuées à leurs releases d'origine. Les versions -0 à -6 ont été retirées.
Seule la synthèse technique publique accompagne le binaire, sans journaux de
développement ni programmes de test. Voir la [portée des validations](validation-summary.json).
