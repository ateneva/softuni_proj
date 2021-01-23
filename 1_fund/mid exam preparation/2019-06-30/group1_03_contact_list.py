
# ************************************************ Group 1 ****************************************************
# https://github.com/ateneva/softuni_proj/wiki/fund_20190630_mid_exam_group_1

# ---------------------------------03. Contact List (Lists Advanced) -----------------------------------------

# ------------90 points (1 X incorrect answer)--------------------
contacts = input().split(" ")

while True:
    command = input()
    do = command.split(" ")[0]

    if do == "Add":
        contact = command.split(" ")[1]
        idx = int(command.split(" ")[2])
        if contact not in contacts:
            contacts.append(contact)
        else:
            if 0 <= idx <= len(contacts):
                contacts.insert(idx, contact)

    elif do == "Remove":
        idx = int(command.split(" ")[1])
        if 0 <= idx <= len(contacts):
            del contacts[idx]

    elif do == "Export":
        start = int(command.split(" ")[1])
        count = int(command.split(" ")[2])
        if count >= len(contacts):
            export = contacts[start:]
        else:
            export = contacts[start:count]
        print(" ".join(export))

    elif do == "Print":
        print_type = command.split(" ")[1]
        if print_type == "Normal":
            contacts = " ".join(contacts)
            print(f"Contacts: {contacts}")
        else:
            contacts.reverse()
            contacts = " ".join(contacts)
            print(f"Contacts: {contacts}")

        break
