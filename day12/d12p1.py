#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/1663807/how-do-i-iterate-through-two-lists-in-parallel

# this one takes a few seconds to run
# (brute force solution)

#returns a list of strings, possible row configurations
# basically for every ?, splits it into 2 possible rows
def possibleConfigurations(row):
    possibles = {row}
    while True:
        newPossibles = set()
        for row in possibles:
            if row.find('?') != -1:
                newPossibles.add(row.replace('?', '.', 1))
                newPossibles.add(row.replace('?', '#', 1))
        if len(newPossibles) == 0:
            return possibles
        possibles = newPossibles

#returns a list of ints, the counts of the streaks of broken strings
def findCount(row):
    count = []
    streak = 0
    for spring in row:
        if spring == '#':
            streak += 1
        elif streak != 0:
            count.append(streak)
            streak = 0
    if streak != 0:
        count.append(streak)
    return count


def main():

    rows = []
    counts = []

    with open("day12/input.txt") as file:

        for line in file:
            line = line.split()
            rows.append(line[0])
            
            count = list(map(int, line[1].split(',')))
            counts.append(count)

    total = 0

    for row, count in zip(rows, counts):
        possibles = possibleConfigurations(row)
        for possible in possibles:
            if findCount(possible) == count:
                total += 1
    
    print(total)

main()