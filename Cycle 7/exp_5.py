import csv

def write_dict_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def read_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

dict_data = [
    {'Name': 'John', 'Age': 28, 'City': 'New York'},
    {'Name': 'Anna', 'Age': 22, 'City': 'London'},
    {'Name': 'Peter', 'Age': 34, 'City': 'Berlin'}
]

csv_filename = "output.csv"
write_dict_to_csv(csv_filename, dict_data)
print("CSV file content:")
read_csv_file(csv_filename)
