# ***************************************** Group 2 ****************************************************

# -------------------------01. Password Reset (Text Processing)-------------------------

# ------------- my solution -> 50 points ----------------------------
original_password = input()
instructions = input()
newpassword = ''

while instructions != 'Done':
    reset = instructions.split(' ')
    command = reset[0]

    if command == 'TakeOdd':
        for i, p in enumerate(original_password):
            if i % 2 != 0:
                newpassword += p
        print(newpassword)

    elif command == 'Cut':
        idx = int(reset[1])
        length = idx + int(reset[2])
        cut = newpassword[idx:length]
        newpassword = newpassword.replace(cut, '', 1)
        print(newpassword)

    elif command == 'Substitute':
        substring = reset[1]
        replace_with = reset[2]
        if substring in newpassword:
            newpassword = newpassword.replace(substring, replace_with)
            print(newpassword)
        else:
            print("Nothing to replace!")

    instructions = input()

print(f'Your password is: {newpassword}')

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^shared solution -> 100 points^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   Get Password
password = input()

while True:

    #   Handle command input
    command_input = input()
    if " " in command_input:
        command = command_input.split(" ")[0]
    else:
        command = command_input

    #   Take Odd characters only
    if command == "TakeOdd":
        password = password[1::2]
        print(password)

    elif command == "Cut":
        index = int(command_input.split(" ")[1])
        length = int(command_input.split(" ")[2])
        stop = index + length

        if len(password) > stop:
            password = password[0: index:] + password[stop::]

        print(password)

    elif command == "Substitute":
        char1 = command_input.split(" ")[1]
        char2 = command_input.split(" ")[2]

        if char1 in password:
            password = password.replace(char1, char2)
            print(password)
        else:
            print("Nothing to replace!")
    elif command == "Done":
        break

# -------------------------02. Fancy Barcodes (Regex)-----------------------------------------

# ---------------- my solution --> 70 points ---------------------------------------------
barcodes = int(input())

for b in range(1, barcodes + 1):
    barcode = input()
    valid_characters = barcode.replace("@", '').replace('#', '')
    valid_length = len(valid_characters)
    last_valid_length = barcode[valid_length+1:]
    #barcode_end = barcode[-1]

    if valid_length >= 6:
        if barcode.startswith('@#') and barcode.find('@#', valid_length, len(barcode)):
            if valid_characters.isalnum():
                start = valid_characters[0]
                if start.isupper():
                    end = valid_characters[valid_length-1]
                    if valid_characters.isalpha():            # default product group
                        product_group = '00'
                    else:
                        product_group = ''
                        for v in valid_characters:
                            if v.isdigit():
                                product_group += v
                    print(f"Product group: {product_group}")
                else:
                    print('Invalid barcode')
            else:
                print('Invalid barcode')
        else:
            print('Invalid barcode')
    else:
        print('Invalid barcode')

    #print(barcode, ' ', valid_length,last_valid_length)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^shared solution -> 100 points^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import re

def get_barcode(input_bar_code):
    pattern = "^[@]{1}[#]+([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})[@]{1}[#]+$"
    pattern = re.compile(pattern)

    result = pattern.search(input_bar_code)

    if result is None:
        return "Invalid barcode"

    inner_code = result.group(1)

    code = ""
    for ch in inner_code:
        if ch.isdigit():
            code = code + ch

    if len(code) == 0:
        code = "00"

    return "Product group: " + code

number_of_barcodes = int(input())
results = []
for i in range(number_of_barcodes):
    barcode = str(input())
    results.append(get_barcode(barcode))

for i in results:
    print(i)

# -------------------------02. Heroes of Code and Logic (Dictionaries)-----------------------------------------

# ----------------------my solution ->  0 points-------------------------------
def validate_existing_key(dictionary, key, def_value=''):
    if key not in dictionary:
        dictionary[key] = def_value

def print_dict(dictionary, template):
    for (key, value) in dictionary.items():
        print(template.format(key, value))

num_heroes = int(input())
game = input()
health_points = {}
mana_points = {}
hero_name = ''
hp = 0
mp = 0

