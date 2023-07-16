import csv

with open('passwd', "r") as f:
    reader = csv.reader(f, delimiter=':', lineterminator="\n")
    for row in reader:
        print(row)

"""
These properties we use such as delimiter and lineterminator can be grouped
and used ad csv delimiters

"""
print(csv.list_dialects())