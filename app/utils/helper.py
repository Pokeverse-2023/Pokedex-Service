import csv


def convert_to_json(file_name: str, headers: list):
    csv_file = open(file_name, "r")
    reader = csv.DictReader(csv_file)

    for each in reader:
        row = {}
        for field in headers:
            row[field] = each[field]
        return row
