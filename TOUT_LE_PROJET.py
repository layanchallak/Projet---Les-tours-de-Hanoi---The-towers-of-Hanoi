# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:20:57 2023

@author: primo tech
"""

'''Partie A'''
def init(n):
    # Initialize an empty list for each tower
    plateau = [[], [], []]
    # Add the disks to the leftmost tower
    plateau[0] = list(range(n, 0, -1))
    return plateau

def nbDisques(plateau, numtour):
    return len(plateau[numtour])

def disqueSup(plateau, numtour):
    if plateau[numtour]:
        return plateau[numtour][-1]
    else:
        return -1


def posDisque(plateau, numdisque):
    for index, tower in enumerate(plateau):
        if numdisque in tower:
            return index
    return -1  # Normalement cela ne devrait pas arriver si le disque est forcément présent

def verifDepl(plateau, nt1, nt2):
    # Check if the initial tower has disks.
    if not plateau[nt1]:
        return False
    else:
        disk_to_move = plateau[nt1][-1]
    
    # Check if the destination tower is empty or the top disk is larger than the one we want to move.
    if not plateau[nt2] or plateau[nt2][-1] > disk_to_move:
        return True
    else:
        return False


def verifVictoire(plateau, n):
    # Check if the last tower has n disks in the correct order and the other towers are empty.
    return plateau[-1] == list(range(n, 0, -1)) and all(not tower for tower in plateau[:-1])
'''PARTIE B'''
import turtle

def dessinePlateau(n):
    turtle.speed(-1)  # Set the drawing speed to the fastest
    turtle.penup()

    # Constants for the drawing based on disk number
    largest_disk_diameter = 40 + 30 * (n - 1)
    base_width = 4 * largest_disk_diameter + 2 * 20  # 20 is the horizontal gap between towers
    tower_height = 20 * (n + 2)  # Each disk's thickness is assumed to be 20
    turtle.fillcolor('black')
    # Position the turtle at the starting point for the base
    turtle.goto(-300, -200)
    # Draw the base
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(base_width)
    turtle.left(90)
    turtle.forward(20)  # The thickness of the base
    turtle.left(90)
    turtle.forward(base_width)
    turtle.left(90)
    turtle.forward(20)  # The thickness of the base
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    # Draw the towers
    for i in range(3):
        tower_position = -300 + largest_disk_diameter + (largest_disk_diameter + 20) * i
        turtle.goto(tower_position, -200)
        turtle.pendown()
        turtle.begin_fill()
        turtle.left(90)
        turtle.forward(tower_height)  # The height of the tower
        turtle.right(90)
        turtle.forward(6)  # The thickness of the tower
        turtle.right(90)
        turtle.forward(tower_height)  # The height of the tower
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()

    turtle.hideturtle() 
    
def dessineDisque(nd, plateau, n):
    turtle.speed(-1)
    turtle.penup()
    
    # Disk and tower calculations
    disk_height = 20
    disk_diameter = 40 + 30 * (nd - 1)
    tower_width = 6
    tower_spacing = 20
    base_position = -300
    largest_disk_diameter = 40 + 30 * (n - 1)
    # Find the disk's tower and position
    for tower_index, tower in enumerate(plateau):
        if nd in tower:
            disk_position = tower.index(nd)
            break
    
    # Calculate x position of the disk
    x_position = base_position -20 +  (largest_disk_diameter + tower_spacing) * (1+tower_index) + tower_width / 2
    # Calculate y position of the disk
    y_position = -200 + 20 + disk_height * disk_position

    # Draw the disk
    turtle.goto(x_position - disk_diameter / 2, y_position)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(disk_diameter)
        turtle.left(90)
        turtle.forward(disk_height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def effaceDisque(nd, plateau, n):
    # Paramètres pour le dessin
    disk_height = 20
    disk_diameter = 40 + 30 * (nd - 1)
    tower_width = 6
    base_position = -300
    tower_spacing = 20
    largest_disk_diameter = 40 + 30 * (n - 1)

    # Trouver la tour et la position du disque
    for tower_index, tower in enumerate(plateau):
        if nd in tower:
            disk_position = tower.index(nd)
            break
    else:
        print(f"Error: Disk {nd} not found on any tower.")
        return

    # Calculer la position du disque
    x_position = base_position -20 +  (largest_disk_diameter + tower_spacing) * (1+tower_index) + tower_width / 2
    y_position = -200 + 20 + disk_height * disk_position

    # Effacer le disque en le dessinant en blanc
    turtle.goto(x_position - disk_diameter / 2, y_position)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(disk_diameter)
        turtle.left(90)
        turtle.forward(disk_height)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(x_position - tower_width / 2, y_position)

    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(tower_width)
        turtle.left(90)
        turtle.forward(disk_height)  # Hauteur du disque pour redessiner l'axe de la tour
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()  

def dessineConfig(plateau, n):
    # For each tower in the plateau
    for tower_index, tower in enumerate(plateau):
        # For each disk number in each tower
        for disk_number in tower:
            # Call dessineDisque to draw the disk
            dessineDisque(disk_number, plateau, n)
            
def effaceTout(plateau, n):
    # For each tower in the plateau
    for tower_index, tower in enumerate(plateau):
        # For each disk number in each tower
        for disk_number in tower:
            # Call effaceDisque to erase the disk
            effaceDisque(disk_number, plateau, n)
    # After erasing, we might need to redraw the towers if the top disk was erased
    dessinePlateau(n)  # This will redraw the towers over the erased disks





'''Partie C & D'''
def lireCoords(plateau):
    # Ensure the user selects a non-empty start tower
    while True:
        try:
            start_tower = int(input("Enter the number of the start tower (0-2): "))
            if start_tower in [0, 1, 2] and plateau[start_tower]:
                break
            else:
                print("Invalid choice. The start tower must be between 0 and 2 and cannot be empty.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ensure the user selects a valid destination tower
    while True:
        try:
            end_tower = int(input("Enter the number of the destination tower (0-2): "))
            if end_tower in [0, 1, 2]:
                if not plateau[end_tower] or plateau[end_tower][-1] > plateau[start_tower][-1]:
                    break
                else:
                    print("Invalid choice. The destination tower must be empty or have a larger disk.")
            else:
                print("Invalid choice. The destination tower must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return start_tower, end_tower


def jouerUnCoup(plateau, n):
    start_tower, end_tower = lireCoords(plateau)
    
    # Ensure there is a disk to move
    if not plateau[start_tower]:
        print(f"No disks to move from tower {start_tower}")
        return plateau

    disk_to_move = plateau[start_tower][-1]
    
    # Ensure the move is valid
    if plateau[end_tower] and plateau[end_tower][-1] < disk_to_move:
        print(f"Cannot move disk {disk_to_move} to tower {end_tower}, smaller disk present.")
        return plateau
    
    # Move the disk
    effaceDisque(disk_to_move, plateau, n)
    plateau[start_tower].pop()
    plateau[end_tower].append(disk_to_move)
    dessineDisque(disk_to_move, plateau, n)
    
    return plateau

def dernierCoup(coups):
    dernier_numero_coup = max(coups.keys())
    plateau_avant = coups[dernier_numero_coup - 1]
    plateau_apres = coups[dernier_numero_coup]

    for i in range(3):
        if len(plateau_avant[i]) > len(plateau_apres[i]):
            tour_depart = i
        elif len(plateau_avant[i]) < len(plateau_apres[i]):
            tour_arrivee = i

    return tour_depart, tour_arrivee


def annulerDernierCoup(coups, plateau, n):
    if len(coups) <= 1:
        print("Aucun coup précédent à annuler.")
        return plateau, len(coups) - 1

    dernier_numero_coup = max(coups.keys())
    dernier_coup = dernierCoup(coups)

    # Inverser le dernier coup
    if dernier_coup and dernier_numero_coup != 0:
        tour_depart, tour_arrivee = dernier_coup
        disque_a_deplacer = plateau[tour_arrivee].pop()
        plateau[tour_depart].append(disque_a_deplacer)
        
    del coups[dernier_numero_coup]

    # Décrémenter le compteur de coups
    compteur_coup = dernier_numero_coup - 1

    return plateau, compteur_coup



def boucleJeu(plateau, n, max_coups=None):
    compteur = 0
    game_status = 'in_progress'
    coups = {0: [list(tower) for tower in plateau]}  # Historique des coups

    while not verifVictoire(plateau, n):
        if max_coups is not None and compteur >= max_coups:
            game_status = 'lost'
            break

        print(f"\nCoup {compteur + 1} (0 pour annuler le dernier coup) :")
        choix = input("Appuyez sur 'a' pour annuler le dernier coup, ou sur 'Enter' pour continuer : ")

        if choix == 'a':
            if compteur > 0:
                effaceTout(plateau, n)
                plateau, compteur = annulerDernierCoup(coups, plateau, n)
                dessineConfig(plateau, n)
                print(f"Coup annulé. Retour au coup {compteur}.")
                continue
            else:
                print("Aucun coup à annuler.")

        else: 
            plateau = jouerUnCoup(plateau, n)
            compteur += 1
            coups[compteur]=[list(tower) for tower in plateau]

    if verifVictoire(plateau, n):
        game_status = 'won'

    return compteur, game_status

'''PARTIE E'''
def sauvScore(scores, joueur, nb_disques, nb_coups,Temps):
    """
    Enregistre le score d'un joueur dans le dictionnaire 'scores'.
    
    :param scores: Dictionnaire des scores.
    :param joueur: Nom du joueur.
    :param nb_disques: Nombre de disques utilisés dans la partie.
    :param nb_coups: Nombre de coups effectués pour gagner.
    """
    # Si le joueur n'existe pas dans le dictionnaire, créer une nouvelle entrée
    if joueur not in scores:
        scores[joueur] = []

    # Ajouter le score pour la partie actuelle
    score = {'disques': nb_disques, 'coups': nb_coups, 'Temps': Temps}
    scores[joueur].append(score)

def afficheScores(scores):
    """
    Affiche un tableau des meilleurs scores par nombre de disques.
    
    :param scores: Dictionnaire contenant les scores des joueurs.
    """
    # Créer un dictionnaire pour regrouper les scores par nombre de disques
    scores_par_disques = {}

    # Regrouper les scores par nombre de disques
    for joueur, score_list in scores.items():
        for score in score_list:
            nb_disques = score['disques']
            nb_coups = score['coups']
            if nb_disques not in scores_par_disques:
                scores_par_disques[nb_disques] = []
            scores_par_disques[nb_disques].append((joueur, nb_coups))

    # Trier et afficher les scores pour chaque nombre de disques
    for nb_disques, score_list in scores_par_disques.items():
        score_list.sort(key=lambda x: x[1])  # Tri par nombre de coups
        print(f"\nMeilleurs scores pour {nb_disques} disques:")
        for score in score_list:
            print(f"Joueur: {score[0]}, Coups: {score[1]},Temps : {score[2]}")
            
def afficheChronos(scores, nb_disques=None):
    print("Classement en durée de jeu:")
    for joueur, score_list in scores.items():
        for score in sorted(score_list, key=lambda x: x['Temps']):
            if nb_disques is None or score['disques'] == nb_disques:
                duree_min, duree_sec = divmod(score['Temps'], 60)
                print(f"{joueur} - Disques: {score['disques']}, Temps: {int(duree_min)}m {int(duree_sec)}s")

def reflexionMoy(scores, joueur):
    """
    Calcule le temps moyen de réflexion par coup pour un joueur donné.
    
    :param scores: Dictionnaire des scores.
    :param joueur: Nom du joueur.
    :return: Temps moyen de réflexion par coup (en secondes).
    """
    total_temps = 0
    total_coups = 0

    if joueur in scores:
        for partie in scores[joueur]:
            total_temps += partie['Temps']
            total_coups += partie['coups']

        if total_coups > 0:
            temps_moyen = total_temps / total_coups
            return temps_moyen
        else:
            return None
    else:
        return None
def classementReflexion(scores):
    """
    Affiche un classement des joueurs selon leur temps moyen de réflexion par coup.

    :param scores: Dictionnaire des scores.
    """
    reflexion_par_joueur = {}

    for joueur in scores:
        temps_moyen = reflexionMoy(scores, joueur)
        if temps_moyen is not None:
            reflexion_par_joueur[joueur] = temps_moyen

    # Trier les joueurs par temps de réflexion moyen (du plus rapide au plus lent)
    classement = sorted(reflexion_par_joueur.items(), key=lambda x: x[1])

    print("Classement des joueurs (le plus rapide en premier) :")
    for i, (joueur, temps) in enumerate(classement, 1):
        print(f"{i}. {joueur} - Temps moyen par coup: {temps:.2f} secondes")

import time

def afficherMenu():
    print("\nMenu Principal")
    print("1. Jouer une partie")
    print("2. Afficher les scores")
    print("3. Afficher les temps moyens de réflexion")
    print("4. Afficher le classement de rapidité")
    print("5. Afficher la solution")
    print("6. Quitter")
    choix = input("Entrez votre choix : ")
    return choix
'''PARTIE F'''
def hanoi(n, depart, intermediaire, arrivee):
    """
    Résout le problème des tours de Hanoi pour n disques.
    
    :param n: Nombre de disques.
    :param depart: Tour de départ.
    :param intermediaire: Tour intermédiaire.
    :param arrivee: Tour d'arrivée.
    :return: Liste des mouvements (chaque mouvement est un tuple (tour de départ, tour d'arrivée)).
    """
    if n == 1:
        return [(depart, arrivee)]
    else:
        mouvements = []
        # Déplacer n-1 disques de la tour de départ vers la tour intermédiaire
        mouvements += hanoi(n - 1, depart, arrivee, intermediaire)
        # Déplacer le plus grand disque vers la tour d'arrivée
        mouvements += [(depart, arrivee)]
        # Déplacer les n-1 disques de la tour intermédiaire vers la tour d'arrivée
        mouvements += hanoi(n - 1, intermediaire, depart, arrivee)
        return mouvements



def animerDeplacements(deplacements, n):
    # Initialiser le plateau et Turtle
    plateau = init(n)
    dessinePlateau(n)
    dessineConfig(plateau, n)
    
    for depart, arrivee in deplacements:
        disque_a_deplacer = plateau[depart][-1]
        effaceDisque(disque_a_deplacer, plateau, n)
        disque_a_deplacer = plateau[depart].pop()
        plateau[arrivee].append(disque_a_deplacer)
        dessineDisque(disque_a_deplacer, plateau, n)
    effaceTout(plateau, n)
        



def main():
    scores = {}
    while True:
        choix = afficherMenu()

        if choix == '1':

                # Demander le nombre de disques
                while True:
                    try:
                        n = int(input("Enter the number of disks: "))
                        max_moves = int(input("donner le nombre maximal des mouvements: "))
                        if n > 0:
                            break
                        else:
                            print("Please enter a positive integer.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                plateau = init(n)
                dessinePlateau(n)
                dessineConfig(plateau, n)
                # Enregistrez le temps de début
                debut_jeu = time.time()
                moves, status = boucleJeu(plateau, n,max_moves)
                effaceTout(plateau, n)
                min_moves = 2 ** n - 1
                fin_jeu = time.time()
                duree_jeu = fin_jeu - debut_jeu
                duree_min, duree_sec = divmod(duree_jeu, 60)

                if status == 'won':
                    print(f"Congratulations! You've won in {moves} moves. Minimum possible moves: {min_moves}.")
                    print(f"Time taken: {int(duree_min)} minutes and {int(duree_sec)} seconds")
                    joueur = input("Enter your name: ")
                    sauvScore(scores, joueur, n, moves, duree_jeu)  # Inclure duree_jeu dans l'appel
                    print(f"Score saved for {joueur}.")
                elif status in ['lost', 'abandoned']:
                    print(f"Game {status}. Moves made: {moves}, Minimum possible moves: {min_moves}.")
                    print(f"Time taken: {int(duree_min)} minutes and {int(duree_sec)} seconds")
                    deplacements = hanoi(n, 0, 1, 2)
                    animerDeplacements(deplacements, n)    
                # Afficher les scores enregistrés
                print("Current Scores:")
                for joueur, score_list in scores.items():
                    for score in score_list:
                        print(f"{joueur}: Disks: {score['disques']}, Moves: {score['coups']}, Time: {score['Temps']} seconds")

                turtle.reset()
        elif choix == '2':
            # Afficher les scores
            print("Scores des joueurs :")
            for joueur, score_list in scores.items():
                print(f"{joueur}: {score_list}")
        elif choix == '3':
            # Afficher les temps moyens de réflexion
            for joueur in scores:
                temps_moyen = reflexionMoy(scores, joueur)
                if temps_moyen is not None:
                    print(f"{joueur} - Temps moyen par coup: {temps_moyen:.2f} secondes")
        elif choix == '4':
            # Afficher le classement de rapidité
            classementReflexion(scores)
        elif choix == '5':
            n = int(input("Enter the number of disks: "))
            deplacements = hanoi(n, 0, 1, 2)
            animerDeplacements(deplacements, n)
            turtle.reset()
        elif choix == '6':
            print('fin du programme')
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

    turtle.done()
if __name__ == "__main__":
    main()





