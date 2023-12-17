import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the script directory
file_path = os.path.join(script_dir, "input.txt")
print(file_path)

with open(file_path, "r") as file:
    array = file.readlines()

for entry in array:
    print(entry.strip())  # Example: printing each entry after stripping newline characters


