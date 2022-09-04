
# ************train the trainers ***********************************************
jury = int(input())
presentation = input()
total_score = 0
total_avg_score = 0
presentation_count = 0

while not presentation == 'Finish':
    avg_score = 0  # nullify avg_score fpr every presentation
    total_score = 0

    for i in range(1, jury + 1):
        score = float(input())
        total_score += score
        total_avg_score += score
        presentation_count += 1

    avg_score = total_score / jury
    print(f'{presentation} - {avg_score:.2f}.')

    presentation = input()

else:
    total_avg_score /= presentation_count
    print(f"Student's final assessment is {total_avg_score:.2f}.")


# ************* 06.christmas decoration (nested loop) **************************

budget = int(input())
decoration = input()
money_left = 0
cost = 0

while decoration != 'Stop':
    for char in decoration:
        i = ord(char)
        cost += i

    if cost <= budget:
        print("Item successfully purchased!")
    else:
        print("Not enough money!")
        break

    money_left = abs(budget-cost)
    decoration = input()

else:
    print(f"Money left: {money_left}")


# ***************06.name game (nested loop) ************************************

player = input()
winner_points = 0
winner = ''

while player != 'Stop':
    points = 0

    for char in player:
        i = ord(char)
        num = int(input())

        if i == num:
            points += 10
        else:
            points += 2

    if points >= winner_points:
        winner_points = points
        winner = player

    player = input()

print(f"The winner is {winner} with {winner_points} points!")

 # **************06.the most powerful word (nested loop) ***********************

word = input()
strongest = 0
most_powerful_word = ''

while word != 'End of words':
    strength = 0

    for char in word:
        i = ord(char)
        strength += i

    if word[0] in ('a', 'e', 'i', 'o', 'u', 'y') \
        or word[0] in ('A', 'E', 'I', 'O', 'U', 'Y'):
        strength *= len(word)

    else:
        strength //= len(word)

    if strength >= strongest:
        strongest = strength
        most_powerful_word = word

    word = input()

print(f"The most powerful word is {most_powerful_word} - {strongest}")


# *************06.favourtite movie (nested loop) *******************************

movie = input()
movies = 0
most_points = 0
best_movie = ''

while not movie == 'STOP':
    movies += 1
    points = 0   # needs to start over for every movie

    for char in movie:
        p = ord(char)
        points += p

        if p >= 97 and p <= 122:
            points -= 2*len(movie)

        elif p >= 65 and p <= 90:
            points -= len(movie)

    if points >= most_points:
        most_points = points
        best_movie = movie

    if movies >= 7:
        print("The limit is reached.")
        print(f"The best movie for you is {best_movie} with {most_points} ASCII sum.")
        break

    movie = input()

else:
    print(f"The best movie for you is {best_movie} with {most_points} ASCII sum.")


# **************06.high jump (nested loop) *************************************

target = int(input())
first_target = target - 30
jumps = 0
fail = 0

while first_target <= target:
    for attempt in range(1, 4):
        next_jump = int(input())
        jumps += 1

        if next_jump > first_target:
            first_target += 5
            fail = 0
            break
        else:
            fail += 1

    if fail == 3:
        print(f"Tihomir failed at {next_jump}cm after {jumps} jumps.")
        break

else:
    print(f"Tihomir succeeded, he jumped over {target}cm after {jumps} jumps.")

# ************06.basketball tournament (nested loop) ***************************

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
