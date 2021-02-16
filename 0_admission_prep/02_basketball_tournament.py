
# ******* 06.basketball tournament (nested loop) *******************************

tournament = input()
wins = 0
losses = 0
tournaments = 0

while tournament != 'End of tournaments':
    games = int(input())
    game_count = 0

    for game in range(1, games + 1):
        team_dessy = int(input())
        rival = int(input())
        game_count += 1
        winner_points = abs(team_dessy-rival)

        if team_dessy > rival:
            wins += 1
            print(f"Game {game_count} of tournament {tournament}: win with {winner_points} points.")

        else:
            losses += 1
            print(f"Game {game_count} of tournament {tournament}: lost with {winner_points} points.")

    tournaments += game_count
    tournament = input()

else:
    print(f'{(wins/tournaments * 100):.2f}% matches win')
    print(f'{(losses/tournaments * 100):.2f}% matches lost')
