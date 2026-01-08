from poudelard.utils.input_utils import demander_nombre


def actualiser_points_maison(maisons, nom_maison, points):
    if points is None:
        points = 0

    if nom_maison not in maisons:
        print("Maison introuvable.")
        return

    if type(maisons[nom_maison]) == int:
        maisons[nom_maison] = maisons[nom_maison] + points
        print(f"{nom_maison} gagne {points} points. Nouveau total : {maisons[nom_maison]}")
        return

    if type(maisons[nom_maison]) == dict:
        if "points" in maisons[nom_maison]:
            maisons[nom_maison]["points"] = maisons[nom_maison]["points"] + points
            total = maisons[nom_maison]["points"]

        else:
            print("Format de maison inconnu.")
            return

        print(f"{nom_maison} gagne {points} points. Nouveau total : {total}")


def afficher_maison_gagnante(maisons):
    print(maisons)
    score_max = None

    for nom_maison in maisons:
        valeur = maisons[nom_maison]


        if "points" in valeur:
            score = valeur["points"]

        else:
            score = 0


        if score_max is None or score > score_max:
            score_max = score

    gagnantes = []
    for nom_maison in maisons:
        valeur = maisons[nom_maison]


        if "points" in valeur:
                score = valeur["points"]

        else:
            score = 0


        if score == score_max:
            gagnantes.append(nom_maison)

    if len(gagnantes) == 1:
        print("La maison gagnante est", gagnantes[0], "avec", score_max, "points !")
    else:
        print("Égalité entre les maisons suivantes avec", score_max, "points :")
        for m in gagnantes:
            print("-", m)



def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attributs = joueur["Attributs"]

    scores["Gryffondor"] += attributs["courage"] * 2
    scores["Serpentard"] += attributs["ambition"] * 2
    scores["Poufsouffle"] += attributs["loyaute"] * 2
    scores["Serdaigle"] += attributs["intelligence"] * 2

    for question, choix_possibles, maisons_associees in questions:
        print(question)

        i = 0
        while i < len(choix_possibles):
            print(f"{i + 1}. {choix_possibles[i]}")
            i += 1

        choix = demander_nombre("Ton choix : ", 1, len(choix_possibles))
        maison = maisons_associees[choix - 1]
        scores[maison] += 3
        print()

    maison_gagnante = None
    score_max = None

    for maison in scores:
        if score_max is None or scores[maison] > score_max:
            score_max = scores[maison]
            maison_gagnante = maison

    print("Résumé des scores :")
    for maison in scores:
        print(f"{maison} : {scores[maison]} points")
    print()

    return maison_gagnante
