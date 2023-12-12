#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/18648626/for-loop-with-two-variables

#return list of numerical values of cards
def cardValues(cards):
    vals = []
    for card in cards:
        if card.isdecimal():
            vals.append(int(card))
        elif card == 'T':
            vals.append(10)
        elif card == 'J':
            vals.append(11)
        elif card == 'Q':
            vals.append(12)
        elif card == 'K':
            vals.append(13)
        elif card == 'A':
            vals.append(14)
    return vals

#returns the strength of cards, based on the type
# e.g. 5 of a kind has strength 6
def handType(cards):
    repeats = {}
    for card in cards:
        repeats[card] = repeats.get(card, 0) + 1
    vals = list(repeats.values())
    vals.sort(reverse=True)

    if vals[0] == 5:
        return 6
    elif vals[0] == 4:
        return 5
    elif vals[0] == 3:
        if vals[1] == 2:
            return 4
        else:
            return 3
    elif vals[0] == 2:
        if vals[1] == 2:
            return 2
        else:
            return 1
    else:
        return 0

#stores the numerical value of cards (in order), the type of hand, and the bid number
class Hand:
    def __init__(self, string):
        self.cards = cardValues(string[:5])
        self.type = handType(string[:5])
        self.bid = int(string[6:])

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for c1, c2 in zip(self.cards, other.cards):
            if c1 != c2:
                return c1 < c2
        return False
        
def main():

    hands = []

    with open("day07/input.txt") as file:
        for line in file:
            hands.append(Hand(line))
        
    hands.sort()
    
    sum = 0
    for i in range(len(hands)):
        sum += hands[i].bid * (i+1)
    print(sum)

main()