#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops
# https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index

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
    for mirror in range(1, len(rows)):
        for i, row in enumerate(rows):
            j = mirror*2 - i - 1
            if j < 0 or j >= len(rows):
                continue
            if row != rows[j]:
                break
        #today I learned what a for-else was
        #it only runs this else block if it didn't "break" out of the above for loop
        else:
            return mirror
    return -1

#similar to findmirror(), but finds for both rows or columns, 
#   and multiplies a row mirror by 100
#   and cannot be the same as prevmirror (if prevmirror == 0, it is ignored)
# -1 if cannot find
#(this is an ugly solution, really)
#(it got 10 times uglier but it works)
def findnewmirror(rows, prevmirror):
    mirrornum = findmirror(rows) * 100
    if mirrornum == prevmirror:
        mirrornum = findmirror(rowstocolumns(rows))
        if mirrornum == -1:
            mirrornum = prevmirror
    elif mirrornum == -100:
        mirrornum = findmirror(rowstocolumns(rows))
    #reverse to check for a different mirror of the same type (row/column) 
    #   after the prev mirror
    if mirrornum == prevmirror:
        rows.reverse()
        mirrornum = findmirror(rows) * 100
        rows.reverse()
        if mirrornum == -100:
            columns = rowstocolumns(rows)
            columns.reverse()
            mirrornum = findmirror(columns)
            mirrornum = len(columns) - mirrornum
        else:
            mirrornum = len(rows)*100 - mirrornum
    return mirrornum

def main():

    with open("day13/input.txt") as file:
        grids = file.read().split("\n\n")

    allrows = []
    for grid in grids:
        allrows.append(grid.split())

    total = 0

    for rows in allrows:
        prevmirror = findnewmirror(rows, 0)
        
        #loop through every space on the board, flip its type, 
        #   and check if there is a new mirror (there should always be a new mirror for each grid)
        for i, row in enumerate(rows):
            for j, space in enumerate(row):
                if space == '.':
                    rows[i] = rows[i][:j] + '#' + rows[i][j+1:]
                else:
                    rows[i] = rows[i][:j] + '.' + rows[i][j+1:]
                
                newmirror = findnewmirror(rows, prevmirror)
                if newmirror != -1 and newmirror != prevmirror:
                    total += newmirror
                    break

                rows[i] = rows[i][:j] + space + rows[i][j+1:]
            else:
                continue
            break
        else:
            print("BAD shouldn't get here")
        # print(total)

    print(total)

main()