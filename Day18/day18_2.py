import os
from collections import namedtuple

def readFile():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path relative to the script directory
    file_path = os.path.join(script_dir, "input.txt")
    #print(file_path)

    with open(file_path, "r") as file:
        return file.readlines()

#Point = namedtuple("Point", ["x", "y"])

## 
class pointWithColor:
    def __init__(self, direction, length, x0, y0, color):
        if direction == "0":    # R
            self.x = x0 + length
            self.y = y0
        elif direction == "2":  # L
            self.x = x0 - length
            self.y = y0
        elif direction == "3":  # U
            self.x = x0
            self.y = y0 + length
        elif direction == "1":  # D
            self.x = x0
            self.y = y0 - length
        else:
            raise Exception("Invalid direction")
        self.color = color
        self.direction = direction
        self.length = length
    def __str__(self):
        return f"{self.direction} {self.length} ({self.x},{self.y})"

def parseFile(lines):
    list = []
    x0 = 0
    y0 = 0
    for line in lines:
        splitLine = line.strip().split()
        color = splitLine[2].replace("(", "").replace(")", "").replace("#", "")
        point = pointWithColor(
            color[5:6], 
            int(color[:5], 16), 
            x0,
            y0,
            color)
        list.append(point)
        x0 = point.x
        y0 = point.y
    return list

points = parseFile(readFile())

# https://web.archive.org/web/20100405070507/http://valis.cs.uiuc.edu/~sariel/research/CG/compgeom/msg00831.html#        Let 'vertices' be an array of N pairs (x,y), indexed from 0
#        Let 'area' = 0.0
#        for i = 0 to N-1, do
#        Let j = (i+1) mod N
#        Let area = area + vertices[i].x * vertices[j].y
#        Let area = area - vertices[i].y * vertices[j].x
#        end for
#        Return 'area'

# Added circumference + 1 to the formula, to account for the fact that the formula only calculates the area 
# inside of the polygon, and the elves also dug out the _sides_ of the polygon.

area = 0
circumference = 0
numPoints = len(points)
for i in range(numPoints):
    j = (i + 1) % numPoints
    area = area + points[i].x * points[j].y
    area = area - points[i].y * points[j].x
    circumference += points[i].length
    print("p0:", points[i], ", p1:", points[j],"-->", area)

print((abs(area)+circumference)/2 + 1)