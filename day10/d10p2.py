#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it

def turnLeft(dir):
    if dir[0] == 0:
        return (-dir[1], 0)
    else:
        return (0, dir[0])
    
def turnRight(dir):
    if dir[0] == 0:
        return (dir[1], 0)
    else:
        return (0, -dir[0])

#returns length 2 tuple of the new direction to travel
def findDir(dir, pipe):
    if pipe in '-|':
        return dir
    elif pipe == 'L' and dir == (1, 0) or pipe == 'J' and dir == (0, 1):
        return turnLeft(dir)
    elif pipe == '7' and dir == (-1, 0) or pipe == 'F' and dir == (0, -1):
        return turnLeft(dir)
    else:
        return turnRight(dir)

def findLoc(dir, loc):
    return (loc[0]+dir[0], loc[1]+dir[1])

#I have learned recursion is limited in Python, so this probably not the best solution
def addEnclosed(loc, enclosed, locs):
    if loc not in enclosed.union(locs):
        enclosed.add(loc)
        addEnclosed(findLoc((0, 1), loc), enclosed, locs)
        addEnclosed(findLoc((0, -1), loc), enclosed, locs)
        addEnclosed(findLoc((1, 0), loc), enclosed, locs)
        addEnclosed(findLoc((-1, 0), loc), enclosed, locs)

def main():

    grid = []

    with open("day10/input.txt") as file:
        for line in file:
            if 'S' in line:
                start = (len(grid), line.index('S'))
            grid.append(list(line.rstrip()))

    #(totally bad assumption) assume pipe goes down to start
    dir = (1, 0)
    loc = findLoc(dir, start)
    dirs = [dir]
    locs = [loc]

    #find the next direction, follow that direction to the next location, until back to the start
    while loc != start:
        dir = findDir(dir, grid[loc[0]][loc[1]])
        loc = findLoc(dir, loc)
        dirs.append(dir)
        locs.append(loc)
    
    enclosed = set()
    #atrocious assumptions being made, ignoring the last tile and 
    # more importantly assuming the loop is a left-turing loop
    for i in range(len(dirs)-1):
        dir = dirs[i]
        loc = locs[i]
        #if the next turn is a right turn, check forwards
        if dirs[i+1] == turnRight(dir):
            addEnclosed(findLoc(dir, loc), enclosed, locs)
        dir = turnLeft(dir)
        addEnclosed(findLoc(dir, loc), enclosed, locs)

    #this one takes a few seconds to loop through heh
    print(len(enclosed))

main()