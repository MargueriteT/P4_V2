from modele import *

# For new tournament, enter all information about it
tournament = Tournament(name=input("name"), player_number=input("number_of_player"),
                        round_number=input("number of round"), exit_player=None, round_name=[], players=[],
                        sorted_players=[])

# for the tournament, enter information for x player (player_number)
for i in range(0, tournament.player_number):
    # enter all information about player
    tournament.list_of_players(Player(first_name=input("first_name"), last_name=input("last_name"),
                                      initial_score=input("score_initial")))

# classification of players by initial score
tournament.sorted_players_list_beginning()

# for number of round : enter the name of the round, match players, add the score of each of them
for x in range(0, tournament.round_number):
    tournament.name_of_the_round()
    tournament.matching_players()
    tournament.score_of_match()
    # if this is the last round then display results of tournament and stop the app
    if x == tournament.round_number - 1:
        tournament.tournament_classement()
        break
    # if it's not the last round then classify players by score at the previous round and continues
    else:
        tournament.sort_list_other_round()