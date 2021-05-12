import csv
import datetime as dt

today = dt.datetime.today().strftime('%Y%m%d%H%M')
today_date = dt.datetime.today().strftime('%Y%m%d')
print(today)


def change_csv_delimiters(inputPath, outputPath):
    '''

    Args:
        inputPath = full path to the file that needs changing
        outputPath = full path where the updated file should be saved
    '''

    print("Converting CSV to semi-colon delimited file...")
    with open(inputPath, encoding="utf8") as inputFile:
        with open(outputPath, 'w', newline='', encoding="utf8") as outputFile:
            reader = csv.DictReader(inputFile, delimiter=';')
            writer = csv.DictWriter(outputFile, reader.fieldnames, delimiter=',', quotechar='"')
            writer.writeheader()
            writer.writerows(reader)
    print("Conversion complete")


if __name__ == '__main__':
    change_csv_delimiters('C:/Users/angelinat/Documents/checks/actions.csv', 'C:/Users/angelinat/Documents/checks/actions_comma.csv')
