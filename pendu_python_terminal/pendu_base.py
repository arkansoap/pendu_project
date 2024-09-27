"""Jeu du pendu
règles: 8 tentatives

python pendu/pendu_base.py

"""
import draw_pendu
import random
from larousse_api import larousse

# TODO rajouter la possibilité de faire une propoition entière à la place d'une seule lettre
# TODO système de point en fonction de la difficulté du mot et de du nb d'essais
# TODO enlever les accents du mots (ou pas) niveau de difficulté (avec ou sans accents)
# TODO niveau difficulté (nb tentatives) params du jeu
# TODO maj du print de la console pour effacer lignes du dessus
# TODO interface graphique pygame
# TODO mot composé (tiret en diffficulté / paramètre)
# TODO controle entree utilisateur (seulement lettre...)
# TODO pb carac spéciaux non identifiés


class Param_exception(Exception):
    message = "merci de rentrer un nombre de tentative valide"


class Mot:
    def __init__(self):
        # TODO version sans accent du mot, select mot sans mot composé ou espace si mot composé
        self.mot_str = self.selection_mot()
        self.len_mot = len(self.mot)
        self.diff_mot()
        # self.choix_caracSpeciaux = ...
        # self.mot_composés = ...
        # self.mot_easyVersion = ...

    def selection_mot(self):
        with open("liste.de.mots.francais.frgut.txt", encoding="utf-8") as file:
            liste_mot = file.readlines()
        self.mot = random.choice(liste_mot).strip("\n")
        return self.mot

    def diff_mot(self):
        # TODO fonction du nb de tentatives, de la longueur du mot, des carac spéciaux, du nb de lettres différentes dans le mot ...
        if len(self.mot_str) > 6:
            diff_len_mot = 2
        else:
            diff_len_mot = 1
        self.coeff_diff_mot = diff_len_mot


class Game_params:
    def __init__(self, mot: Mot, player_name: str):
        self.mot = mot
        self.define_tentatives()
        self.player_name = player_name
        self.get_coeff_game()

    def define_tentatives(self):
        self.nb_tentatives = int(input("nb de tentatives: "))
        try:
            if self.nb_tentatives == 8:
                self.draw = draw_pendu.liste_draw
            else:
                raise Param_exception
        except Param_exception as p:
            print(p.message)
            self.define_tentatives()
        return self.nb_tentatives, self.draw

    def get_coeff_game(self):
        self.coeff_game = (10 / self.nb_tentatives) + (self.mot.coeff_diff_mot)


class Pendu:
    def __init__(self):
        self.mot = Mot()
        self.etat = self.mot.len_mot * "*"
        self.nb_erreur = 0

    @staticmethod
    def get_definition(mot):
        liste_def = larousse.get_definitions(mot)
        print("\nDéfinition:\n")
        for definition in liste_def:
            print(f"\n {definition}\n")

    def replace_lettre_in_guess(self, lettre_proposee):
        position = 0
        etat_liste = list(self.etat)
        for lettre in self.mot.mot_str:
            if lettre_proposee == lettre:
                etat_liste[position] = lettre_proposee
            position += 1
        self.etat = "".join(etat_liste)
        print(f"\n______________\n\n{self.etat}\n______________")
        return self.etat

    def affiche_pendu(self, params: Game_params):
        print(params.draw[self.nb_erreur])
        print(f"\n______________\n\n{self.etat}\n______________")

    def check_lettre(self, lettre_proposee, params: Game_params):
        if lettre_proposee in self.etat:
            print("\nProposition déja faite\n")
        elif lettre_proposee in self.mot.mot_str:
            self.replace_lettre_in_guess(lettre_proposee)
        elif lettre_proposee not in self.mot.mot_str:
            self.affiche_pendu(params)
            self.nb_erreur += 1

    def main(self, params: Game_params):
        jeu = True
        while jeu:
            lettre_proposee = input("\nentrer une lettre: ")
            self.check_lettre(lettre_proposee, params)
            if self.nb_erreur == params.nb_tentatives:
                print(f"\n Le mot était: {self.mot.mot_str}")
                self.get_definition(self.mot.mot_str)
                print(
                    "\n******************\n\nVous avez perdu !!\n\n******************\n\n"
                )
                jeu = False
            if self.etat == self.mot.mot_str:
                print(f"\n!!!!!! {self.mot.mot_str} !!!!!!\n")
                self.get_definition(self.mot.mot_str)
                print(
                    "\n******************\n\nVous avez gagné !!\n\n******************\n\n"
                )
                jeu = False


class Score:
    def __init__(self, pendu: Pendu, params: Game_params):
        # TODO load best_score & playerScore from json file
        # self.bestscore:dict = ...
        # self.player_scores = ...
        # TODO depend de nb_erreur parties
        self.params = params
        self.pendu = pendu

    def calcul_score(self):
        self.score = self.params.coeff_game * (
            self.params.nb_tentatives - self.pendu.nb_erreur
        )
        return self.score


if __name__ == "__main__":
    pendu = Pendu()
    player_name = input("player name = ")
    game_params = Game_params(mot=pendu.mot, player_name=player_name)
    pendu.main(game_params)
    score = Score(pendu, game_params)
    print(f"{game_params.player_name} score = {score.calcul_score()}")

    # print(game_params.draw[1])
    # print(pendu.mot.mot_str)
    # print(pendu.mot.len_mot)
    # print(pendu.etat)
