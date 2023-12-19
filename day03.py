from fileOps import readFile
from geometricOps import isPointInRect

class Numeric:
    def __init__(self, char, x, y):
        self.number = char
        self.x = x
        self.y = y
    def padRight(self, char):
        self.number += char
    def nextToSpecialChar(self, x, y):
        # Define a rectangle around this numeric, and check if
        # the given point is inside that rectangle
        return isPointInRect(x, 
                             y, 
                             self.x - 1,
                             self.y - 1, 
                             len(self.number) + 1,  # Width depends on the number of digits 
                             2)     # Height is always 2 (!?)
    def __str__(self):
        return f"{self.number} ({self.x},{self.y})"

class SpecialChar:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.symbol} ({self.x},{self.y})"

def parseNumbersAndSymbols(linesWithLineBreaks):

    lines = []
    for line in linesWithLineBreaks:
        lines.append(str(line).strip())

    specialChars = []
    numerics = []
    thisNumeric = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            char = lines[y][x]
            if char.isdigit():
                if thisNumeric is None:
                    thisNumeric = Numeric(char, x, y)
                    numerics.append(thisNumeric)
                else:
                    thisNumeric.padRight(char)
            elif char == '.':
                thisNumeric = None
                continue
            else:
                thisNumeric = None
                specialChars.append(SpecialChar(char, x, y))
    return numerics, specialChars

numerics, specialChars = parseNumbersAndSymbols(readFile("day03input.txt"))
for n in numerics:
    print(n)
for s in specialChars:
    print(s)

enginePartSum = 0
for n in numerics:
    for s in specialChars:
        if n.number == "269" and s.symbol == '$':
            pass
        if n.nextToSpecialChar(s.x, s.y):
            print(f"Numeric {n} and special char {s} are next to eachother")
            enginePartSum += int(n.number)
            break

print (f"Sum of engine parts: {enginePartSum}")
