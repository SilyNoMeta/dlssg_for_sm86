# Installation : version.dll, ASI ou dxgi.dll

Release **310.9.1-8** — [télécharger le paquet universel](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8).
Il contient une seule `version.dll`, utilisable aussi sous les noms `dxgi.dll` ou `dxgi.asi`.
Ces modes nécessitent la -8 ; le binaire -7 original doit garder son nom `version.dll`.

Tous les noms utilisent les mêmes runtime DX12/Vulkan, kernels,
correctif temporel et options INI. Fermer le jeu et sauvegarder les fichiers
existants, puis choisir **une seule** installation près du véritable exécutable.
N'installer qu'une copie de notre bridge et conserver son INI en changeant de mode.

## Avec Ultimate ASI Loader

1. Installer [Ultimate ASI Loader x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader)
   sous le nom `version.dll`.
2. Renommer **notre** `version.dll` en `dxgi.asi` et la placer à côté.
3. Placer `dlssg_sm86.ini` dans ce même dossier, sans le renommer.
4. Relancer le jeu et activer DLSS Frame Generation dans ses réglages.

```text
Jeu.exe
version.dll       ← Ultimate ASI Loader x64
dxgi.asi          ← notre bridge
dlssg_sm86.ini     ← configuration du bridge
```

REFramework peut conserver son `dinput8.dll`. Les noms `version.dll` et
`dxgi.asi` correspondent ici à deux produits distincts.
Avec UAL, un autre nom `.asi` fonctionne aussi grâce à `InitializeASI` :
`dlssg_sm86.asi` a été vérifié dans notre test de chargement. Avec un loader qui
n'appelle pas cette fonction, garder `dxgi.asi`, qui démarre automatiquement.
Pour les plugins installés dans un sous-dossier ASI, garder l'INI à côté du plugin.

## Directement sous dxgi.dll

Renommer notre `version.dll` en `dxgi.dll`, puis placer cette DLL et
`dlssg_sm86.ini` à côté de l'exécutable. Ce mode ne nécessite pas d'ASI loader.

```text
Jeu.exe
dxgi.dll          ← notre bridge, qui transmet aussi les appels DXGI à Windows
dlssg_sm86.ini
```

Si `dxgi.dll` est déjà utilisé par un autre mod, par exemple ReShade, conserver
ce mod et choisir le mode ASI. Notre proxy DXGI transmet à Windows ; il ne
chaîne pas automatiquement un autre proxy DXGI.

## Directement sous version.dll

Placer notre `version.dll` et `dlssg_sm86.ini` à côté de l'exécutable, sans
ajouter d'ASI loader. Choisir un autre mode si ce nom est déjà occupé.
Le jeu doit charger le nom de DLL choisi pour déclencher le bridge.
Ne jamais renommer le bridge en `nvngx_dlssg.dll`.

## Configuration et vérification

Le nom de l'INI reste **`dlssg_sm86.ini`**, quel que soit le nom de notre DLL.
Les quatre options sous `[Optimizations]` acceptent `1` ou `0` ; l'absence de
fichier ou de clé conserve la valeur `1`. Redémarrer le jeu après modification.
La correction temporelle X3/X4 reste toujours active.

Dans `dlssg3109.log`, chercher `asi_attached`, `dxgi_attached` ou
`proxy_attached`, puis `installed_310_9_1` lorsque le runtime est pris en charge.
Le loader ASI n'a pas besoin d'afficher une interface pour fonctionner.
Un simple chargement du plugin ne prouve pas que la génération d'images tourne.

Le binaire universel passe les tests automatiques de chargement et d'images
DX12/Vulkan. Le mode direct `dxgi.dll` est confirmé fonctionnel dans Wukong
sur RTX 3070 Ti Laptop 8 Go. Ce retour ne constitue pas un nouveau benchmark.
Le nom n'ajoute pas de génération d'images à un jeu qui ne l'intègre pas,
ni de backend DLSSG DX11. Pour revenir en arrière, fermer le jeu, retirer
la copie du bridge installée et restaurer les fichiers sauvegardés.
