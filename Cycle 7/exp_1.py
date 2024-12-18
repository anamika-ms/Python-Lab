def read_file_into_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

filename = "example.txt"
lines_list = read_file_into_list(filename)
print(lines_list)
