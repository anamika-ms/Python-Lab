import csv

def read_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


csv_filename = "sample.csv"
read_csv_file(csv_filename)
