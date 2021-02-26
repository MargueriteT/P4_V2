from tinydb import TinyDB
from random import *


class Player:

    @classmethod
    def all_players(cls):
        all_players = [Player.__init__()]
        print(all_players)

    def __init__(self, name, initial_score, tournament_score, match_score=[]):
        self.name = name
        self.initial_score = int(initial_score)
        self.tournament_score = tournament_score
        self.match_score = match_score

    def information_about_player(self):
        print("Mon nom est ", self.name, " mon score initial est ", self.initial_score, " et mon score au match est ",
              self.match_score)

    """# class Players function to allow verification of information about each player
    def information_about_players(self):
        global player
        player = {"full_name": self.name, "initial_score": self.initial_score}
        print("Mon nom est", player["full_name"], "et mon score : ", player["initial_score"])

    # Add players to the list
    def __add__(self):
        global player_list
        player_list.append(player)
        print(player_list)
        """

    """# add score
    def score_match(self):
        for player in player_"""


    def score_tournament(self, score_match, tournament_score):
        tournament_score = tournament_score + score_match


class Tournament:
    # creation of object
    def __init__(self, name, player_number, round_number, exit_player, round_name=None, all_rounds_names=[], players=[], sorted_players=[], tournament_score=0,
                 list_of_match={}):
        self.name = name
        self.player_number = int(player_number)
        self.round_number = int(round_number)
        self.exit_player = exit_player
        self.round_name = round_name
        self.all_rounds_names = all_rounds_names
        self.players = players
        self.sorted_players = sorted_players
        self.tournament_score = tournament_score
        self.list_of_match = list_of_match


    # players' list for a tournament
    def list_of_players(self, Player):
        self.players.append({"full_name": Player.name, "initial_score": Player.initial_score})
        #print(self.players)

    # sorted players' list by rank
    def sorted_players_list_beginning(self, sorted_players, players):
        sorted_players.extend(sorted(players, key=lambda k: k["initial_score"], reverse=True))
        print(sorted_players)

    def name_of_the_round(self, round_name):
        self.round_name = input("named the round")
        print(self.round_name)

    # association of two players for the first round and display all match for the round
    def matching_players(self, player, player_number, sorted_players, list_of_match):
        # Divide the sorted list in two in order to match each player of the first list with a player of the
        # second one according to their rank in the lists
        # if number_of_players isn't pair exit one player randomly
        if (player_number % 2) != 0:
            half_player = (player_number - 1) / 2
            exit_player = choice(sorted_players)
            sorted_players.remove(exit_player)
            # if number_of_players is pair
            return exit_player, half_player
            # print(exit_player)
        else:
            half_player = player_number / 2

        # Creation of the two lists
        s1 = sorted_players[0: int(half_player)]
        s2 = sorted_players[int(half_player):]

        # list of all matches of a round

        list_of_match[self.round_name] = []
        for i in range(0, int(player_number / 2)):
            match = [s1[i], s2[i]]
            list_of_match[self.round_name].append(match)
        return list_of_match[self.round_name]
        print(list_of_match[self.round_name])

    def score_of_match(self, players, player_number, list_of_match, exit_player):

        # add point for a round to each player
        players[:] = []
        for match in list_of_match[self.round_name]:
            print(match[0]["full_name"])
            match[0][self.round_name] = input("Entrer le score")
            players.append(match[0])
            print(match[1]["full_name"])
            match[1][self.round_name] = input("Entrer le score")
            players.append(match[1])
        if (player_number % 2) != 0:
            exit_player[self.round_name] = 0
            players.append(exit_player)
        else:
            pass
        for player in players:
            print(player)

    def sort_list_other_round(self, sorted_players, players, round_name):
        sorted_players[:] = []
        sorted_players.extend(sorted(players, key=lambda k: k[self.round_name], reverse=True))
        print(sorted_players)

    def tournament_score(self, players):
        for player in players:
            print(self.tournament_score)






