
# Réalisateurs 
Robin Lamotte 17051 - Damien Ryckaert 18040

# Modules utilisés 
json, socket, sys, cherrypy, random, time, copy, pickle, ast, re


# AVALAM-PROJECT
Project Avalam
Règles du jeu:
http://www.oya.fr/?post/2014/12/09/73-avalam-est-a-oya

L'IA est basée sur le framework easyAI, voir:
https://github.com/Zulko/easyAI/blob/master/README.rst

!!!attention!!!
 Certains codes d'easyAI ont été modifiés pour mieux correspondre aux critères d'évaluation. Avalam_project importe ces fonctions réécrites (au lieu de les importer d'easyAI). Il faut donc télécharger tous les fichiers du projet!!

L'IA utilise Negamax, une variante de l'algorithme Minimax avec élagage 'alpha/beta' afin d'optimiser la recherche.
https://en.wikipedia.org/wiki/Negamax
Ce code génère tous les états qu'il est possible d'atteindre en x coups et attribue à chacun d'entre eux une valeur avec la fonction d'évaluation Avalam.scoring().
Celle-ci calcule dans un premier temps le nombre de tours que possède chaque équipe (le score direct). 
Ensuite, elle cherche si cette tour pourrait encore se déplacer ou être prise par l'adversaire. Si non, c'est qu'elle est 'figée'. Elle ne bougera plus de la partie, donc le point qu'elle rapporte peut être considéré comme acquis. Ces tours valorisent le score du joueur qui la possède. Cette façon d'évaluer le score vise à compenser le fait que Negamax n'a pas le temps de calculer très profondément.
Negamax cherche ensuite quel coup amènera son joueur à obtenir le meilleur score en supposant que l'adversaire jouera également le mieux possible.
L'élagage alpha/beta fait gagner du temps à l'algorithme en l'empêchant d'explorer des situations moins bonne que la meilleure déjà trouvée.
De plus, Negamax attribue plus de valeur à un même état de jeu s'il est atteint plus rapidement (par exemple atteindre un score de 7 en 3 coups vaut mieux qu'en 5 coups).
L'algorithme devient trop lent en début de partie (moment où le plus de coups sont possibles), il commence donc avec une profondeur de 2, et l'augmente en fin de partie. Un temps limite (break_time) à été ajouté à Negamax pour limiter le temps de réflexion à (un peu) moins de 10 secondes au cas où celui-ci dépasserait la limite imposée.   


inscription: inscription.py
serveur ia: battle_server.py


Pour jouer contre l'ia dans le terminal, appeler la fonction human_vs_ai(human_color=1).
Pour voir jouer l'ia contre random, appeler la fonction random_vs_ai(random_color=1).

Pour obtenir de l'ia un seul coup sans jouer toute la partie, appeler la fonction AI_runner(state=body). (body étant l'état du jeu reçu part le serveur).

Lorsqu'on joue human_vs_ai():
'Player 1' a les pions '0' et 'Player 2' a les pions '1'.    
Les tours sont représentées par un tuple de forme (pion dominant la tour, nombre de pions dans la tour).
Quand c'est au tour de Human_Player de jouer, le joueur peut rentrer dans la ligne de commande:
<<<<<<< HEAD
    - le mouvement à jouer, sous forme de 4 numéros 'ab cd' avec a=ligne 'from', b=colonne 'from', c=ligne 'to', d=colonne 'to'
    - 'show moves' pour montrer tous les coups possibles
    - 'move #nbr' pour jouer le coups numéro 'nbr' proposés par 'show moves'
    - 'quit' pour interrompre le jeu


