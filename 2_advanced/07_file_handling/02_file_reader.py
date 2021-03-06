
'''Create a program that reads the numbers from the file.
    Print on the console the sum of those numbers.
'''

def sum_file_numbers(folder, file):
    full_path = folder + file
    try:
        with open(full_path, 'r', encoding="utf-8") as f:
            lines = f.read()
            result = sum([int(l) for l in lines.split(',')])
            return result

    except FileNotFoundError:
        print('File not found')

print(sum_file_numbers('C:/Users/hp/Desktop/', 'numbers.txt'))
