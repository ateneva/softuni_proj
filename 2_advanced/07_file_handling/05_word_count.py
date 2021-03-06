
'''
Write a program that reads a list of words from the file words.txt
and finds how many times each of the words is contained in another file compare_text.txt
    Matching should be case-insensitive.
    The results should be written to another text files.
    Sort the words by frequency in descending order.
'''

import re
import json

def file_reader(full_path):
    try:
        with open(full_path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            return "".join(lines)

    except FileNotFoundError:
        print('File not found')


def compare_words(folder):
    source_path = folder + 'words.txt'
    check_file = folder + 'compare_text.txt'
    special_chars = r"[.|,|-]|]|[?|!]"

    words = [word for word in file_reader(source_path).split()]
    check = [re.sub(special_chars, '', c).lower() for c in file_reader(check_file).split()]
    # print(words)
    # print(check)

    record = {w: check.count(w) for w in words}
    print(record)
    sort_record = dict(sorted(record.items(), key=lambda v: (-v[1])))

    with open(folder + 'myfile.json', 'w',  encoding="utf-8") as mf:
        record_format = json.dumps(sort_record, indent=4)
        mf.write(record_format)



if __name__ == '__main__':
    compare_words('C:/Users/hp/Desktop/')
    print(file_reader('C:/Users/hp/Desktop/myfile.json'))