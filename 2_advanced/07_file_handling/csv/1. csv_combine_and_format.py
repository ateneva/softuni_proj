
import os
from glob import glob


def union_data(file_name, file_path, save_path):
    '''
    Args:
        file_name = name of the unioned file
        file_path = full directory path to the location of the files
        save_path = directory where the unioned file should be saved
    '''

    initial_file = f'{file_name}_000000000000.csv'
    merged_file = f"{file_name}.csv"
    full_path = save_path + merged_file

    # check if file already exists and remove it if it does
    if os.path.isfile(full_path):
        os.remove(full_path)
        print('Removed old file')
    else:
        pass

    # create new unioned file
    print('Creating new unioned file...')
    with open(full_path,  'a', newline='\n', encoding='utf8') as singleFile:
        # new line in python 3 fixes unix/windows line encodings

        for csv in glob(file_path + f'{file_name}_*.csv'):
            csv_name = csv[csv.find('\\')+1:]

            if csv_name == merged_file:
                pass

            elif csv_name == initial_file:             # write the header + content of first file
                for line in open(csv, 'r'):
                    singleFile.write(line)

            else:
                with open(csv, 'r') as file:           # skip header for subsequent files
                    next(file)                         # lines = f.readlines()[1:] # alternative approach
                    for line in file:
                        singleFile.write(line)

            print(f'{csv} loaded successfully')
            os.remove(csv)
    print(f'{full_path} created')


if __name__ == '__main__':
    union_data('reviews', 'C:/Users/angelinat/Documents/python_handy/data/', 'C:/Users/angelinat/Documents/python_handy/data/')