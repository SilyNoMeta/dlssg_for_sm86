<div align="center">

<h1>DLSS Frame Generation<br>pour les RTX série 30</h1>
<p>Plus d’images. Des mouvements plus fluides. Un multiplicateur qui suit votre jeu.</p>
<p>
<img alt="Version 310.9.1-9" src="https://img.shields.io/badge/release-310.9.1--9-76b900?style=flat-square">
<img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square">
<img alt="DirectX 12 et Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square">
<img alt="SM86" src="https://img.shields.io/badge/GPU-SM86-30363d?style=flat-square">
</p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-9/dlssg-sm86-310.9.1-9-win64.zip">Télécharger la 310.9.1-9</a></strong> · <a href="RELEASE-NOTES.md">Les nouveautés</a> · <a href="docs/install-loaders.fr.md">Guide d’installation</a></p>
<p><a href="README.en.md">English</a> · <strong>Français</strong> · <a href="README.zh-CN.md">简体中文</a></p>

</div>

---

Profitez de **DLSS Frame Generation 310.9.1** sur les GPU **Ampere SM86 / RTX série 30 compatibles**. Cette adaptation expérimentale s’appuie sur le [projet original de sdli1995](https://github.com/sdli1995/dlssg_for_sm86) : mouvements MFG corrigés, optimisations au choix et une seule DLL pour **DirectX 12 et Vulkan**.

**La nouveauté de la -9 :** des multiplicateurs fixes jusqu’à **X6**, le **Dynamic MFG natif sur les intégrations DX12 compatibles**, et des réglages dans un seul INI modifiable. Le jeu doit déjà intégrer DLSS Frame Generation.

## Ce que ça change pour vous

| Fonction | En pratique |
|---|---|
| **Choisir de X2 à X6** | Essayez davantage d’images générées entre les images rendues, dans la limite du plugin chargé. X4 correspond à une image rendue et trois images générées. |
| **Laisser le Dynamic MFG choisir** | Indiquez la cible de votre choix au runtime NVIDIA : il adapte le multiplicateur à la charge. Nécessite une intégration Streamline DX12 et un pilote compatibles. |
| **Retrouver un mouvement bien réparti** | Les images intermédiaires occupent des positions différentes le long du mouvement. La correction temporelle résout l’ancien défaut « beaucoup de FPS, peu de fluidité ». Elle reste toujours active. |
| **Jouer en DX12 ou Vulkan** | Les deux utilisent les mêmes kernels SM86 corrigés. X5/X6 fixe dépend du plugin du jeu ; le dynamique natif reste réservé à DX12. |
| **Coexister avec vos mods** | Gardez `version.dll`, renommez-la en `dxgi.dll` ou chargez-la comme plugin ASI. C’est le même fichier, avec les mêmes fonctions. |
| **Choisir vos optimisations** | Quatre optimisations GPU activables séparément dans un INI. Aucun outil de compilation ni installation CUDA nécessaire pour jouer. |

Davantage d’images générées peut améliorer la fluidité visuelle, mais **X6 n’est pas forcément le meilleur choix**. La réactivité dépend toujours de la cadence réellement rendue, et les artefacts peuvent devenir plus visibles avec un facteur élevé. Commencez par X2 ou X3, puis comparez en mouvement.

## Pour commencer

1. **Téléchargez et extrayez** le [ZIP de la release](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-9/dlssg-sm86-310.9.1-9-win64.zip).
2. **Fermez le jeu et sauvegardez** les fichiers à remplacer. Copiez `version.dll` et `dlssg_sm86.ini` à côté du véritable exécutable du jeu. Pour Wukong : `b1/Binaries/Win64`.
3. **Activez DLSS Frame Generation dans le jeu.** L’INI fourni laisse le jeu choisir son mode et autorise un plafond X6 lorsque l’intégration le permet.
4. **Modifiez l’INI** pour choisir un facteur fixe ou activer le dynamique sur les jeux compatibles. Relancez après chaque changement de configuration.

> **Vous découvrez les mods DLSS ?** [RHI](https://github.com/RankFTW/RHI) facilite la gestion des versions DLSS et des outils complémentaires. Suivez son guide, puis installez la DLL de ce projet avec les étapes ci-dessus.

Vous utilisez déjà d’autres mods ? Choisissez un seul mode de chargement :

| Fichier à installer | Quand l’utiliser |
|---|---|
| `version.dll` | Chargement direct, le choix par défaut. |
| `dxgi.dll` | Renommez la même DLL pour un chargement direct via DXGI, sans ASI Loader. |
| `dxgi.asi` | Renommez la même DLL et chargez-la avec [Ultimate ASI Loader x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader). Le loader lui-même peut occuper `version.dll`. |

**Une seule copie de notre DLL.** Gardez le nom `dlssg_sm86.ini`, à côté de notre DLL/ASI. Conservez vos éventuels proxys ReShade ou autres : le [guide d’installation](docs/install-loaders.fr.md) explique la cohabitation, les autres noms ASI et le retour en arrière. Ne renommez pas ce fichier en `nvngx_dlssg.dll`.

## Réglez-le à votre façon

Ouvrez **`dlssg_sm86.ini`**, à côté de notre DLL, avec un éditeur de texte. Mettez les valeurs de votre choix, enregistrez et **relancez le jeu**. Le fichier fourni contient :

```ini
[FrameGeneration]
MaxMultiplier=6
ForceMultiplier=0
DynamicMFG=0
DynamicTargetFPS=0
```

| Paramètre | La valeur à mettre |
|---|---|
| `MaxMultiplier` | Votre plafond, de **2 à 6**. Le plugin chargé doit prendre en charge le facteur demandé. |
| `ForceMultiplier` | **0** laisse choisir le jeu ; **2 à votre plafond** demande ce multiplicateur fixe. |
| `DynamicMFG` | **1** demande le dynamique natif sur les intégrations DX12 compatibles ; **0** ne le demande pas via notre DLL. |
| `DynamicTargetFPS` | **0** vise la fréquence de l’écran. Indiquez **votre propre cible de FPS** (entier de 1 à 1000) pour le dynamique. |

**Vous voulez du X5 fixe ?** Mettez `MaxMultiplier=6`, `ForceMultiplier=5` et `DynamicMFG=0`. Pour X2, X3, X4 ou X6, remplacez simplement la valeur du facteur.

**Vous voulez une adaptation automatique ?** Mettez `DynamicMFG=1` et choisissez votre `DynamicTargetFPS`. Avec `ForceMultiplier=0`, le choix du jeu sert de repli. Vous pouvez aussi prévoir un repli fixe, par exemple `ForceMultiplier=4`, si le dynamique est indisponible et le forçage fixe pris en charge.

La cible est un objectif, **pas une garantie de FPS constants** ; VSync peut prendre le dessus. FG doit être activé dans le jeu, mais le menu n’a pas besoin d’une entrée « Dynamic ». Ces réglages n’ajoutent pas de nouveaux boutons.

Le dynamique natif exige une **intégration Streamline DX12 et un pilote compatibles**. Le forçage fixe nécessite aussi un chemin Streamline reconnu ; les intégrations NGX directes restent pilotées par le jeu. Sous **Vulkan**, utilisez le mode fixe : le dynamique natif n’y est pas activé. Un choix dynamique natif déjà effectué par le jeu est conservé, même si notre demande dynamique est désactivée.

**Vous gardez un ancien INI ?** Ajoutez la section ci-dessus pour accéder à ces contrôles. Sans elle, les valeurs par défaut sont `MaxMultiplier=4` et `0` pour les trois autres clés. Le nouvel INI fourni autorise explicitement X6 tout en laissant le jeu choisir son mode.

## De petites optimisations, au choix

Les quatre sont activées par défaut. Passez une valeur à `0` pour comparer, puis relancez le jeu. Les gains peuvent être modestes et dépendent de la charge.

| Réglage INI | Ce qui change |
|---|---|
| `HardwareBilinear` | Utilise le filtrage matériel du GPU pour la reconstruction finale. De petites différences de pixels sont possibles. Inspiré de l’option [HardwareBilinear du projet original](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md). |
| `Conv13SharedInput` | Réutilise les données d’entrée d’une convolution dans la mémoire partagée rapide du GPU. |
| `Conv0SharedInput` | Applique cette réutilisation à une autre convolution de reconstruction. |
| `ResidualVectorLoads` | Regroupe les lectures mémoire de deux convolutions résiduelles. |

Ces options se trouvent dans `[Optimizations]` et s’appliquent aux deux API. Une clé d’optimisation absente vaut `1`. Les désactiver toutes conserve la correction temporelle. Elles ne règlent ni Neural Rendering ni NR Cost Scaler ; aucun mode FP8/INT8 ni modèle neuronal réduit n’est inclus.

## Compatibilité et outils utiles

**Windows x64 · GPU SM86 compatible · jeu intégrant déjà DLSS FG.** Le jeu fournit les informations de mouvement/profondeur et la présentation. Cette DLL n’ajoute pas FG à n’importe quel jeu et ne fournit pas de backend DX11. Linux/Proton, DXVK et les RTX 20 ne sont pas validés.

Le Dynamic MFG natif a été confirmé fonctionnel en jeu sur une **RTX 3070 Ti Laptop avec 8 Go de VRAM**, pilote **616.92**. Ce retour porte sur un portable, pas sur toutes les cartes RTX 30 ni tous les jeux. Ce pilote testé ne constitue pas un minimum requis. Les facteurs élevés et le dynamique dépendent du **plugin Streamline réellement chargé et du pilote**, pas seulement du nom de la DLL.

Le testeur rapporte aussi une très bonne compatibilité avec **[DLSS Tool de ShortFuse](https://discord.com/channels/1408098019194310818/1543975158937821315)** et **[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884)**, disponibles via RHI. Leur compatibilité NR n’étend pas celle de notre DLL FG à d’autres GPU. Les liens Discord peuvent nécessiter de rejoindre le serveur.

Si ces outils vous rendent service, offrez une étoile à **[RHI](https://github.com/RankFTW/RHI)** et à **[RenoDX de ShortFuse](https://github.com/clshortfuse/renodx)**. Leur travail simplifie beaucoup l’installation.

## Quelle version essayer ?

| Version | Différence principale | Pour quel usage |
|---|---|---|
| **[310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9)** | Dynamique sur les intégrations DX12 compatibles, X5/X6 fixe, réglages INI, chargement universel. | **Commencez ici.** Inclut les corrections et les quatre optimisations précédentes. |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | X2–X4 corrigé, chargement `version.dll` / `dxgi.dll` / ASI. | Comparer ou revenir à une version sans les nouveaux contrôles MFG. |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | Première correction des mouvements MFG ; `version.dll` uniquement. | Comparaison historique de la correction temporelle. |

Les versions -0 à -6 ont été retirées à cause du défaut de mouvement MFG. Le rectangle blanc sur le graphique du benchmark Wukong reste un problème distinct connu.

## Pour les curieux · pour contribuer

Les [notes techniques](docs/research.fr.md) expliquent la correction temporelle, le partage des capacités entre vues, les vérifications et ce qui reste à mesurer. Pour le diagnostic, consultez le [guide des logs](docs/install-loaders.fr.md#configuration-et-vérification). Quand le filigrane NVIDIA est disponible, `Dyn DRV` indique le dynamique pilote ; `4x/6x` signifie X4 courant avec un plafond X6.

**Les retours d’autres configurations sont bienvenus.** Indiquez GPU/VRAM, pilote, jeu/API, version Streamline chargée, résolution, contenu de l’INI et réglages NR/Cost Scaler éventuels. Décrivez les mouvements et la réactivité ; les captures FrameView/PresentMon sont particulièrement utiles. [Partager un retour →](https://github.com/SilyNoMeta/dlssg_for_sm86/issues)

---

Basé sur [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86). Merci à [Michael Robles / RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) pour la correction temporelle, à [mavismmg / ImDreamt et MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) pour la référence MFG étendu/dynamique, et à [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) pour le chargement ASI. Le runtime et les ressources NVIDIA conservent leurs droits d’origine. [Mentions tierces](THIRD_PARTY_NOTICES.txt) · [Empreintes](SHA256SUMS.txt)
