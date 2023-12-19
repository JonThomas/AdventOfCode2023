from fileOps import readFile

class Game:
    def __init__(self, gameId, numRed, numGreen, numBlue):
        self.gameId = gameId
        self.numRed = numRed
        self.numGreen = numGreen
        self.numBlue = numBlue
    def __str__(self):
        return f"{self.gameId} R:{self.numRed} G:{self.numGreen} B:{self.numBlue}"

# Input example:  3 blue, 4 red
def GetColorIfLarger(gameSet, color, currentColorCount):
    if color in gameSet:
        for c in gameSet.split(','):
            if color in c:
                count = int(c.replace(color, "").strip())
                return max(count, currentColorCount)
    return currentColorCount

def parseGames(lines):
    games = []
    # input format: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in lines:
        splitLine = line.strip().split(':')
        gameId = int(splitLine[0][5:])
        numRed = 0
        numGreen = 0
        numBlue = 0
        for gameSet in splitLine[1].split(';'):
            numRed = GetColorIfLarger(gameSet, "red", numRed)
            numBlue = GetColorIfLarger(gameSet, "blue", numBlue)
            numGreen = GetColorIfLarger(gameSet, "green", numGreen)
        game = Game(gameId, numRed, numGreen, numBlue)
        games.append(game)
        print(game)
    return games

games = parseGames(readFile("day02input.txt"))

gameIdSum = 0
for game in games:
    if game.numRed > 12 or game.numGreen > 13 or game.numBlue > 14:
        #print(game, "is invalid")
        pass  # Placeholder statement to avoid empty block error
    else:
        print(game, "OK!")
        gameIdSum += game.gameId
print("Game ID sum:", gameIdSum)