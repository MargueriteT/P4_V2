from modele import *

# For new tournament, enter all information about it
tournament = Tournament(name=input("name"), player_number=input("number_of_player"), round_number=input("number of round"))

# For X players enter information about them and add them to the list of player
for player in range(0, tournament.player_number):
    player = Player(name=input("last_name"), initial_score=input("score_initial"), tournament_score=0, match_score=[])
    player.information_about_players()
    player.__add__()

# ranking players
tournament.player_ranking()







