from fileOps import readFileRemoveLinebreaks

class LotteryTicket:
    def __init__(self, name, winningNumbers, myNumbers):
        self.name = name
        self.winningNumbers = winningNumbers
        self.myNumbers = myNumbers
    def FindMyWinningNumbers(self):
        myWinningNumbers = []
        for myNumber in self.myNumbers:
            if myNumber in self.winningNumbers:
                myWinningNumbers.append(myNumber)
        return myWinningNumbers
    def __str__(self):
        winningNumStr = ""
        for num in self.winningNumbers:
            winningNumStr += f"{num},"
        myNumStr = ""
        for num in self.myNumbers:
            myNumStr += f"{num},"
        return f"{self.name}: Winning={winningNumStr} Mine={myNumStr}"

# Example input: 
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def parseLotteryTickets(lines):
    lotteryTickets = []
    for line in lines:
        nameAndNumbers = line.split(':')
        winningNumberString = nameAndNumbers[1].split('|')[0].replace("  ", " ").strip()
        myNumberString = nameAndNumbers[1].split('|')[1].replace("  ", " ").strip()
        lotteryTickets.append(LotteryTicket(nameAndNumbers[0].strip(), 
                                            winningNumberString.split(' '), 
                                            myNumberString.split(' ')))
    return lotteryTickets

LotteryTickets = parseLotteryTickets(readFileRemoveLinebreaks("day04input.txt"))
lotteryPoints = 0
for ticket in LotteryTickets:
    winningNumbers = ticket.FindMyWinningNumbers()
    ticketPoints = 0
    if len(winningNumbers) > 0:
        ticketPoints = 2 ** (len(winningNumbers)-1)
    lotteryPoints += ticketPoints
    print(f"{ticket.name}: {ticketPoints} points {winningNumbers}")

print(lotteryPoints)