#references
# https://www.w3schools.com/python/

def flipgrid(rows):
    columns = [""] * len(rows[0])
    for row in rows:
        for i, space in enumerate(row):
            columns[i] += space
    return columns

def main():

    with open("day14/input.txt") as file:
        grid = file.read().split()

    #change to list of columns
    grid = flipgrid(grid)
    maxvalue = len(grid[0])

    total = 0
    
    #calculate load, checking each rounded rock, updating value after each rock found
    for column in grid:
        value = maxvalue
        for i, space in enumerate(column):
            if space == 'O':
                total += value
                value -= 1
            elif space == '#':
                value = maxvalue - i - 1

    print(total)


main()