while game != 'End':
    players = game.split(' ')
    command = players[0]

    if len(players) <= 3:
        hero_name = players[0]
        hp = [int(players[1])]
        mp = [int(players[2])]
        validate_existing_key(health_points, hero_name)
        if hero_name in health_points:
            if hero_name in health_points:
                hp.append(hp)

        validate_existing_key(mana_points, hero_name)
        if hero_name in mana_points:
            if hero_name in health_points:
                hp.append(mp)

    else:
        activities = heroes.split('-')
        if command == 'CastSpell':
            hero_name = activities[1]
            mp_needed = int(activities[2])
            spell_name = activities[3]

        elif command == 'TakeDamage':
            hero_name = activities[1]
            damage = int(activities[2])
            attacker = activities[3]

        elif command == 'Recharge':
            hero_name = activities[1]
            mp_added = int(activities[2])

        elif command == 'Heal':
            hero_name = activities[1]
            hp_added = int(activities[2])


    print(health_points, mana_points)
    heroes = input()

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^shared solution -> 100 points^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#   Set the number of heroes you gonna play with
num_of_heroes = int(input())
dict_heroes = {}

while len(dict_heroes) < num_of_heroes:

    #   Initialise your heroes' names, HP and MP
    init_hero = input()
    name = init_hero.split(" ")[0]
    health_points = int(init_hero.split(" ")[1])  # max 100 HP
    mana_points = int(init_hero.split(" ")[2])  # max 200 MP

    #   Add the hero to the dictionary
    if health_points > 100:
        health_points = 100
    if mana_points > 200:
        mana_points = 200

    dict_heroes.setdefault(name, [health_points, mana_points])

while True:
    text_input = input()
    command = text_input.split(" - ")[0]

    #   CastSpell – {hero name} – {MP needed} – {spell name}
    if command == "CastSpell":

        #   Extract info from the line
        hero = text_input.split(" - ")[1]
        mp_needed = int(text_input.split(" - ")[2])
        spell_name = text_input.split(" - ")[3]

        #   Check if hero has enough mana
        if dict_heroes[hero][1] >= mp_needed:
            dict_heroes[hero][1] -= mp_needed
            print("{0} has successfully cast {1} and now has {2} MP!".format(hero, spell_name, dict_heroes[hero][1]))
        else:
            print("{0} does not have enough MP to cast {1}!".format(hero, spell_name))

    #   TakeDamage – {hero name} – {damage} – {attacker}
    elif command == "TakeDamage":
        hero = text_input.split(" - ")[1]
        damage = int(text_input.split(" - ")[2])
        attacker = text_input.split(" - ")[3]

        dict_heroes[hero][0] -= damage

        if dict_heroes[hero][0] > 0:
            print("{0} was hit for {1} HP by {2} and now has {3} HP left!".format(
                hero, damage, attacker, dict_heroes[hero][0]
            ))
        else:
            del dict_heroes[hero]  # Bury the hero
            print("{0} has been killed by {1}!".format(hero, attacker))

    #   Recharge – {hero name} – {amount}
    elif command == "Recharge":
        hero = text_input.split(" - ")[1]
        amount = int(text_input.split(" - ")[2])

        mp_limit = 200 - dict_heroes[hero][1]
        if amount >= mp_limit:
            amount = mp_limit
            dict_heroes[hero][1] += amount
            print("{0} recharged for {1} MP!".format(hero, amount))
        else:
            dict_heroes[hero][1] += amount
            print("{0} recharged for {1} MP!".format(hero, amount))

    #   Heal – {hero name} – {amount}
    elif command == "Heal":
        hero = text_input.split(" - ")[1]
        amount = int(text_input.split(" - ")[2])

        hp_limit = 100 - dict_heroes[hero][0]
        if amount >= hp_limit:
            amount = hp_limit
            dict_heroes[hero][0] += amount
            print("{0} healed for {1} HP!".format(hero, amount))
        else:
            dict_heroes[hero][0] += amount
            print("{0} healed for {1} HP!".format(hero, amount))

    elif text_input == "End":
        break

