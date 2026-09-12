# DLSSG — add-on ReShade autonome (310.9.1-10)

Installer **ReShade avec prise en charge complète des add-ons + DLSSG.addon64 +
dlssg_sm86.ini**. Le moteur est intégré à l'add-on : aucune DLL/ASI séparée de
notre projet n'est nécessaire. Placer l'INI près de l'add-on dans le dossier
parcouru par ReShade. Retirer notre ancien proxy (version.dll / dxgi.dll / ASI)
et DLSSGControls.addon64 avant de relancer. Conserver ReShade, les autres loaders
nécessaires et les add-ons NR. Ne retirer que les fichiers de notre ancien paquet.

ReShade doit charger l'add-on avant l'initialisation de DLSSG.
Le moteur reste chargé jusqu'à la fermeture du processus pour conserver ses
interceptions lors d'une recréation du périphérique ReShade. Pour le retirer,
le désactiver pour le prochain lancement puis redémarrer le jeu.
Si ReShade se charge trop tard dans un jeu, utiliser le paquet DLL/ASI.
Ne pas cumuler avec l'add-on de déblocage MFG pour Ada.

## Régler la génération

Activer d'abord la FG dans le jeu. Dans ReShade, ouvrir **DLSSG Live Controls**.
Choisir les réglages enregistrés, le mode du jeu, un multiplicateur fixe ou le
Dynamic MFG. Le dynamique demande une intégration DX12 compatible.

- **Apply for this session** applique uniquement pour cette session.
- **Apply & save settings** enregistre aussi le mode et la cible FPS dans
  dlssg_sm86.ini, pour les retrouver au prochain lancement.
- L'état accepté décrit la dernière soumission au SDK, pas le multiplicateur
  dynamique instantané. Si la demande reste en attente, appliquer une option FG
  dans le menu du jeu.
- Par défaut, le jeu choisit son mode. Aucune cible FPS ni touche n'est imposée.

## Réaffecter les touches

Dans la section inférieure, cliquer sur **Record** en face de l'action, puis
appuyer sur une combinaison comme Ctrl+Alt+F8. Échap annule la capture.
Le champ est également éditable ; le vider désactive l'action.
**Save keyboard shortcuts** enregistre et active les raccourcis sans redémarrer.
Ce bouton ne sauvegarde pas les paramètres de génération.
Une combinaison invalide ou en double est refusée sans sauvegarde partielle.
Les raccourcis existants sont suspendus pendant la capture/édition dans le panneau ;
relâcher une touche avant de l'utiliser à nouveau.

Modificateurs : Ctrl, Alt, Shift, Win. Touches : F1–F24, A–Z, 0–9, noms comme
Insert/Delete/Home/End/PageUp/PageDown/Space/Tab/Enter/Escape et les flèches, ou
code Windows 0xNN. La capture utilise ce code pour les touches moins courantes.

## Paramètres de l'INI

MaxInterpolatedFrames est l'unique plafond : 1..5 = X2..X6, défaut 5.
ForceMultiplier utilise le facteur affiché : 0 suit le jeu, 2..6 demande X2..X6.
DynamicMFG et DynamicTargetFPS sont les paramètres de [FrameGeneration].
ActivateDynamicMFG, dans [Hotkeys], est uniquement le raccourci.
Les quatre optimisations, le plafond, la journalisation et la télémétrie restent
éditables dans l'INI avec redémarrage. Les sauvegardes du panneau conservent les
autres sections et passent par une copie temporaire : en cas d'échec, le fichier
et les réglages actifs précédents sont conservés.

## OptiScaler : tester uniquement le compteur

Utiliser un OptiScaler contenant la [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156), encore en attente de revue à la publication. Aucun binaire OptiScaler modifié n'est fourni ; l'INI seul ne met pas à jour un ancien consommateur. Régler **FG Output = None**, puis
**FG Input = None**, et garder la FG activée dans le jeu. Ne pas sélectionner
Nukem's ni un autre remplacement pour afficher le compteur.

1. Dans notre INI, mettre [Telemetry] Enabled=1 et redémarrer après sauvegarde.
2. À droite dans OptiScaler, ouvrir **FPS Overlay**.
3. Cocher **FPS Overlay Enabled** et choisir **Overlay Type = Simple**.
4. Cliquer **Save Settings**, puis redémarrer si des changements de backend étaient en attente.

Chercher deux nombres de FPS et la mention **DLSSG source telemetry**. Le second
nombre mesure la cadence CPU des images source ; le premier reste le compteur
existant d'OptiScaler. Les graphes au bas de sa fenêtre de réglages ne sont pas
cet overlay. En dynamique, ne pas diviser les FPS par le plafond configuré.
L'absence de second nombre signifie que les données sont indisponibles, périmées,
ambiguës ou que l'intégration n'est pas observée, pas que le jeu tourne à zéro FPS.
Notre panneau peut aussi afficher cette cadence lorsqu'elle est disponible.

## Ce qui a été testé

Chargement autonome et deux cycles de périphérique avec ReShade 6.8.0,
sauvegarde/relecture, erreurs d'écriture et conflits de touches : tests réussis.
Les commandes Streamline réelles passent sur DX12 et Vulkan, avec dynamique
natif limité à DX12. Le petit hôte DX11 sert seulement à vérifier l'interface :
il ne valide ni n'ajoute la FG sur DX11. L'utilisateur a confirmé les commandes autonomes, la capture des touches et le changement de cible dynamique dans Wukong sur RTX 3070 Ti Laptop 8 Go. Ce retour fonctionnel n'est ni un benchmark ni une validation de tous les jeux. Runtime et kernels inchangés ; RTX 20 reste expérimental.

## Cible dynamique et sauvegarde

L’override NVIDIA **Override DLSSG Target Frame Rate**, global ou par jeu, peut remplacer la cible du panneau. Désactiver l’override concerné puis relancer pour utiliser votre cible. Limiteur FPS classique et VSync restent distincts. Le raccourci dynamique utilise la cible sauvegardée dans l’INI : utiliser Apply & save settings pour la conserver. Voir la [référence INI](live-controls.fr.md).
