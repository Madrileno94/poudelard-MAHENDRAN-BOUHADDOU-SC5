def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte != "":
            return texte
        else:
            print("Veuillez entrer un texte non vide.")