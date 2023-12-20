import os

def readFile(relativePath):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the file path relative to the script directory
    file_path = os.path.join(script_dir, relativePath)
    #print(file_path)

    with open(file_path, "r") as file:
        return file.readlines()

def readFileRemoveLinebreaks(relativePath):
    linesWithLineBreaks = readFile(relativePath)
    lines = []
    for line in linesWithLineBreaks:
        lines.append(str(line).strip())
    return lines

# This makes it possible to call readFile from the command line:
# >>> python fileOps.py Day18/input.txt
if __name__ == "__main__":
    import sys
    f = readFile(sys.argv[1])
    print(f)