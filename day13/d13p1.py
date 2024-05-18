#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops

#or columns to rows
def rowstocolumns(rows):
    columns = [""] * len(rows[0])
    for row in rows:
        for i, space in enumerate(row):
            columns[i] += space
    return columns

#works the same for columns
#returns the mirror number, or -1 if it can't find it
def findmirror(rows):
    for mirrornum in range(1, len(rows)):
        for i, row in enumerate(rows):
            j = mirrornum*2 - i - 1
            if j < 0 or j >= len(rows):
                continue
            if row != rows[j]:
                break
        #today I learned what a for-else was
        #it only runs this else block if it didn't "break" out of the above for loop
        else:
            return mirrornum
    return -1

def main():

    with open("day13/input.txt") as file:
        grids = file.read().split("\n\n")

    allrows = []
    for grid in grids:
        allrows.append(grid.split())

    total = 0

    for rows in allrows:
        mirror = findmirror(rows)
        if mirror != -1:
            total += mirror * 100
        else:
            total += findmirror(rowstocolumns(rows))

    print(total)

main()