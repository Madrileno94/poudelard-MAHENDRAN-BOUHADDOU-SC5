def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte != "":
            return texte
        else:
            print("Veuillez entrer un texte non vide.")

def demander_nombre(message, min_val=None, max_val=None):
    valide = False
    while not valide:
        saisie = input(message).strip()
        valide = True
        if saisie == "":
            print("Veuillez entrer un nombre entier valide.")
            valide = False
        else:
            negatif = False
            start = 0

            if saisie[0] == "-":
                negatif = True
                start = 1

                if len(saisie) == 1:
                    print("Veuillez entrer un nombre entier valide.")
                    valide = False

            if valide:
                for c in saisie[start:]:
                    if c < '0' or c > '9':
                        print("Veuillez entrer un nombre entier valide.")
                        valide = False

            if valide:
                nombre = int(saisie)


                if min_val is not None and nombre < min_val:
                    print(f"Veuillez entrer un nombre ≥ {min_val}.")
                    valide = False


                if max_val is not None and nombre > max_val:
                    print(f"Veuillez entrer un nombre ≤ {max_val}.")
                    valide = False

    return nombre

def demander_choix(message, options):
    print(message)
    numero = 1
    for opt in options:
        print(f"{numero}. {opt}")
        numero += 1

    total_options = len(options)
    choix_valide = False

    while not choix_valide:
        choix = demander_nombre("Votre choix : ", 1, total_options)
        choix_valide = True

    return options[choix-1]

import json

def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)
    return donnees






