import csv
with open("data.csv", "r") as csv_file:
    rows = csv.DictReader(csv_file, delimiter=',')
    for row in rows:
        time = row["Time"]
        temp = format((float(row["TempInF"])-32)*5/9, '.2f')
        print("The temperature at", time, "is", temp, "degrees Celcius.")