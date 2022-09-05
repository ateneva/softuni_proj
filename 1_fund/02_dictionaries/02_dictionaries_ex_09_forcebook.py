
# 09. Forcebook ----------------------------------------------------------------

'''
The force users are struggling to remember which side are the different forceUsers from, because they switch them
too often. So you are tasked to create a web application to manage their profiles.
You should store an information for every unique forceUser,registered in the application.

You will receive several input linesin one of the following formats:
    {forceSide} | {forceUser}{forceUser} -> {forceSide}

The forceUser and forceSideare strings, containing any character.
* If you receive forceSide | forceUser, you should check if such forceUser already exists,
and if not, addhim/her to the corresponding side.

* If you receive a forceUser -> forceSide,  should check if there is such a forceUseralready
    and if so, change his/her side.
    If there is no such forceUser, add him/her to the corresponding forceSide,
treating the command as a new registered forceUser.

Then you should print on the console: "{forceUser} joins the {forceSide} side!"

You should end your program when you receive the command "Lumpawaroo".
At that point you should print each force side, ordered descending by forceUsers count, than ordered by name.

For each side print the forceUsers, ordered by name.
In case there are no forceUsers in a side, you shouldn`t print the side information.


The input comes in the form of commands in one of the formats specified above.
The input ends, when you receive the command "Lumpawaroo".

As output for each forceSide, ordered descending by
    forceUsers count,
    then by name,
    you must print all the forceUsers, ordered by name alphabetically.

The output format is:
    Side: {forceSide}, Members: {forceUsers.Count}! {forceUser}! {forceUser}! {forceUser}

In case there are NOforceUsers, don`t print this side.
'''

# 40 out of 100
forces = input()
forcebook = {}
forceusers = []

while forces != 'Lumpawaroo':
    if forces.find('|'):
        joins = forces.split(' | ')
        if len(joins) > 1:
            side = joins[0]
            user = joins[1]

            if side not in forcebook:
                forcebook[side] = [user]
            else:
                for sides, users in forcebook.items():
                    if side == sides and user not in users:
                        forcebook[side].append(user)

    if forces.find('->'):
        moves = forces.split(' -> ')
        if len(moves) > 1:
            side = moves[1]
            user = moves[0]

            for sides,users in forcebook.items():
                if side !=sides and user in users:
                    forcebook[sides].remove(user)

                elif side == sides and user not in sides:
                    forcebook[side].append(user)
                    print(f"{user} joins the {side} side!")

            forcebook[side].sort()

    forces = input()

forcebook = dict(sorted(forcebook.items(), key=lambda s: (-len(s[1]), s[0])))

for k, v in forcebook.items():
    if len(v) > 0:
        print(f'Side: {k}, Members: {len(v)}')
        for m in v:
            print(f'! {m}')



# **********More Exercises **************************************


# 01. Ranking ------------------------------------------------------


# 02. Judge --------------------------------------------------------


# 03. MOBA Challenger ----------------------------------------------


# 04. Snowwhite ----------------------------------------------------


# 05. Dragon Army --------------------------------------------------
