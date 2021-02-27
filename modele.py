from tinydb import TinyDB
from random import *


class Player:
    """ function to complete for a new player to be record in the list while a player already record isn't
    @classmethod
    def all_players(cls):
        all_players = [Player.__init__()]
        print(all_players)"""

    # function to create class instance
    def __init__(self, first_name, last_name, initial_score):
        self.first_name = first_name
        self.last_name = last_name
        self.initial_score = int(initial_score)

    """def information_about_player(self):
        print("Mon nom est ", self.name, " mon score initial est ", self.initial_score)"""


class Tournament(Player):
    # creation of instance Tournament
    def __init__(self, name, player_number, round_number, exit_player, round_name=[], players=[],
                 sorted_players=[], list_of_match={}, total_score_of_tournament=0):
        self.name = name
        self.player_number = int(player_number)
        self.round_number = int(round_number)
        self.exit_player = exit_player
        self.round_name = round_name
        self.players = players
        self.sorted_players = sorted_players
        self.list_of_match = list_of_match
        Player.total_score_of_tournament = total_score_of_tournament

    # players' list for a tournament filled with the players who participates to the tournament
    def list_of_players(self, Player):
        self.players.append({"full_name": Player.first_name + Player.last_name,
                             "score initial": Player.initial_score})

    # sorted players' list by : players are classify with their initial score
    def sorted_players_list_beginning(self):
        self.sorted_players.extend(sorted(self.players, key=lambda k: k["score initial"], reverse=True))
        # print(sorted_players)

    # record the name of each round of the tournament in a list
    def name_of_the_round(self):
        self.round_name.append(input("named the round"))
        # print(self.round_name)

    # this function create pair of player (a pair = one match)
    def matching_players(self):
        # two possibilities : player number is pair or not
        if (self.player_number % 2) != 0:  # if number_of_players isn't pair exit one player randomly
            half_player = (self.player_number - 1) / 2
            self.exit_player = choice(self.sorted_players)
            self.sorted_players.remove(self.exit_player)
            return self.exit_player, half_player
            # print(exit_player)
        else:  # if player' number is pair
            half_player = self.player_number / 2

        # sorted list is divide in two lists s1 and s2
        s1 = self.sorted_players[0: int(half_player)]
        s2 = self.sorted_players[int(half_player):]

        # all matches of a round record in the same list, list_of_match allow to access matches of each round
        self.list_of_match[self.round_name[len(self.round_name) - 1]] = []
        if len(self.round_name) == 1:  # If first round then just need to pair players
            for i in range(0, int(half_player)):
                match = [s1[i], s2[i]]  # take players of each list to pair them by rank in the list
                self.list_of_match[self.round_name[0]].append(match)
            # print(list_of_match[self.round_name[0]])
            return self.list_of_match[self.round_name[0]]

        else:  # if it's not the first round, need to pair players and to verify that they don't already play together
            i = 0
            while i < int(half_player):  # as long as there is still players to match
                match = [s1[i], s2[i]]
                # if match between to players already happen then need to pair with next player :
                if match in self.list_of_match[self.round_name[(len(self.round_name)) - 2]]:
                    match1 = [s1[i], s2[i + 1]]
                    self.list_of_match[self.round_name[len(self.round_name) - 1]].append(match1)
                    match2 = [s1[i + 1], s2[i]]
                    self.list_of_match[self.round_name[len(self.round_name) - 1]].append(match2)
                    if i + 1 == int(half_player) - 1:  # if there is no player left then stop the matching
                        break
                    else:  # if there is still player then switched to next players unpaired
                        i = i + 2
                #  if match never happen, directly record it in the list
                else:
                    self.list_of_match[self.round_name[len(self.round_name) - 1]].append(match)

        # print(list_of_match[self.round_name[len(self.round_name) - 1]])
        return self.list_of_match[self.round_name[len(self.round_name) - 1]]

    def score_of_match(self):
        # add point for a round to each player
        # empty the list of players to fill it again with the score of the last round added
        self.players[:] = []
        # for each match record in the list of match of the round
        for match in self.list_of_match[self.round_name[len(self.round_name) - 1]]:
            # add point to first player of a match
            print(match[0]["full_name"])
            match[0][self.round_name[len(self.round_name) - 1]] = float(input("Entrer le score"))
            # Add the point of the round to total score
            if len(self.round_name) > 1:  # in case it's not the first round : add point to the total
                match[0]["total_score_of_tournament"] = match[0]["total_score_of_tournament"] + \
                                                        match[0][self.round_name[len(self.round_name) - 1]]
            else:  # in case this is the first create the key and add point of first round
                match[0]["total_score_of_tournament"] = match[0][self.round_name[len(self.round_name) - 1]]
            # add back the player to the list
            self.players.append(match[0])

            # add point to the second player of the match
            print(match[1]["full_name"])
            match[1][self.round_name[len(self.round_name) - 1]] = float(input("Entrer le score"))
            # Add the point of the round to total score
            if len(self.round_name) > 1:   # in case it's not the first round : add point to the total
                match[1]["total_score_of_tournament"] = match[1]["total_score_of_tournament"] + \
                                                        match[1][self.round_name[len(self.round_name) - 1]]
            else:  # in case this is the first create the key and add point of first round
                match[1]["total_score_of_tournament"] = match[1][self.round_name[len(self.round_name) - 1]]
            # add back the player to the list
            self.players.append(match[1])

        if (self.player_number % 2) != 0:  # if player number isn't pair, add zero point to exit player
            self.exit_player[self.round_name[len(self.round_name) - 1]] = 0
            # Add the point of the round to total score
            if len(self.round_name) > 1:  # in case it's not the first round : add point to the total
                self.exit_player["total_score_of_tournament"] = self.exit_player["total_score_of_tournament"] + \
                                                                self.exit_player[
                                                                    self.round_name[len(self.round_name) - 1]]
            else: # in case this is the first create the key and add point of first round
                self.exit_player["total_score_of_tournament"] = self.exit_player[
                    self.round_name[len(self.round_name) - 1]]
            # this player is add back to the players list
            self.players.append(self.exit_player)
        else:  # if player number is pair then pass
            pass
        """for player in self.players:
            print(player["full_name"], player["total_score_of_tournament"])"""

    # function to classify players by their score at the last round
    def sort_list_other_round(self):
        # empty the list to create a new one
        self.sorted_players[:] = []
        # classify players by previous round's score
        self.sorted_players.extend(sorted(self.players, key=lambda k: k[self.round_name[len(self.round_name) - 1]],
                                          reverse=True))
        # print(sorted_players)

    # classify players by their total score at the tournament and give the classification (name and score)
    def tournament_classement(self):
        self.sorted_players[:] = []
        self.sorted_players.extend(sorted(self.players, key=lambda k: k["total_score_of_tournament"], reverse=True))
        for player in self.sorted_players:
            print(player)
            print(player["total_score_of_tournament"])
