from modele import *

# For new tournament, enter all information about it
tournament = Tournament(name=input("name"), player_number=input("number_of_player"),
                        round_number=input("number of round"), exit_player=None, round_name=None, players=[],
                        sorted_players=[], tournament_score=0)

for player in range(0, tournament.player_number):
    player = Player(name=input("last_name"), initial_score=input("score_initial"), tournament_score=0, match_score=[])
    tournament.list_of_players(player)

tournament.sorted_players_list_beginning(tournament.sorted_players, tournament.players)

for x in range(0, tournament.round_number):
    tournament.name_of_the_round(tournament.round_name)
    tournament.matching_players(tournament.players, tournament.player_number, tournament.sorted_players,
                                tournament.list_of_match)
    tournament.score_of_match(tournament.players, tournament.player_number, tournament.list_of_match,
                              tournament.exit_player)
    tournament.sort_list_other_round(tournament.sorted_players, tournament.players, tournament.round_name)
