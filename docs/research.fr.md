# Justesse temporelle et optimisations incluses

11 septembre 2026 · release 310.9.1-7 · [English](research.en.md) / [Français](research.fr.md) / [简体中文](research.zh-CN.md)

## Observation et hypothèse

L'[issue #2](https://github.com/SilyNoMeta/dlssg_for_sm86/issues/2) décrit 160–170 FPS en X4 mais une mauvaise fluidité
dans Cyberpunk et Onimusha sur RTX 3060 Ti 8 Go. Le mainteneur retrouve ce ressenti
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

52 cas hors jeu sur RTX 3070 Ti Laptop 8 Go, pilote 616.92 : 49 succès attendus
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
une forte amélioration de fluidité X4 dans Wukong avec cette DLL exacte.
Cyberpunk, Onimusha/ASI loader et un nouvel essai Vulkan en jeu restent à confirmer.
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

## Premières mesures en jeu

Wukong 1.0.21.23831, DX12, 2560×1440, High/Élevé, ray tracing intégral Faible,
super résolution 58, flou Fort ; RTX 3070 Ti **Laptop 8 Go**, i9-12900H, pilote 616.92.
Réglages NR/Cost Scaler et repère de capture déclarés identiques ; les valeurs NR
exactes ne figurent pas dans les CSV. Un passage d'environ 60 secondes par condition.

| Configuration X4 | FPS affichés | 1 % low | Latence PC moyenne |
|---|---:|---:|---:|
| Original natif 310.1 | 106,151 | 61,112 | 87,691 ms |
| Ancienne -4 | 103,710 | 72,330 | 88,099 ms |
| DLL corrigée (-7) | 98,064 | 66,295 | 91,377 ms |

**Le compagnon Codex était visible, sans être utilisé, pendant le passage corrigé.**
Les conditions diffèrent donc des passages antérieurs : ces chiffres ne prouvent
ni une régression de FPS causée par le correctif, ni un gain. Le résultat nouveau
est le ressenti X4 nettement plus fluide, cohérent avec le test de mouvement.
La capture du benchmark complet affiche 102 FPS ; elle porte sur un autre
intervalle que les 98,064 FPS des 60 secondes FrameView.

Les [agrégats des captures](benchmark-summary.csv) comprennent la première série
-0…-4 et les passages original/corrigé. Les empreintes identifient les sources ;
les journaux personnels bruts ne sont pas publiés. FPS=1000N/ΣΔt, avec
MsBetweenDisplayChange. Les lows inversent la moyenne des ceil(0,01N)/ceil(0,001N)
intervalles les plus longs. Intervalles nuls et pics restent inclus. La latence PC
est la moyenne MsPCLatency. Les images d'un passage ne sont pas des répétitions
indépendantes du benchmark : aucun intervalle de confiance trompeur n'est fourni.
Les retours d'autres GPU et jeux sont bienvenus, avec mouvement et réactivité en plus des FPS.

## Traçabilité

SHA256 de la DLL : `d10fc4d245ddfa0a8b2bd5530dfde23547bf193d6f30623d4875627db1002bef`.
La DLL publiée est celle testée comme candidate temporelle, sans reconstruction.
Les releases -0…-6 ont été retirées à cause du défaut MFG ; leurs résultats sont
conservés pour interprétation, pas comme téléchargements recommandés.
Cette documentation présente la méthode et les agrégats autorisés ; les journaux
de développement et applications de test privés ne sont pas fournis.
