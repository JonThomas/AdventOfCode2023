import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the script directory
file_path = os.path.join(script_dir, "input.txt")
print(file_path)

with open(file_path, "r") as file:
    array = file.readlines()

total = 0

for entry in array:
    # Find the first digit in the entry
    first_digit = next((char for char in entry if char.isdigit()), None)
    # Find the last digit in the entry
    last_digit = next((char for char in entry[::-1] if char.isdigit()), None)

    print(entry.strip(), ": First Digit:", first_digit, "Last Digit:", last_digit)

    total += int(first_digit + last_digit)

print("Total:", total)