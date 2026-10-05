import csv

def extract(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    print("Row count:", len(rows) - 1)

    return rows


def transform(rows):
    header = rows[0]
    data = rows[1:]

    transformed_data = []

    for row in data:
        transformed_data.append(row)

    return [header] + transformed_data
def load(rows, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Data loaded successfully")