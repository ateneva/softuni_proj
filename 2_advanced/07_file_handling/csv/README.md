

# Read to CSV with `csv` module

* read csv with reader

```python
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```

* read CSV from dicotionary with `DictReader`
```python
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
```
* If quoting is set to `csv.QUOTE_MINIMAL`, then `.writerow()` will quote fields only if they contain the delimiter or the quotechar
  * This is the default case

* If quoting is set to `csv.QUOTE_ALL`, then `.writerow()` will quote all fields


* If quoting is set to `csv.QUOTE_NONNUMERIC`, then `.writerow()` will quote all fields containing text data and 
  * convert all numeric fields to the float data type.


* If quoting is set to `csv.QUOTE_NONE`, then `.writerow()` will escape delimiters instead of quoting them. 
  * In this case, you also must provide a value for the escapechar optional parameter.


# Write to CSV with `csv` module 

```python
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

* write all rows at once and quote all fields the fields
```python
import csv

with open("sample.csv", "w") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows([["a", 1], ["b", 2]])

f.close()
```

* write to a csv file from dictionary
```python
import csv

with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
```

# Read CSV with `pandas`
```python
import pandas as pd

df = pd.read_csv(
    "/path/to/output/file.csv",
    escapechar="\\")
```

```python
import pandas
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)
```

# Write to CSV with `pandas`
```python
import csv
import pandas as pd

df = # build dataframe here

df.to_csv(
    "/path/to/output/file.csv",
    quoting=csv.QUOTE_NONNUMERIC,
    escapechar="\\",
    doublequote=False,
    index=False)
```

```python
import pandas
df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')
```

# References
* https://realpython.com/python-csv/
* https://www.adamsmith.haus/python/examples/3278/csv-write-to-a-csv-file-and-quote-all-fields