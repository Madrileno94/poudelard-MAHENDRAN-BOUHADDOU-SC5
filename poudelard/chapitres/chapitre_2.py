
from poudelard.univers import personnage
from poudelard.univers.maison import repartition_maison
from poudelard.univers.personnage import afficher_personnage
from poudelard.utils.input_utils import demander_nombre, load_fichier


def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en")
    print("direction du Nord...")
    print()

    # Raccourci vers les attributs
    attributs = joueur["attributs"]

    # --- Rencontre avec Ron ---
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie")
    print("ensemble ?")
    print("Que répondez-vous ?")
    print("1. Bien sûr, assieds-toi !")
    print("2. Désolé, je préfère voyager seul.")
    choix = demander_nombre("Votre choix : ", 1, 2)

    if choix == 1:
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c’est incroyable !")
        attributs["loyauté"] = attributs["loyauté"] + 1
    else:
        print("Ron hausse les épaules : — Pas de souci... Peut-être plus tard !")
        attributs["ambition"] = attributs["ambition"] + 1

    print()

    # --- Rencontre avec Hermione ---
    print("Une fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire")
    print("de la Magie’ ?")
    print("Que répondez-vous ?")
    print("1. Oui, j’adore apprendre de nouvelles choses !")
    print("2. Euh… non, je préfère les aventures aux bouquins.")
    choix = demander_nombre("Votre choix : ", 1, 2)

    if choix == 1:
        print("Hermione sourit : — Enfin quelqu’un qui prend les choses au sérieux !")
        attributs["intelligence"] = attributs["intelligence"] + 1
    else:
        print("Hermione fronce les sourcils : — Il faudrait pourtant s’y mettre un")
        print("jour !")
        attributs["courage"] = attributs["courage"] + 1

    print()

    # --- Rencontre avec Drago ---
    print("Puis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le")
    print("départ, tu ne crois pas ?")
    print("Comment réagissez-vous ?")
    print("1. Je lui serre la main poliment.")
    print("2. Je l’ignore complètement.")
    print("3. Je lui réponds avec arrogance.")
    choix = demander_nombre("Votre choix : ", 1, 3)

    if choix == 1:
        print("Drago esquisse un sourire satisfait. — Au moins, toi, tu as des manières.")
        attributs["ambition"] = attributs["ambition"] + 1
    elif choix == 2:
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
        attributs["loyauté"] = attributs["loyauté"] + 1
    else:
        print("Drago plisse les yeux. — Très courageux… ou très idiot.")
        attributs["courage"] = attributs["courage"] + 1

    print()
    print("Le train continue sa route. Le château de Poudlard se profile à")
    print("l’horizon...")
    print("Tes choix semblent déjà en dire long sur ta personnalité !")
    print(f"Tes attributs mis à jour : {attributs}")

    def mot_de_bienvenue():
        print("Le professeur Dumbledore se lève et observe la Grande Salle.")
        print("— Bienvenue à Poudlard, jeunes sorciers et sorcières.")
        print("Cette école sera désormais votre maison,")
        print("où vous apprendrez, grandirez et forgerez votre destin.")
        print("Que cette année soit riche en découvertes et en magie !")
        print()
        input("Appuyez sur Entrée pour continuer...")

def mot_de_bienvenue():
    print("Le professeur Dumbledore se lève et observe la Grande Salle.")
    print("— Bienvenue à Poudlard, jeunes sorciers et sorcières.")
    print("Cette école sera désormais votre maison,")
    print("où vous apprendrez, grandirez et forgerez votre destin.")
    print("Que cette année soit riche en découvertes et en magie !")
    print()
    input("Appuyez sur Entrée pour continuer...")


def ceremonie_repartition(joueur):
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    print("La cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions :")
    print()

    maison = repartition_maison(joueur, questions)

    # Mise à jour du champ "Maison" du joueur
    joueur["Maison"] = maison

    print(f"Le Choixpeau s’exclame : {maison} !!!")
    print(f"Tu rejoins les élèves de {maison} sous les acclamations")


def installation_salle_commune(joueur):
    # Charger les informations des maisons
    maisons = load_fichier("../data/maisons.json")

    maison_joueur = joueur["Maison"]

    # Sécurité : vérifier que la maison existe dans le JSON
    if maison_joueur not in maisons:
        print("Erreur : maison inconnue.")
        return

    infos = maisons[maison_joueur]

    print("Vous suivez les préfets à travers les couloirs du château...")
    print()

    # Emoji + description
    print(f"{infos['emoji']} {infos['description']}")
    print()

    # Message d'accueil
    print(infos["message_installation"])
    print()

    # Couleurs
    couleurs = ", ".join(infos["couleurs"])
    print(f"Les couleurs de votre maison : {couleurs}")

    print()

    # Bonus d'attributs (si présents)
    bonus = infos.get("bonus_attributs", {})
    attributs = joueur["attributs"]

    for cle in bonus:
        if cle in attributs:
            attributs[cle] = attributs[cle] + bonus[cle]

    # Affichage des attributs après bonus
    print("Vos attributs après installation dans la maison :")
    print(attributs)


def lancer_chapitre_2(personnage):
    # 1) Rencontre avec Ron, Hermione et Drago
    rencontrer_amis(personnage)

    # 2) Message de bienvenue de Dumbledore
    mot_de_bienvenue()

    # 3) Cérémonie de répartition
    ceremonie_repartition(personnage)

    # 4) Installation dans la salle commune
    installation_salle_commune(personnage)

    # 5) Affichage du personnage (résumé de fin de chapitre)
    afficher_personnage(personnage)

    # 6) Fin du chapitre
    print("Fin du Chapitre 2 ! Les cours commencent à Poudlard...")




lancer_chapitre_2(personnage)


