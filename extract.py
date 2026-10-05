import csv

def extract(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    print("Row count:", len(rows) - 1)

    return rows