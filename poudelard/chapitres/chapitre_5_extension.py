import random
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage


def lancer_chapitre_5_basilic(joueur, maisons):
    print("\n" + "=" * 50)
    print("CHAPITRE 5 : LA CHAMBRE DES SECRETS")
    print("=" * 50)
    print("\nLe Basilic surgit des ombres ! Tu dois choisir une action :")
    print("1. Attaquer avec un sortilège")
    print("2. Esquiver son regard mortel")
    print("3. Utiliser l'épée de Gryffindor")

    choix = input("> ")

    if choix == "3":
        print("\nTu brandis l'épée de Gryffindor et transperces le palais du Basilic !")
        print("Le monstre s'effondre. Tu as sauvé Poudlard !")
        points_victoire = 1000
    elif choix == "1" or choix == "2":
        print("\nGrâce à ton agilité et l'aide du phénix Fumseck, tu terrasses le monstre !")
        points_victoire = 500
    else:
        print("\nDans la panique, tu lances une pierre, mais tu finis par l'emporter de justesse !")
        points_victoire = 200

    joueur["Score"] = points_victoire
    actualiser_points_maison(joueur, maisons)

    print(f"\nL'AVENTURE EST TERMINÉE !")
    print(f"Tu as rapporté {points_victoire} points vitaux à ta maison.")

    print("\n--- CLASSEMENT FINAL ---")
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
