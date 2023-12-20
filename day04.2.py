from fileOps import readFileRemoveLinebreaks

class LotteryTicket:
    def __init__(self, name, winningNumbers, myNumbers):
        self.name = name
        self.winningNumbers = winningNumbers
        self.myNumbers = myNumbers
        self._numCopies = 1
    def FindHowManyWinningNumbers(self):
        numberOfWinningNumbers = 0
        for myNumber in self.myNumbers:
            if myNumber in self.winningNumbers:
                numberOfWinningNumbers += 1
        return numberOfWinningNumbers, self._numCopies
    def AddTicketCopies(self, numCopies):
        self._numCopies += numCopies
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
        lotteryTickets.append(LotteryTicket(int(nameAndNumbers[0].replace("Card ", "").strip()), 
                                            winningNumberString.split(' '), 
                                            myNumberString.split(' ')))
    return lotteryTickets

LotteryTickets = parseLotteryTickets(readFileRemoveLinebreaks("day04input.txt"))
maxTicketNumber = len(LotteryTickets)
totalNumberOfScratcCards = 0
for ticket in LotteryTickets:
    winningScratchCards, numCopies = ticket.FindHowManyWinningNumbers()
    print(f"{ticket.name} has {winningScratchCards} wins and {numCopies} copies")
    totalNumberOfScratcCards += numCopies
    for i in range(winningScratchCards):
        if ticket.name + i + 1 <= maxTicketNumber:
            print(f"Ticket {ticket.name} is adding {numCopies} copies of ticket {ticket.name + i + 1}")
            LotteryTickets[ticket.name + i].AddTicketCopies(numCopies)
    
print(totalNumberOfScratcCards)