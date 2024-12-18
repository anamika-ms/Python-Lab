def copy_odd_lines(source_file, destination_file):
    with open(source_file, 'r') as src:
        lines = src.readlines()

    with open(destination_file, 'w') as dest:
        for i in range(0, len(lines), 2):
            dest.write(lines[i])


source = "example.txt"
destination = "odd_lines.txt"
copy_odd_lines(source, destination)
print("Odd lines have been copied.")
