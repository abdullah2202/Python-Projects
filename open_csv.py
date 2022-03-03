import csv
import time

with open("files/test_data.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count+= 1
        print(f'{row["name"]}\'s number is {row["number"]} and his code is {row["code"]} ')
        time.sleep(2)
        