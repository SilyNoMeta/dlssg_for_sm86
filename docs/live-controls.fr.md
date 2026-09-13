# Commandes en direct et référence INI — 310.9.1-11

Le ZIP unique contient le moteur DLL/ASI et le panneau ReShade facultatif. Sans ReShade, modifier l’INI à la main puis redémarrer. Garder `dlssg_sm86.ini` près du moteur et activer d’abord la FG dans le jeu. RTX 20 reste expérimental sans essai sur Turing physique.

## Raccourcis par défaut et personnalisation

**Limite connue :** les raccourcis de la DLL seule échouent dans le nouvel essai en jeu sur Wukong, malgré le chargement des liaisons valides. Les tests automatisés ne valident pas la détection des touches en jeu. Utiliser le panneau ReShade pour les changements en direct ; avec la DLL seule, modifier l’INI puis redémarrer. La syntaxe ci-dessous décrit l’interface implémentée, sans garantir son fonctionnement dans chaque intégration.

Par défaut : **Ctrl+F2 à Ctrl+F6** pour X2–X6, **Ctrl+F10** pour le dynamique,
**Ctrl+F11** pour suivre le jeu et **Ctrl+F12** pour restaurer les réglages INI.
Chaque combinaison peut être modifiée ; une valeur vide désactive le raccourci :

| Entrée | Action |
|---|---|
| `ForceX2` … `ForceX6` | Demander ce multiplicateur fixe dans les limites de l'INI et du plugin. |
| `RestoreINI` | Restaurer les réglages Force/Dynamic/cible lus au lancement. |
| `FollowGame` | Suivre le choix du jeu, y compris son propre mode dynamique, sans notre forçage INI. |
| `ActivateDynamicMFG` | Demander le dynamique natif avec la cible de l'INI, sur DX12 compatible. |

Configuration par défaut du prochain paquet :

```ini
[Hotkeys]
ForceX2=Ctrl+F2
ForceX3=Ctrl+F3
ForceX4=Ctrl+F4
ForceX5=Ctrl+F5
ForceX6=Ctrl+F6
ActivateDynamicMFG=Ctrl+F10
FollowGame=Ctrl+F11
RestoreINI=Ctrl+F12
```

Séparer les modificateurs et **une seule touche** par `+`. La casse et les
espaces autour des noms sont ignorés. Modificateurs : `Ctrl`, `Alt`, `Shift`,
`Win`. Touches : `F1`–`F24`, `A`–`Z`, `0`–`9`, `Insert`, `Delete`, `Home`, `End`,
`PageUp`, `PageDown`, `Space`, `Tab`, `Enter`, `Escape`, `Up`, `Down`, `Left`,
`Right`, `Backspace`, `Pause`. Les noms restent en anglais dans l'INI.
Un code de touche Windows à deux chiffres hexadécimaux est aussi accepté,
par exemple `0x41` pour A : [table Microsoft](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes).
Les lettres utilisent les touches virtuelles Windows ; vérifier la combinaison
sur votre disposition de clavier.

La combinaison doit correspondre exactement : `F8` ne déclenche pas l'action
`Ctrl+F8`. Maintenir une touche ne répète pas l'action. Le jeu doit être au
premier plan ; revenir par Alt-Tab avec une touche maintenue ne déclenche rien.
Une combinaison invalide est désactivée ; les doublons désactivent toutes les
actions concernées. Les touches ne sont pas interceptées : éviter les conflits
avec le jeu ou les autres overlays. Préférer des combinaisons ; une lettre seule
peut aussi déclencher une action pendant la saisie dans un chat en jeu.

Redémarrer après modification des raccourcis. Leur utilisation ne réécrit pas
l'INI et ne nécessite pas de redémarrage si le jeu soumet régulièrement ses options FG.

## Panneau ReShade ou raccourcis

Pour un panneau en jeu, choisir le **ZIP de contrôle ReShade**, qui contient la DLL moteur et `DLSSGControls.addon64`. Voir le [guide du panneau](reshade-controls.fr.md). L’add-on pilote la DLL ; il ne la remplace pas.

Le panneau propose **Apply for this session**, **Apply & save settings** et **Save keyboard shortcuts** séparément. Une sauvegarde réussie met à jour l'INI et les réglages sauvegardés utilisés par la session. `RestoreINI` restaure ces valeurs sans relire un fichier modifié manuellement. `ActivateDynamicMFG` reprend la cible sauvegardée dans l'INI : sauvegarder une cible de session pour la réutiliser avec ce raccourci.

