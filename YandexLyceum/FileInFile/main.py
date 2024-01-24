input_file_name = "input.txt"
output_file_name = "output.txt"
units_to_numbers = {"B": 1}
units_to_numbers["K"] = 1024
units_to_numbers["M"] = units_to_numbers["K"] * 1024
units_to_numbers["G"] = units_to_numbers["M"] * 1024
units_to_numbers["T"] = units_to_numbers["G"] * 1024
numbers_to_units = {}
numbers_to_units[units_to_numbers["B"] * 1024] = "K"
numbers_to_units[units_to_numbers["K"] * 1024] = "M"
numbers_to_units[units_to_numbers["M"] * 1024] = "G"
numbers_to_units[units_to_numbers["G"] * 1024] = "T"

extensions = {}
files = []
with open(input_file_name) as input_file:
    lines = [line for line in input_file.readlines()]
    for line in lines:
        file, size, unit = [chunck for chunck in line.split()]
        files.append((file, size, unit))

for file, size, unit in files:
    size = int(size) * units_to_numbers[unit[0]]
    extension = file.split('.')[-1]
    if extension in extensions:
        extensions[extension].append((file, size))
    else:
        extensions[extension] = [(file, size)]

with open(output_file_name, "w") as output_file:
    extensions_order = [ext for ext in sorted(extensions.keys())]
    for ext in extensions_order:
        sum_size = 0
        sum_unit = ""
        for file, size in sorted(extensions[ext], key=lambda x: x[0]):
            sum_size += size
            print(file, file=output_file)
        min_sum_size = sum_size
        for unit in numbers_to_units:
            if 0 < sum_size // unit < min_sum_size:
                sum_unit = numbers_to_units[unit]
                min_sum_size = int(round(sum_size / unit))
        print("----------", file=output_file)
        print(f"Summary: {min_sum_size} {sum_unit}B", file=output_file, end="\n\n")
