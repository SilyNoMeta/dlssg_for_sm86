# Commandes en direct et référence INI — 310.9.1-10

Ces commandes fonctionnent avec le paquet DLL/ASI ou avec le paquet ReShade autonome. Installer un seul moteur, avec `dlssg_sm86.ini` à côté, puis activer la FG dans le jeu. RTX 20 reste expérimental sans test sur Turing physique.

## Des raccourcis choisis par vous

**Aucun raccourci n'est attribué par défaut.** Dans `[Hotkeys]`, remplir les
actions souhaitées ; une valeur vide désactive le raccourci :

| Entrée | Action |
|---|---|
| `ForceX2` … `ForceX6` | Demander ce multiplicateur fixe dans les limites de l'INI et du plugin. |
| `RestoreINI` | Restaurer les réglages Force/Dynamic/cible lus au lancement. |
| `FollowGame` | Suivre le choix du jeu, y compris son propre mode dynamique, sans notre forçage INI. |
| `ActivateDynamicMFG` | Demander le dynamique natif avec la cible de l'INI, sur DX12 compatible. |

Exemple à copier **uniquement si ces touches vous conviennent** :

```ini
[Hotkeys]
ForceX4=Ctrl+Alt+F6
ForceX6=Ctrl+Alt+F8
RestoreINI=Ctrl+Alt+F9
FollowGame=Ctrl+Alt+F10
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

Pour un panneau, choisir le **ZIP ReShade autonome** à la place du ZIP DLL. Voir le [guide autonome](standalone-reshade.fr.md). Aucun compagnon `DLSSGControls.addon64` n'est fourni ni nécessaire.

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
