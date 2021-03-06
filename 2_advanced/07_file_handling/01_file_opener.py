

'''Create program that opens the file.
     If the file is found, print 'File found'.
     If the file is not found, print 'File not found'.
 '''

def open_file(folder, file):
    full_path = folder + file
    try:
        with open(full_path, 'r') as f:
            f.read()
            print('File found')

    except FileNotFoundError:
        print('File not found')

open_file('C:/Users/hp/Desktop/', 'text.txt')
