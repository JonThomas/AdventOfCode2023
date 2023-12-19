from fileOps import readFile
from geometricOps import isPointInRect
from day03 import Numeric, SpecialChar, parseNumbersAndSymbols

numerics, specialChars = parseNumbersAndSymbols(readFile("day03input.txt"))

for s in specialChars:
    print(s)

# For all special chars with symbol '*', multiply its numeric neighbours when 
# the special char has exactly two neighbours
gearRatio = 0
for s in specialChars:
    numericNeighbours = []
    if s.symbol != '*':
        continue
    for n in numerics:
        if n.nextToSpecialChar(s.x, s.y):
            print(f"SpecialChar {s} is next to {n}")
            numericNeighbours.append(n)
    if len(numericNeighbours) == 2:
        print(f"SpecialChar {s} is next to exactly two numerics")
        gearRatio += int(numericNeighbours[0].number) * int(numericNeighbours[1].number)

print (f"Gear ratio: {gearRatio}")
