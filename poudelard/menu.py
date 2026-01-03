from poudelard.chapitres.chapitre_2 import lancer_chapitre_2
from utils.input_utils import load_fichier
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch
from chapitres.chapitre_1 import lancer_chapitre_1

from chapitres.chapitre_5_extension import lancer_chapitre_5_basilic


def afficher_menu_principal():
    print("\n1. Lancer l'aventure Poudlard (Chapitres 3, 4 et 5)")
    print("2. Quitter le jeu.")



def lancer_choix_menu():

    maisons = load_fichier("data/maisons.json")

    while True:
        afficher_menu_principal()
        choix = input("Votre choix : ")

        if choix == "1":

            personnage =lancer_chapitre_1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage, maisons)
            lancer_chapitre4_quidditch(personnage, maisons)
            lancer_chapitre_5_basilic(personnage, maisons)

            print("\nBravo ! Tu as terminé toute l'aventure !")

        elif choix == "2":
            print("Au revoir, jeune sorcier !")
            break
        else:
            print("Erreur : Choix invalide. Veuillez saisir 1 ou 2.")