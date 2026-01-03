def initialiser_personnage(nom,prenom,attributs):
    joueur={
        "nom":nom,
        "Prenom":prenom,
        "argent":100,
        "Inventaires":[],
        "attributs": attributs
    }
    return joueur
def afficher_personnage(joueur):
    print("Profil du personnage :")

    for cle in joueur:
        valeur = joueur[cle]

        if type(valeur) == dict:
            print(f"{cle} :")
            for sous_cle in valeur:
                print(f" - {sous_cle} : {valeur[sous_cle]}")

        elif type(valeur) == list:
            if len(valeur) == 0:
                print(f"{cle} :")
            else:
                elements = ", ".join(str(x) for x in valeur)
                print(f"{cle} : {elements}")

        else:
            print(f"{cle} : {valeur}")

def modifier_argent(joueur, montant):
    joueur["argent"] = joueur["argent"] + montant

def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)






