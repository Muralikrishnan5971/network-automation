import csv

with open('testfiles/testdata.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)            # skips the first line in the reader object
    year_1963 = dict()
    for row in reader:
        year_1963[row[0]] = row[1]
    print(year_1963)

    print(year_1963.values())   # values function returns a list of values
    max_1963 = max(year_1963.values())
    print(max_1963)

    # interating over the dictionary year_1963

    for k, v in year_1963.items():
        if max_1963 == v:
            print(f"busiest month in 1963 : {k}, Flights: {v.strip()}")     # strip function removes all whitespaces



