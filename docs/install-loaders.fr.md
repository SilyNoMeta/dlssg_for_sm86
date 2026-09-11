# Installation : version.dll, ASI ou dxgi.dll

Ces instructions décrivent les modes préparés pour la prochaine version.
Ils ne sont pas pris en charge par le binaire -7 téléchargeable.

Le même binaire contient le bridge DX12/Vulkan, le runtime, les kernels et les
options INI. Choisir **une seule** des installations suivantes, dans le dossier
du véritable exécutable du jeu. N'installer qu'une copie de notre bridge.

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

## Configuration et vérification

Le nom de l'INI reste **`dlssg_sm86.ini`**, quel que soit le nom de notre DLL.
Les quatre options sous `[Optimizations]` acceptent `1` ou `0` ; l'absence de
fichier ou de clé conserve la valeur `1`. Redémarrer le jeu après modification.
La correction temporelle X3/X4 reste toujours active.

Dans `dlssg3109.log`, chercher `asi_attached`, `dxgi_attached` ou
`proxy_attached`, puis `installed_310_9_1` lorsque le runtime est pris en charge.
Le loader ASI n'a pas besoin d'afficher une interface pour fonctionner.
Un simple chargement du plugin ne prouve pas que la génération d'images tourne.

La version combinée passe les tests automatiques de chargement et d'images
DX12/Vulkan. Le mode direct dxgi.dll reste à tester en jeu. Le nom de fichier
n'ajoute pas de génération d'images à une intégration absente, ni de backend DX11.
