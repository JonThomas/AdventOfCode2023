from fileOps import readFile

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

for entry in readFile("day01input.txt"):
    # Find the first digit in the entry
    first_digit = findNumberInString(entry.strip())
    # Find the last digit in the entry
    last_digit = findNumberInStringFromEnd(entry.strip())

    #print(entry.strip(), ": First Digit:", first_digit, "Last Digit:", last_digit)

    total += int(first_digit + last_digit)

print("Total:", total)