Les commandes s'appliquent à la prochaine soumission des options FG Streamline par le jeu. Si une demande reste en attente, appliquer un réglage FG dans le menu du jeu. L'acceptation SDK ne prouve pas que le pilote utilise la cible ni que les images sont présentées. Le forçage fixe Vulkan exige un chemin Streamline reconnu ; le dynamique natif reste limité à DX12. Les intégrations NGX directes restent pilotées par le jeu. Le panneau ne modifie ni NR, ni Reflex, ni VSync, ni les profils NVIDIA.

## Définir le plafond d'images générées

`MaxInterpolatedFrames`, dans `[FrameGeneration]`, compte les images **générées**.
On ajoute une image rendue pour obtenir le multiplicateur affiché.

| MaxInterpolatedFrames | Mode maximal |
|---|---|
| 1 | X2 |
| 2 | X3 |
| 3 | X4 |
| 4 | X5 |
| 5 | X6 |

Valeur absente ou invalide : **5**. Le plugin chargé peut imposer un plafond plus
bas. La valeur 1 conserve X2 et les correctifs de compatibilité et de temporalité.
`ForceMultiplier` utilise le facteur affiché : `4` demande X4, `0` suit le jeu.

**Migration :** remplacer `MaxMultiplier=M` par `MaxInterpolatedFrames=M-1`.
Par exemple, `MaxMultiplier=6` devient `MaxInterpolatedFrames=5`. L'ancienne clé
n'est plus lue. Renommer aussi `[Hotkeys] DynamicMFG` en `ActivateDynamicMFG`.
Conserver `[FrameGeneration] DynamicMFG` près de `DynamicTargetFPS` : c'est
l'activation au démarrage ; `ActivateDynamicMFG` attribue seulement un raccourci.

## Télémétrie facultative des images source

```ini
[Telemetry]
Enabled=1
```

Le défaut est `0` ; redémarrer après modification. La DLL mesure les soumissions
Streamline réussies d'images source distinctes sur environ une demi-seconde.
Plusieurs appels pour la même image ne sont comptés qu'une fois. C'est une cadence
de soumission CPU, pas une mesure de fin du rendu GPU ni de latence d'entrée.
Des données périmées ou ambiguës restent indisponibles. Les intégrations NGX
directes sans interception des constantes Streamline ne sont pas couvertes.

OptiScaler doit contenir la [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156), encore en attente de revue à la publication. Aucun OptiScaler modifié n'est inclus dans ce ZIP. Activer la clé INI ne suffit pas à faire lire cette interface par un ancien binaire. Avec le support, le second nombre de FPS utilise cette cadence ; les backends FG gérés par OptiScaler conservent leur affichage. Le panneau ReShade peut aussi afficher la cadence indépendamment. [Configuration du compteur](standalone-reshade.fr.md).

## Couper notre journal

```ini
[Logging]
Enabled=0
```

Redémarrer après modification. Le défaut est `1`. Avec `0`, notre DLL ne crée
ni n'alimente `dlssg3109.log`. Un ancien fichier reste intact : sa présence ne
signifie pas que la journalisation continue. Cela ne coupe pas les journaux des
autres outils ou de NVIDIA. Réactiver avant de préparer un rapport de diagnostic.

## La cible dynamique diffère de l'INI ?

Vérifier l'override NVIDIA de **cible dynamique DLSSG**, global et spécifique au
jeu, en plus du limiteur FPS classique et de VSync. Ce sont des réglages distincts.
Le pilote peut remplacer une cible pourtant acceptée par Streamline. Sauvegarder
le profil avant de corriger l'override concerné, sans réinitialiser les autres réglages.


Si le journal est activé, `hotkey_bindings_loaded` indique le nombre de raccourcis valides. `hotkey_action_triggered=0` correspond à ForceX2 (1–4 à X3–X6). `live_multiplier_requested` prouve que la demande est enregistrée ; `sl_forced_multiplier_accepted` indique que Streamline l’accepte. Cela ne remplace pas la vérification des images présentées. Pour F4 seul, écrire `ForceX2=F4` dans `[Hotkeys]`, puis redémarrer.
