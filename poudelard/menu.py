from poudelard.chapitres.chapitre_2 import lancer_chapitre_2
from poudelard.utils.input_utils import demander_nombre


def afficher_menu_principal():
    print("=== MENU PRINCIPAL ===")
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu")

def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    en_cours = True

    while en_cours:

        afficher_menu_principal()

        choix = demander_nombre("Votre choix : ", 1, 2)

        if choix == 1:
            personnage = lancer_chapitre_1()
            lancer_chapitre_2(personnage)

            print("🎉 Fin de l’aventure ! Merci d’avoir joué.")
            en_cours = False
        elif choix == 2:
            print("Au revoir, jeune sorcier. À très bientôt à Poudlard !")
            en_cours = False
