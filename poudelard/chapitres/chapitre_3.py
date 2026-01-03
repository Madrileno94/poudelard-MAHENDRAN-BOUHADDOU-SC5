import random

from poudelard.utils.input_utils import load_fichier
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage


def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    print("Tu commences tes cours de magie à Poudlard...\n")
    tous_les_sorts = load_fichier(chemin_fichier)

    s_off = [s for s in tous_les_sorts if s["type"].lower() == "offensif"]
    s_def = [s for s in tous_les_sorts if s["type"].lower() == "défensif"]
    s_uti = [s for s in tous_les_sorts if s["type"].lower() == "utilitaire"]

    choisis = []

    if len(s_off) > 0:
        choisis.append(random.choice(s_off))
    if len(s_def) > 0:
        sort_def = random.choice(s_def)
        if sort_def not in choisis:
            choisis.append(sort_def)

    while len(choisis) < 5 and len(s_uti) > 0:
        sort_pioche = random.choice(s_uti)
        if sort_pioche not in choisis:
            choisis.append(sort_pioche)

    if "Sortilèges" not in joueur:
        joueur["Sortilèges"] = []

    for s in choisis:
        joueur["Sortilèges"].append(s["nom"])
        print(f"Tu viens d'apprendre le sortilège : {s['nom']} ({s['type']})")
        input("Appuie sur Entrée pour continuer...")

    print("\nTu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :\n")

    for s in choisis:
        print(f"- {s['nom']} ({s['type']}) : {s['description']}")


def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    print("\nBienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")

    questions_data = load_fichier(chemin_fichier)
    questions_choisies = []

    while len(questions_choisies) < 4 and len(questions_choisies) < len(questions_data):
        q = random.choice(questions_data)
        if q not in questions_choisies:
            questions_choisies.append(q)

    score_quiz = 0

    for i in range(len(questions_choisies)):
        q = questions_choisies[i]
        print(f"{i + 1}. {q['question']}")

        reponse_joueur = input("> ").strip()

        if reponse_joueur.lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score_quiz = score_quiz + 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}")

        print()

    print(f"Score obtenu : {score_quiz} points")
    if "Score" not in joueur:
        joueur["Score"] = 0
    joueur["Score"] = joueur["Score"] + score_quiz


def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)

    points_gagnes = quiz_magie(personnage)

    if "Maison" in personnage:
        actualiser_points_maison(maisons, personnage["Maison"], points_gagnes)
    else:
        print("Erreur : aucune maison n'est définie pour ce personnage, impossible d'ajouter des points.")

    afficher_maison_gagnante(maisons)

    print("\nRésumé du personnage en fin de Chapitre 3 :")
    afficher_personnage(personnage)

    print("Fin du Chapitre 3 ! Les défis de Poudlard ne font que commencer...\n")
    return personnage









