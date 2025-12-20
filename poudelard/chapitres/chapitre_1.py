from poudelard.univers.personnage import initialiser_personnage, afficher_personnage
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
        "loyauté": loyaute,
        "ambition": ambition
    }

    joueur = initialiser_personnage(nom, prenom, attributs)

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
    print(f"Hagrid : 'Salut {prenom} ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == "Non":
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui !")
    else:
        print("Vous suivez Hagrid avec enthousiasme vers l'arrière-cour.")



def acheter_forunitures(personnage):
    boutique = load_fichier("../data/inventaire.json")
    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    while len(objets_obligatoires) > 0:
        print("\nCatalogue des objets disponibles :")

        # Affichage en ordre 1..n (les clés sont des strings "1", "2", ...)
        nb_articles = len(boutique)
        num = 1
        while num <= nb_articles:
            cle = str(num)
            article = boutique[cle]          # ["Nom", prix]
            nom_article = article[0]
            prix_article = article[1]
            print(f"{num}. {nom_article} - {prix_article} gallions")
            num += 1

        print(f"\nVous avez {personnage['argent']} gallions.")
        print(f"Objets obligatoires restants à acheter : {', '.join(objets_obligatoires)}")

        # Trouver le prix minimum des objets obligatoires encore restants
        prix_min = None
        num = 1
        while num <= nb_articles:
            cle = str(num)
            nom_article = boutique[cle][0]
            prix_article = boutique[cle][1]

            if nom_article in objets_obligatoires:
                if prix_min is None or prix_article < prix_min:
                    prix_min = prix_article
            num += 1

        # Si on ne trouve aucun objet obligatoire dans la boutique (problème de données)
        if prix_min is None:
            print("Erreur : objets obligatoires introuvables dans la boutique.")
            return

        # Si le joueur ne peut même pas acheter le moins cher obligatoire : stop
        if personnage["argent"] < prix_min:
            print("Vous n'avez plus assez d'argent pour acheter les objets obligatoires.")
            print("Fin des achats.")
            return

        # Choix de l'objet (entre 1 et nb_articles)
        choix = demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, nb_articles)

        article_choisi = boutique[str(choix)]
        nom_choisi = article_choisi[0]
        prix_choisi = article_choisi[1]

        # Vérifier argent
        if personnage["argent"] < prix_choisi:
            print("Vous n'avez pas assez d'argent pour cet objet.")
        else:
            # Empêcher l'achat en double (optionnel mais utile)
            if nom_choisi in personnage["Inventaires"]:
                print("Vous avez déjà cet objet.")
            else:
                personnage["argent"] = personnage["argent"] - prix_choisi
                personnage["Inventaires"].append(nom_choisi)
                print(f"Vous avez acheté : {nom_choisi} ({prix_choisi} gallions).")

                if nom_choisi in objets_obligatoires:
                    objets_obligatoires.remove(nom_choisi)

    print("Vous avez acheté tous les objets obligatoires !")




def lancer_chapitre_1():

    introduction()

    personnage = creer_personnage()

    recevoir_lettre()

    rencontrer_hagrid(personnage)

    acheter_forunitures(personnage)

    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")

    return personnage


lancer_chapitre_1()