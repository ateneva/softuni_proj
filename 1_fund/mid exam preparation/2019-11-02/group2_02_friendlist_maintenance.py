
# ************************************************ Group 2 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20191102_mid_exam_group_2

# ---------------------------------02. Friendlist Maintenance (Lists Basic)---------------------------------

# ------- 100 points -----------------------

friends = input().split(", ")
command = input()

while command != "Report":
    do = command.split(" ")[0]
    #print(friends, command, do)

    if do == 'Blacklist':
        friend = command.split(" ")[1].strip()
        if friend in friends:
            old_friend = friend
            friend_idx = friends.index(friend)
            friends[friend_idx] = "Blacklisted"
            print(f"{old_friend} was blacklisted.")
        else:
            print(f"{friend} was not found.")

    elif do == "Error":
        friend_idx = int(command.split(" ")[1])
        friend = friends[friend_idx]

        if friend not in ("Blacklisted", "Lost"):
            old_friend = friend.strip()
            friends[friend_idx] = "Lost"
            print(f"{old_friend} was lost due to an error.")

    elif do == "Change":
        idx = int(command.split(" ")[1])
        new_name = command.split(" ")[2]

        if idx >= 0 and idx < len(friends):
            old_name = friends[idx].strip()
            friends[idx] = new_name
            print(f"{old_name} changed his username to {new_name}.")

    command = input()

blacklisted = friends.count("Blacklisted")
lost = friends.count("Lost")
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(" ".join(friends))
