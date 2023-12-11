#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times

def main():

    sum = 0

    with open("day04/input.txt") as file:

        #element 0 always represents how many copies of the current card you have
        #so element 0 is deleted with each loop, and new multipliers are appended
        multipliers = [1]

        for line in file:
            splitLine = line.split()
            winnings = splitLine[2:12]
            ours = splitLine[13:]
            numMatches = len([n for n in winnings if n in ours])
            
            sum += multipliers[0]
            
            #new copies of cards created by the current card
            newMultipliers = [multipliers[0]] * numMatches
            #delete element 0
            multipliers = multipliers[1:]
            #extend the number of current copies if more cards are needed (default 1 copy of each card)
            while len(newMultipliers) > len(multipliers) or len(multipliers) == 0:
                multipliers += [1]
            #add the new copies of cards to the corresponding current copies
            for i in range(len(newMultipliers)):
                multipliers[i] += newMultipliers[i]
    
    print(sum)

main()