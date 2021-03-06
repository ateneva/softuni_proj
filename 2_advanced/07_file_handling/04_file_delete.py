
'''
Create a program that deletes the file you created in the previous task.
    If you try to delete the file multiple times, print the message:
    'File already deleted!'.
'''
import os
from pathlib import Path

def delete_files(folder, file_name):
    path_to_files = Path(folder)
    files_in_folder = path_to_files.iterdir()

    for item in files_in_folder:
        if item.name == file_name:
            os.remove(item)
            print('File deleted')
    else:
        print('File does not exist!')

delete_files('C:/Users/hp/Desktop/', 'my_first_file.txt')
