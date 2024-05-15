#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop

#distance between 2 coordinates
def distance(a, b, emptyrows, emptycolumns):
    extraspace = 0
    #can iterate backwards if coordinates are ordered differently
    for x in range(a[0], b[0], 1 if a[0]<b[0] else -1 ):
        if x in emptyrows:
            extraspace += 1
    for y in range(a[1], b[1], 1 if a[1]<b[1] else -1 ):
        if y in emptycolumns:
            extraspace += 1
    return abs(b[0]-a[0]) + abs(b[1]-a[1]) + extraspace

def main():

    grid = []
    #coordinates of galaxies [x, y]
    galaxies = []
    emptyrows = set()
    emptycolumns = set()

    with open("day11/input.txt") as file:
        #emptycolumns starts with all possible columns, then columns with '#' removed
        start = file.tell()
        emptycolumns = set(range(len(file.readline().rstrip())))
        file.seek(start)

        for x, line in enumerate(file):
            grid.append(line.rstrip())
            if '#' not in line:
                emptyrows.add(x);

            for y, char in enumerate(line):
                if char == '#':
                    galaxies.append([x, y])
                    emptycolumns.discard(y)

    sum = 0

    #compares each coordinate pair without repeats
    for a in galaxies:
        for b in galaxies:
            if a < b:
                sum += distance(a, b, emptyrows, emptycolumns)

    # print(grid)
    # print(galaxies)
    # print(emptyrows)
    # print(emptycolumns)
    print(sum)

main()