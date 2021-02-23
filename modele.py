from tinydb import TinyDB
from random import *


class Tournament():
    def __init__(self, name, player_number, round_number):
        self.name = name
        self.player_number = int(player_number)
        self.round_number = int(round_number)

    def player_ranking(self):
        global sorted_players_list
        sorted_players_list = sorted(player_list, key=lambda k: k["initial_score"], reverse=True)
        print(sorted_players_list)

    def matching_first_round(self, player_number):
        # associer les joueurs par paires en fonction de leur classement dans les deux listes obtenues à
        # partir de my_list

        # if number_of_players is pair
        if (player_number % 2) != 0:
            half_player = (player_number - 1) / 2
            exit_player = choice(sorted_players_list)
            sorted_players_list.remove(exit_player)
        else:
            half_player = player_number / 2


        s1 = sorted_players_list[0: int(half_player)]
        s2 = sorted_players_list[int(half_player):]

        list_of_match = []

        for i in range(0, int(player_number / 2)):
            match = (s1[i], s2[i])
            list_of_match.append(match)

        for i in range(0, int(player_number / 2)):
            s1[i].update({"score_match": input("Entrer le score ")})
            s2[i].update({"score_match": input("entrer score")})
            print(s1[i], s2[i])

        if (player_number % 2) != 0:
            # take back the excluded player
            sorted_players_list.append(exit_player)
        else:
            pass


    def add_score_match(self, score_match):
        Player.match_score.append(score_match)
        for i in Player:
            print(i)

player_list = []
player = {}


class Player:
    def __init__(self, name, initial_score, tournament_score, match_score):
        self.name = name
        self.initial_score = int(initial_score)
        self.tournament_score = tournament_score
        self.match_score = match_score

    # class Players function to allow verification of information about each player
    def information_about_players(self):
        global player
        player = {"full_name": self.name, "initial_score": self.initial_score}
        print("Mon nom est", player["full_name"], "et mon score : ", player["initial_score"])

    # Add players to the list
    def __add__(self):
        global player_list
        player_list.append(player)
        print(player_list)

    """# add score
    def score_match(self):
        for player in player_"""

    def score_tournament(self, score_match, tournament_score):
        tournament_score = tournament_score + score_match