
'''Create a program that creates a file called my_first_file.txt.
    In that file write a single line with the content:
        'I just created my first file!'
'''

def create_file(folder, file):
    full_path = folder + file

    with open(full_path, 'w', encoding="utf-8") as f:
        f.write('I just created my first file!')

    return full_path


def file_reader(path):
    try:
        with open(path, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            return lines

    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    create_file('C:/Users/hp/Desktop/', 'my_first_file.txt')
    print(file_reader('C:/Users/hp/Desktop/my_first_file.txt'))