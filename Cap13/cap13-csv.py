import csv

with open("./sample-13.1.csv", mode="r", encoding="utf-8") as f:
    reader_obj = csv.reader(f)
    for row in reader_obj:
        print(row)
