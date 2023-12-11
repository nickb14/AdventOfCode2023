#references
# https://www.w3schools.com/python/
# https://www.educative.io/answers/power-operator-in-python

def main():

    sum = 0

    with open("day04/input.txt") as file:

        for line in file:
            splitLine = line.split()
            #assuming exactly 10 winning numbers
            winnings = splitLine[2:12]
            ours = splitLine[13:]

            #list comprehension, list of numbers in both winnings and ours
            numMatches = len([n for n in winnings if n in ours])
            if numMatches != 0:
                sum += 2**(numMatches-1)
    
    print(sum)

main()