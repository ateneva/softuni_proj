import os


def transform_to_dict(path_to_json, clean_path):
    for filename in os.listdir(path_to_json):
        print(filename)
        finalfilename = clean_path + '/' + filename
        file = path_to_json + '/' + filename

        try:
            os.remove(finalfilename)
        except:
            IOError

        with open(file, 'r') as jf:
            print(f'Opening {file}')
            with open(finalfilename, 'a') as jm:
                code = filename[:filename.find('.')].upper()
                jm.write("{")
                jm.write(f'"Code": "{code}",')
                for line in jf:
                    jm.write(line)
                jm.write('}')
            print(f'Converted {finalfilename}')

if __name__ == '__main__':
    transform_to_dict('C:/Users/angelinat/Documents/checks/downloaded', 'C:/Users/angelinat/Documents/checks/converted')