import os
import json


def convert_to_nld(directory, converted_file_path):
    for filename in os.listdir(directory):
        print(filename)
        finalfilename = converted_file_path + filename
        file = directory + '/' + filename
        print(file)

        json_data = open(file, encoding="utf-8")   # use utf-8-sieg for files with special
        prop_dict = json.load(json_data)
        with open(finalfilename, 'w', encoding="utf-8") as f:
            for rec in prop_dict:
                if len(rec) > 0:
                    f.write(json.dumps(rec) + '\n')

        print(f"conversion of {filename} successful")


if __name__ == '__main__':
    convert_to_nld('C:/Users/angelinat/Documents/checks/downloaded', 'C:/Users/angelinat/Documents/checks/converted')
