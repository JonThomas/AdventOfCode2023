import os

def readFile():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path relative to the script directory
    file_path = os.path.join(script_dir, "input.txt")
    #print(file_path)

    with open(file_path, "r") as file:
        return file.readlines()

numbersArray = ["one","two","three","four","five","six","seven","eight","nine"]
    
def toNumber(numeric):
    return str(numbersArray.index(numeric) + 1)

def findNumberInString(input):
    inputPart = ""
    for char in input:
        if char.isdigit():
            return char
        inputPart += char
        #if next((char for char in entry if char.isdigit()), None)
        for num in numbersArray:
            if num in inputPart:
                return toNumber(num)

def findNumberInStringFromEnd(input):
    inputPart = ""
    for char in input[::-1]:
        if char.isdigit():
            return char
        inputPart = char + inputPart
        #if next((char for char in entry if char.isdigit()), None)
        for num in numbersArray:
            if num in inputPart:
                return toNumber(num)

total = 0

for entry in readFile():
    # Find the first digit in the entry
    first_digit = findNumberInString(entry.strip())
    # Find the last digit in the entry
    last_digit = findNumberInStringFromEnd(entry.strip())

    #print(entry.strip(), ": First Digit:", first_digit, "Last Digit:", last_digit)

    total += int(first_digit + last_digit)

print("Total:", total)

