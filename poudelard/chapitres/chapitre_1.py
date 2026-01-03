from poudelard.univers.personnage import initialiser_personnage, afficher_personnage, ajouter_objet, modifier_argent
from poudelard.utils.input_utils import demander_texte, demander_nombre, load_fichier, demander_choix


def introduction():
    print("Bienvenue à Poudlard !")
    print("Ton aventure commence ici.")
    print("Prépare-toi à vivre une aventure pleine de découvertes,")
    print("ainsi que de choix importants et de mystères à percer !")


def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("Choisissez vos attributs :")

    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_nombre("Niveau d’intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d’ambition (1-10) : ", 1, 10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyaute": loyaute,
        "ambition": ambition
    }

    joueur = initialiser_personnage(nom, prenom, attributs)
    joueur["Attributs"] = attributs
    joueur["attributs"] = attributs

    afficher_personnage(joueur)

    return joueur


def recevoir_lettre():
    print("bonjour cher sorcier, vous avez été accepté a poudelard, fellicitation !")
    print("souhaiter vous accepter cette invitation a poudelard ")

    choix=demander_nombre("taper 1 pour oui et 2 pour non",1,2)
    if choix ==1:
        print("oui bien sur")
    if choix ==2:
        print("Vous déchirez la lettre, l’oncle Vernon pousse un cri de joie: EXCELLENT  Enfin quelqu’un de NORMAL dans cette maison Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit()

def rencontrer_hagrid(personnage):
    prenom = personnage["Prenom"]
    print(f"\nHagrid : 'Salut {prenom} ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == "Non":
        print("\nHagrid insiste gentiment et vous entraîne quand même avec lui !")
    else:
        print("\nVous suivez Hagrid avec enthousiasme vers l'arrière-cour.")


def acheter_fournitures(personnage):
    boutique = load_fichier("data/inventaire.json")

    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    while len(objets_obligatoires) > 0:
        print("\nCatalogue des objets disponibles :")
        cles = list(boutique.keys())

        i = 0
        while i < len(cles):
            cle = cles[i]                 # "1", "2", ...
            nom_objet = boutique[cle][0]  # ex: "Baguette magique"
            prix = boutique[cle][1]       # ex: 35
            print(f"{i + 1}. {nom_objet} - {prix} gallions")
            i += 1

        print(f"\nVous avez {personnage['argent']} gallions.")
        print("Objets obligatoires restants à acheter :", ", ".join(objets_obligatoires))

        choix = demander_nombre(
            "Entrez le numéro de l'objet à acheter : ",
            1,
            len(cles)
        )

        cle_choisie = cles[choix - 1]
        nom_objet = boutique[cle_choisie][0]
        prix = boutique[cle_choisie][1]

        if personnage["argent"] < prix:
            print("Vous n'avez pas assez d'argent. Fin du jeu.")
            exit()

        ajouter_objet(personnage, "Inventaires", nom_objet)
        modifier_argent(personnage, -prix)
        print(f"Vous avez acheté : {nom_objet} (-{prix} gallions).")

        if nom_objet in objets_obligatoires:
            objets_obligatoires.remove(nom_objet)

    print("\nTous les objets obligatoires ont été achetés avec succès !")





def lancer_chapitre_1():

    introduction()

    personnage = creer_personnage()

    recevoir_lettre()

    rencontrer_hagrid(personnage)

    acheter_fournitures(personnage)

    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    return personnage
