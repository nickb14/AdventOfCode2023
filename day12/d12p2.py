#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/1663807/how-do-i-iterate-through-two-lists-in-parallel
# https://www.geeksforgeeks.org/copy-constructor-in-python/

import copy

#Path class with 3 variables
#   streak: current streak of broken strings
#   index: current index of the list "count", corresponding to the streaks
#   mult: number of different paths represensted by this configuration of 
#       current streak and index, to further save runtime
#basically stores this information instead of manually creating 
#   each of the different possible configurations of a row
class Path:
    def __init__(self):
        self.streak = 0
        self.index = 0
        self.mult = 1

    # == so the "in" keyword works correctly
    def __eq__(self, other):
        return self.streak == other.streak and self.index == other.index
    
    def __str__(self):
        return f"streak:{self.streak} | index:{self.index} | mult:{self.mult}\n"

#directly returns the number of different ways to arrange a row, given a count configuration
#basically goes through each spring and keeps a running list of possible "Paths" depending of
#   what each next spring is, constantly checking if it is possible based on the given count configuration
def possibleConfigurations(row, count):
    paths = [Path()]
    for spring in row:
        newPaths = []
        for path in paths:
            if spring == '#':
                #bad if already enough broken springs
                if path.index == len(count) or path.streak == count[path.index]:
                    continue
                path.streak += 1
            elif spring == '.':
                if path.streak != 0:
                    #bad if not enough broken in the current streak
                    if path.streak != count[path.index]:
                        continue
                    path.streak = 0
                    path.index += 1
            else: #if spring == '?'
                #if already on streak, must be either '.' or '#'
                if path.streak != 0:
                    if path.streak == count[path.index]:
                        path.streak = 0
                        path.index += 1
                    else:
                        path.streak += 1
                #if no current streak, must consider 2 possible Paths
                else:
                    if path in newPaths:
                        newPaths[newPaths.index(path)].mult += path.mult
                    else:
                        newPaths.append(copy.deepcopy(path))
                    path.streak += 1

            #bad if too many streaks
            if path.index == len(count) and path.streak != 0:
                continue
            if path in newPaths:
                newPaths[newPaths.index(path)].mult += path.mult
            else:
                newPaths.append(path)
        paths = newPaths
    
    sum = 0
    for path in paths:
        #only consider Paths with enough broken springs
        if path.index == len(count) or path.index == len(count)-1 and path.streak == count[-1]:
            sum += path.mult
    return sum



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
        #the "unfolded" rows/counts, x5
        row = row + '?' + row + '?' + row + '?' + row + '?' + row
        count = count + count + count + count + count
        total += possibleConfigurations(row, count)
        # print(total)
    
    print(total)

main()