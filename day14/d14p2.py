#references
# https://www.w3schools.com/python/

#clockwise rotate
def rotategrid(grid):
    newgrid = [""] * len(grid[0])
    for row in grid:
        for i, space in enumerate(row):
            newgrid[i] = space + newgrid[i]
    return newgrid

#round rocks roll to the left
def tiltgrid(grid):
    newgrid = []
    for row in grid:
        newrow = ""
        emptyindex = 0
        for i, space in enumerate(row):
            if space == 'O':
                newrow = newrow[:emptyindex] + 'O' + newrow[emptyindex:]
                emptyindex += 1
            elif space == '#':
                newrow += '#'
                emptyindex = i + 1
            else:
                newrow += '.'
        newgrid.append(newrow)
    return newgrid

#tilt and rotate x4
def spincycle(grid):
    for i in range(4):
        grid = tiltgrid(grid)
        grid = rotategrid(grid)
    return grid

#load to the north (to the left)
def calculateload(grid):
    total = 0
    for row in grid:
        value = len(row)
        for space in row:
            if space == 'O':
                total += value
            value -= 1
    return total

#assuming north is to the left, prints north upwards
#(for testing)
def printgrid(grid):
    grid = rotategrid(grid)
    for row in grid:
        print(row)
    print()
    grid = rotategrid(grid)
    grid = rotategrid(grid)
    grid = rotategrid(grid)

def main():

    with open("day14/input.txt") as file:
        grid = file.read().split()
    
    #by default, a grid's "north" is represented as to the left
    grid = rotategrid(grid)
    grid = rotategrid(grid)
    grid = rotategrid(grid)

    grids = []

    #assuming there is a repeat
    trycycles = 1000
    for i in range(trycycles):
        grid = spincycle(grid)
        if grid in grids:
            break
        grids.append(grid)
    else:
        print("fail, no repeats after " + str(trycycles) + " cycles")
        return 0
    
    #pattern loops every "loopcycles" cycles, starting at "startcycle"
    startcycle = grids.index(grid)
    loopcycles = i - startcycle

    remainingcycles = (1000000000 - startcycle - 1) % loopcycles
    for i in range(remainingcycles):
        grid = spincycle(grid)
    
    print(calculateload(grid))

main()