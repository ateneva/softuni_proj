
'''
Create a program that will receive commands until the command "End".
The commands can be:
	- "Create-{file_name}" - Creates the given file with an empty content.
        If the file already exists, remove the existing text in it (as if the file is created again)

    - "Add-{file_name}-{content}" - Append the content and a new line after it.
        If the file does not exist, create it and add the content

    - "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string.
        If the file does not exist, print: "An error occurred"

    - "Delete-{file_name}" - Delete the file.
        If the file does not exist, print: "An error occurred"

'''

import os
from pathlib import Path

command = input()

def create_file(file):
    full_path = os.getcwd() + '/' + file

    with open(full_path, 'w', encoding="utf-8") as f:
        f.write('')

    return full_path


def delete_files(file):
    path_to_files = Path(os.getcwd())
    files_in_folder = path_to_files.iterdir()

    for item in files_in_folder:
        if item.name == file:
            os.remove(item)
            print('File deleted')
    else:
        print('File does not exist!')


##############################################################

while command != 'End':
    command = command.split('-')

    action = command[0]
    file_name = command[1]
    full_path = os.getcwd() + '/' + file_name

    if action == 'Create':
        create_file('file.txt')
        print(f'Created {file_name}')

    elif action == 'Add':
        content = command[2] + '\n'

        with open(full_path, 'a', encoding="utf-8") as f:
            f.write(content)
        print(f'Added {content} to {file_name}')

    elif action == 'Replace':
        old_string = command[2]
        new_string = command[3]

        try:
            with open(full_path, 'r', encoding="utf-8") as f:
                lines = f.readlines()

            for l in lines:
                if old_string in l:
                    with open(full_path, 'a', encoding="utf-8") as fwr:
                        l = l.replace(old_string, new_string)
                        fwr.write(l)
                        print(l)

        except FileNotFoundError:
            print('An error occured')


    elif action == 'Delete':
        delete_files(file_name)

    command = input()