sortedList = dict(sorted(dict_heroes.items(), key=lambda x: (-(x[1][0]), x[0])))

# sorted_list = dict(sorted(dict_stats.items(), key=lambda x: (-len(x[1]), x[0])))

for hero, others in sortedList.items():
    print(hero)

    print("  HP: {0}".format(dict_heroes[hero][0]))
    print("  MP: {0}".format(dict_heroes[hero][1]))


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^shared solution -> 100 points^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
n = int(input())
max_hp = 100
max_mp = 200

heroes_dict = {}

for i in range(n):
    line = input().split(" ")
    hero = line[0]
    hp = int(line[1])
    mp = int(line[2])

    heroes_dict[hero] = [0] * 2
    heroes_dict[hero][0] = hp
    heroes_dict[hero][1] = mp

while True:
    line = input()
    if line == "End":
        heroes_dict = dict(sorted(heroes_dict.items(), key=lambda x: (-x[1][0], x[0])))

        for k, v in heroes_dict.items():
            print(f"{k}\nHP: {v[0]}\nMP: {v[1]}")
        break

    line = line.split(" - ")
    cmd = line[0]
    hero = line[1]

    if cmd == "CastSpell":
        needed_mp = int(line[2])
        spell_name = line[3]

        if heroes_dict[hero][1] >= needed_mp:
            heroes_dict[hero][1] -= needed_mp
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero][1]} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif cmd == "TakeDamage":
        damage = int(line[2])
        attacker = line[3]

        heroes_dict[hero][0] -= damage
        if heroes_dict[hero][0] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero][0]} HP left!")
        else:
            del heroes_dict[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif cmd == "Recharge":
        amount = int(line[2])
        if heroes_dict[hero][1] + amount > max_mp:
            amount = max_mp - heroes_dict[hero][1]
            heroes_dict[hero][1] = max_mp
        else:
            heroes_dict[hero][1] += amount
        print(f"{hero} recharged for {amount} MP!")

    elif cmd == "Heal":
        amount = int(line[2])
        if heroes_dict[hero][0] + amount > max_hp:
            amount = max_hp - heroes_dict[hero][0]
            heroes_dict[hero][0] = max_hp
        else:
            heroes_dict[hero][0] += amount
        print(f"{hero} healed for {amount} HP!")

count = int(input())


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^shared solution -> 100 points^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

heroes = {}

for x in range(count):
    hero = input()
    name, hp, mp = hero.split()[0], int(hero.split()[1]), int(hero.split()[2])
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    heroes[name] = [hp, mp]

commands = input()
while commands != 'End':

    cmd = commands.split(' - ')[0]
    if cmd == 'CastSpell':
        name, mp_needed, spell_name = commands.split(" - ")[1:]
        if heroes[name][1] >= int(mp_needed):
            heroes[name][1] -= int(mp_needed)
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif cmd == 'TakeDamage':
        name, damage, attacker = commands.split(' - ')[1:]
        heroes[name][0] -= int(damage)
        if heroes[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
        else:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")

    elif cmd == 'Recharge':
        name, amount = commands.split(" - ")[1], int(commands.split(" - ")[2])
        heroes[name][1] += int(amount)
        if heroes[name][1] > 200:
            diff = heroes[name][1] - 200
            heroes[name][1] = 200
        else:
            diff = 0
        print(f'{name} recharged for {int(amount) - diff} MP!')

    elif cmd == 'Heal':
        name, amount = commands.split(" - ")[1:]
        heroes[name][0] += int(amount)
        if heroes[name][0] > 100:
            diff = heroes[name][0] - 100
            heroes[name][0] = 100
        else:
            diff = 0
        print(f'{name} healed for {int(amount) - diff} HP!')

    commands = input()

for name, stats in sorted(sorted(heroes.items(), key=lambda y: y[0]), key=lambda y: y[1][0], reverse=True):
    print(f'{name}')
    print(f'  HP: {stats[0]}')
    print(f'  MP: {stats[1]}')