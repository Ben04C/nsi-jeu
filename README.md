# nsi-jeu

<h2>**A propos**</h2>
Ce projet est un petit jeu fait avec python et la bibliothèque pygame.

<h2>**Configuration requise**</h2>
Ce projet utilise la version python 3.9 et la version 2.0.1 de pygame. <br>
Afin d'installer pygame faire **pip install pygame**

<h2>**Guide D'utilisation**</h2>
<p>Pour lancer le jeu: executer le fichier main.py Un menu va apparaitre il est possible de naviguer entre les options avec les fleches et de séléctionner avec la touche entrée. SEULE L'OPTION START GAME FONCTIONNE POUR L'INSTANT une fois cette option choisie, le jeu lui-même va apparaitre. Il y aura un bref dialogue. Une fois le dialogue terminé il sera possible de se déplacer avec les touches droite et gauche du clavier.</p><br>
<p>Le code du jeu est compris dans le fichier python main.py, le code du menu est compris dans game.py et menu.py. Afin d'accéder aux fichiers du jeu comme les images ou la musique/son aller dans le dossier assets. Tout y est rangé par catégorie.
  <br>
Une fois lancé,le menu apparaitra, il est possible de bouger le "cursor" (la petite etoile a gauche du texte) avec les fleches de haut et de bas. Par contre, pour le moment on peut seulement lance le jeux en cliquant sure la touche d'entree sur le clavier qui fera en sorte que une fenêtre apparaitra avec  un court dialogue. Après avoir lu le message un simple click sur n'importe quel touche du clavier permet de passer à la prochaine étape du jeu. Attention, une fois passé à la prochaine étape, il n'est pas possible de retourner en arrière car le jeu est basé sur la memoire du jouer et comment il arrive a convertir les dialoges en indices. Pour terminer le programme il suffit de passer à la dernière étape et cliquer sur la crois en haut à droite.</p>


<h2>**QUESTIONS: Faire le point sur les difficultés rencontrées**</h2>
<h3>Quelles sont celles qui ont été surmontées ?</h3>
<p>L’équipe a commencé à travailler ensemble sur un projet qui crashait au bout de quelques secondes d'exécution. La très grande majorité du code (qui était dans la boucle while running) à été supprimé. Maintenant il est possible d’avoir des phases de  dialogues et d'enquête. On vise une fin du jeu vers la fin de la première enquête et dialogue.(l’histoire du jeu pourrait continuer indéfiniment et donc le développement aussi) </p>
<br>
<h3>Quelles sont celles qu'il faut absolument régler au plus vite ?</h3>
<p>Il faut créer une partie interactive où l'on peut examiner les objets. Une bulle avec écrit “press e to examine” se montrera et on pourra interagir avec l’objet afin de faire avancer l'enquête. Il faudrait aussi réussir à trouver une histoire afin d’avoir un objectif en tête quand on insère des indices. De plus, il y a encore un peu de graphisme qui est requis afin de dessiner les indices et les autres personnages. Enfin, il faudrait que le menu soit complètement  fonctionnel. Pour l’instant seule l’option start game fonctionne. L’idée d’un système de mot de passe qui permet au joueur de revenir à son point à été discutée. Un système de sauvegarde automatique est aussi envisagé.</p>
<br>
<h3>Quelles sont celles qu'on aura pas le temps de surmonter et qu'est-ce que cela implique comme évolution sur le projet final ?</h3>
<p>On voulait implémenter un point and click avec la souris où on peut clicker sur un objet et on peut intéragir avec (le ramasser, l’utiliser si c’est possible…), mais on a décidé de ne pas le faire car ça allait prendre trop de temps. A la place, on doit clicker sur la touche E (référence aux jeux de valve) pour intéragir avec un objet lorsqu’on est assez proche, ce qui devrait être plus facile à coder.
On voulait aussi créer des nouvelles scènes mais ça va prendre du temps à dessiner donc pour l’instant on garde une seule scène.
On veut aussi ajouter des effets sons et de la musique mais on est pas sûrs d’avoir le temps de les faire.
</p>
<br>
<h3>Séance du 09/02</h3>
<p>Aujourd'hui le systeme d'inspection d'objets a été pas mal avancé, Maintenant il y a un dialogue lorsqu'on inspecte le pot de fleur. Un fois ce dialogue terminé, le pot de fleur disparaîtra (on ne le voit pas car le tableau contient toujours l'image du pot sur lui même). Il y a aussi eu des variables comme kbushes (diminutif de knowledge about bushes) qui ont étées crées pour savoir ce que le personnage a inspecté et donc a retenu.</p>

<br>
<br>
<br>
<br>
old:
<br>
A pygame project The story: Screen is flickering while it says“Flicker, Flicker, Flicker, Flicker, You’re a goner”. A murder in a small alley from a slum. Police is already there. A detective (You) arrives at the crime scene.

Crime scene: In a slum outside a shop, blinds closed with a flickering neon in a dark alley. A small blanket is hiding the body covering everything but the feets are visible . see doodle in brainstorming.

A policeman briefs us on the subject: He says that the victim was working for the government inside of the justice department. The fingerprints from the rebel leader [Find name]’s fingerprints are on the weapon. (At the end of the game you will discover that this evidence was fabricated by the justice minister himself in order to convict the rebel leader). There are no witnesses known at this point in time.

First investigation. You analyse the crime scene and you find the victim’s phone. You write down the numbers. The victim has a perper in his hand. Fin wallet and get the ID card. You find a mysterious metal object (It is a key but you don’t know yet).

The next day: Then the inspector steps in his car drives of and the scene transitions into his office where he is inspecting all the information. secretary comes in after a while 2 bring him coffee and tell him what she found. they go and visit the dead persons relatives who lead him to his lab

More info here: https://drive.google.com/drive/folders/12LP5qPFR-3ibHgnq7ksZ8RhxedlxClWv?usp=sharing

Problemes en ce momment: </br>
- .blit n'affiche pas d'images, il doit y avoir une erreur. - Je ne penses pas que  c'est le load qui pose probleme car l'icone de la fenetre fonctionne parfaitemet.

- Le texte ne s'affiche pas aussi. (La méthode .blit est aussi utilisée)
