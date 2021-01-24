
# ---------------------10. SoftUni exam results --------------------------------

'''
You will be receiving lines in the following format:
    "{username}-{language}-{points}" until you receive "exam finished".

You should store each username and his submissions and points.
You can receive a command to ban a user for cheating in the following format: "{username}-banned".

In that case, you should remove the user from the contest,
    but preserve his submissions in the total count of submissions for each language.

After receiving "exam finished" print each of the participants,
    ordered descending by their max points, then by username, in the following format:
    Results:
    {username} | {points}

After that print each language, used in the exam, ordered descending by
    total submission count and then by language name, in the following format:
    Submissions:
    {language} – {submissionsCount}
'''

# --------------100 points --------------------
judge = input()
results = {}
submissions = {}

while judge != "exam finished":
    judge = judge.split('-')
    user = judge[0]
    language = judge[1]

    if len(judge) == 3:
        points = int(judge[2])

        if user not in results:         # create results key
            results[user] = [points]    # there will be multiple points per user
        else:
            results[user].append(points)

        if language not in submissions:     # create submissions key
            submissions[language] = [user]
        else:
            submissions[language].append(user)

    else:
        results.pop(user)


    judge = input()
results = dict(sorted(results.items(), key=lambda p: (-max(p[1]), p[0])))
submissions = dict(sorted(submissions.items(), key=lambda s: (-len(s[1]), s[0])))

print("Results:")
for user, points in results.items():
    print(f'{user} | {max(points)}')

print("Submissions:")
for language, times in submissions.items():
    print(f'{language} - {len(times)}')
