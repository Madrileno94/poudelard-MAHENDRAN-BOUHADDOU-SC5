import random
from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": equipe_data
    }

    if est_joueur and joueur:
        nom_complet = f"{joueur['Prenom']} {joueur['Nom']}"
        nouvelle_liste = [f"{nom_complet} (Attrapeur)"]

        for j in equipe_data:
            if nom_complet not in j:
                nouvelle_liste.append(j)

        equipe["joueurs"] = nouvelle_liste

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur == True:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1

        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")

    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")

def apparition_vifdor():
    nombre = random.randint(1, 6)
    if nombre == 6:
        return True
    else:
        return False


def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])

    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True

    return gagnant


def afficher_score(e1, e2):

    print("\nScore actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")


def afficher_equipe(equipe):
    print(f"Équipe de {equipe['nom']} :")
    for joueur in equipe['joueurs']:
        print(f"- {joueur}")


def match_quidditch(joueur, maisons):
    data_equipes = load_fichier("data/equipes_quidditch.json")
    maison_joueur = joueur["Maison"]
    adversaires_possibles = [m["Nom"] for m in maisons if m["Nom"] != maison_joueur]
    maison_adverse = random.choice(adversaires_possibles)

    equipe_j = creer_equipe(maison_joueur, data_equipes[maison_joueur], True, joueur)
    equipe_adv = creer_equipe(maison_adverse, data_equipes[maison_adverse], False)

    print(f"Match de Quidditch : {equipe_j['nom']} vs {equipe_adv['nom']} !")
    afficher_equipe(equipe_j)
    afficher_equipe(equipe_adv)

    print(f"Tu joues pour {equipe_j['nom']} en tant qu’Attrapeur")

    match_fini = False
    for tour in range(1, 21):
        if match_fini:
            break

        print(f"━━━ Tour {tour} ━━━")
        tentative_marque(equipe_j, equipe_adv, True)
        tentative_marque(equipe_adv, equipe_j, False)
        afficher_score(equipe_j, equipe_adv)

        if apparition_vifdor():
            gagnant_vif = attraper_vifdor(equipe_j, equipe_adv)
            print(f"Le Vif d’Or a été attrapé par {gagnant_vif['nom']} ! (+150 points)")
            print("Fin du match !")
            afficher_score(equipe_j, equipe_adv)
            match_fini = True
        else:
            input("Appuyez sur Entrée pour continuer")

    print("\nRésultat final :")
    if equipe_j["attrape_vifdor"]:
        print(f"Le Vif d’Or a été attrapé par {equipe_j['nom']} !")
        print(f"+150 points pour {equipe_j['nom']} !")
    elif equipe_adv["attrape_vifdor"]:
        print(f"Le Vif d’Or a été attrapé par {equipe_adv['nom']} !")
        print(f"+150 points pour {equipe_adv['nom']} !")

    if equipe_j["score"] > equipe_adv["score"]:
        nom_vainqueur = equipe_j["nom"]
        score_vainqueur = equipe_j["score"]
        print(f"La maison gagnante est {nom_vainqueur} avec {score_vainqueur} points !")
        print(f"{nom_vainqueur} remporte le match !")
    elif equipe_adv["score"] > equipe_j["score"]:
        nom_vainqueur = equipe_adv["nom"]
        score_vainqueur = equipe_adv["score"]
        print(f"La maison gagnante est {nom_vainqueur} avec {score_vainqueur} points !")
        print(f"{nom_vainqueur} remporte le match...")
    else:
        print("Match nul !")
        return

    points_totaux = score_vainqueur + 500
    print(f"+500 points pour {nom_vainqueur} ! Total : {points_totaux} points.")

    if nom_vainqueur == joueur["Maison"]:
        joueur["Score"] = points_totaux
        actualiser_points_maison(joueur, maisons)
    else:
        for m in maisons:
            if m["Nom"] == nom_vainqueur:
                m["Points"] += points_totaux

    for m in maisons:
        if m["Nom"] == nom_vainqueur:
            print(f"La maison gagnante est {m['Nom']} avec {m['Points']} points !")


def lancer_chapitre4_quidditch(joueur, maisons):

    print("CHAPITRE 4 : LA FINALE DE QUIDDITCH")

    match_quidditch(joueur, maisons)

    print("\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !")

    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)