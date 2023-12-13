#references
# https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-and-how-to-increase-it

#returns length 2 tuple of the new direction to travel
def findDir(dirEnter, pipeType):
    if pipeType in '-|':
        return dirEnter
    elif pipeType == 'L':
        if dirEnter == (1, 0):
            return (0, 1)
        else:
            return (-1, 0)
    elif pipeType == 'J':
        if dirEnter == (1, 0):
            return (0, -1)
        else:
            return (-1, 0)
    elif pipeType == '7':
        if dirEnter == (-1, 0):
            return (0, -1)
        else:
            return (1, 0)
    elif pipeType == 'F':
        if dirEnter == (-1, 0):
            return (0, 1)
        else:
            return (1, 0)
    else:
        print("bad pipe reached!")
        print(pipeType)
        quit()

def main():

    grid = []

    with open("day10/input.txt") as file:
        for line in file:
            if 'S' in line:
                start = (len(grid), line.index('S'))
            grid.append(list(line.rstrip()))

    #(totally bad assumption) assume pipe goes down to start
    dir = (1, 0)
    loc = (start[0]+dir[0], start[1]+dir[1])
    step = 1

    #find the next direction, follow that direction to the next location, until back to the start
    while loc != start:
        dir = findDir(dir, grid[loc[0]][loc[1]])
        loc = (loc[0]+dir[0], loc[1]+dir[1])
        step += 1
    
    halfway = int((step+1) / 2)
    print(halfway)

main()