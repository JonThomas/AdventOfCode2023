from fileOps import readFile

array = readFile("day01input.txt")

total = 0

for entry in array:
    # Find the first digit in the entry
    first_digit = next((char for char in entry if char.isdigit()), None)
    # Find the last digit in the entry
    last_digit = next((char for char in entry[::-1] if char.isdigit()), None)

    print(entry.strip(), ": First Digit:", first_digit, "Last Digit:", last_digit)

    total += int(first_digit + last_digit)

print("Total:", total)