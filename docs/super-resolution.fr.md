# Résolution de rendu DLSS — contrôles expérimentaux

Les contrôles **DLSS image quality** restent accessibles dans tous les jeux.
Ils sont expérimentaux et servent surtout quand on injecte le DLSS dans un jeu
qui ne propose pas ses propres réglages de qualité DLSS ou de résolution de rendu.

**Si le jeu propose ces réglages, utilisez son menu graphique et laissez notre
override désactivé (`RenderScale=0`).** Les appels DLSS ne permettent pas de
détecter de façon fiable la présence d'un menu. L'injection du DLSS ne suffit pas
à garantir la compatibilité de l'override.

Choisissez un préréglage ou un pourcentage, puis **Apply scale for this session**.
Utilisez ensuite **Save render scale** pour conserver la demande dans `dlssg_sm86.ini`.
La sauvegarde d'un pourcentage non nul n'est autorisée qu'après **huit images DLSS
consécutives réussies à la résolution demandée**, avec deux pixels de tolérance
par axe pour l'arrondi du moteur. La DLL applique aussi cette vérification : une
demande en attente, ignorée ou contredite par les mesures ne peut pas être sauvegardée.
Après avoir choisi un nouveau pourcentage, il faut de nouveau l'appliquer.
Cette sauvegarde est indépendante de la génération d'images et des raccourcis.

| Bouton | Largeur et hauteur rendues |
|---|---:|
| DLAA | 100 % |
| Quality | 66,667 % |
| Balanced | 58,824 % |
| Performance | 50 % |
| Ultra Performance | 33,333 % |

Le curseur couvre **50–100 %**. Ultra Performance est un préréglage fixe séparé ;
les valeurs intermédiaires inférieures à 50 % ne sont pas prises en charge.
Le pourcentage s'applique aux deux axes : à 50 %, on rend un quart des pixels.

**Vérifiez « Observed DLSS ».** Cette ligne affiche les dimensions réellement
observées lors d'évaluations DLSS réussies. Une demande acceptée ou enregistrée
ne prouve pas son application. Un adaptateur moteur validé permet l'application
en direct ; d'autres jeux peuvent mémoriser ou ignorer la recommandation.
Sauvegarder puis redémarrer ne garantit pas que cela fonctionnera.

Un échec au démarrage a été signalé après la sauvegarde d'un override dans un jeu
avec réglages DLSS natifs ; sa cause exacte reste indéterminée. **Dans ce cas,
fermez le jeu et remettez `RenderScale=0` dans le fichier INI avant de relancer.**
Pendant une session, désactivez l'override puis appliquez pour rendre la main au
jeu. Avec l'adaptateur moteur, l'ancien pourcentage est restauré ; les autres
jeux décident quand relire les recommandations.

Sans ReShade, modifiez cette section puis redémarrez pour lire le fichier :

```ini
[SuperResolution]
RenderScale=0
```

`0` suit le jeu ; `50` à `100` choisissent un pourcentage personnalisé ; `33.333`
choisit Ultra Performance. Les valeurs absentes ou invalides reviennent à `0`.
Utilisez un point décimal dans l'INI. Les modifications manuelles contournent la
vérification en jeu : privilégiez le panneau. Un redémarrage relit le fichier,
mais ne rend pas une intégration compatible. La sauvegarde de `0` pour désactiver
l'override reste toujours possible, même sans DLSS actif.

Le DLSS doit déjà être actif. Ces contrôles changent la résolution, pas le
modèle neuronal K/M, et n'ajoutent pas le DLSS à un jeu. Utilisez la DLL moteur
et le `DLSSGControls.addon64` correspondant ; le panneau ReShade reste facultatif.
