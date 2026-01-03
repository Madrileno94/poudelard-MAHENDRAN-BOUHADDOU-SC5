from utils.input_utils import demander_choix
from chapitre_3 import lancer_chapitre_3

def afficher_menu_principal():
    print("1. Lancer le Chapitre 1 - L'arrivée dans le monde magique.")
    print("2. Quitter le jeu.")


def lancer_choix_menu():
    maisons = load_fichier("data/maisons.json")

    while True:
        afficher_menu_principal()
        choix = input("Votre choix : ")

        if choix == "1":
            personnage = {
                "Prenom": "Harry",
                "Nom": "Potter",
                "Maison": "Gryffondor",
                "Argent": 100,
                "Score": 0,
                "Inventaire": ["Baguette"],
                "Sortilèges": []
            }

            lancer_chapitre_3(personnage, maisons)

        elif choix == "2":
            print("Au revoir, jeune sorcier !")
            break
        else:
            print("Erreur : Choix invalide. Veuillez saisir 1 ou 2.")
