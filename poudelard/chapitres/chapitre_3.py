import random
from utils.input_utils import load_fichier

def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    print("Tu commences tes cours de magie à Poudlard...\n")
    tous_les_sorts = load_fichier(chemin_fichier)

    s_off = [s for s in tous_les_sorts if s["type"].lower() == "offensif"]
    s_def = [s for s in tous_les_sorts if s["type"].lower() == "défensif"]
    s_uti = [s for s in tous_les_sorts if s["type"].lower() == "utilitaire"]

    choisis = []

    choisis.append(random.choice(s_off))
    choisis.append(random.choice(s_def))

    while len(choisis) < 5:
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
    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")

    questions_data = load_fichier(chemin_fichier)
    questions_choisies = []

    while len(questions_choisies) < 4:
        q = random.choice(questions_data)
        if q not in questions_choisies:
            questions_choisies.append(q)

    score_quiz = 0

    for i in range(len(questions_choisies)):
        q = questions_choisies[i]
        print(f"{i + 1}. {q['question']}")

        reponse_joueur = input("> ")

        if reponse_joueur.lower() == q['reponse'].lower():
            print("Bonne réponse ! +25 points pour ta maison.")
            score_quiz += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}")

    print(f"Score obtenu : {score_quiz} points")

    if "Score" not in joueur:
        joueur["Score"] = 0
    joueur["Score"] += score_quiz

from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage

def lancer_chapitre_3(personnage, maisons):
    apprendre_sorts(personnage)
    quiz_magie(personnage)
    actualiser_points_maison(personnage, maisons)
    afficher_maison_gagnante(maisons)
    afficher_personnage(personnage)








