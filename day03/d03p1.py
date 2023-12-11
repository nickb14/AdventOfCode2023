#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
# https://stackoverflow.com/questions/2909106/whats-a-correct-and-good-way-to-implement-hash
# https://stackoverflow.com/questions/15148496/passing-an-integer-by-reference-in-python
# https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-for-equality-against-a-single-value

#hashable 2D point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __key(self):
        return (self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__key() == other.__key()
        else:
            return NotImplemented
    
    def __hash__(self):
        return hash(self.__key())

#stores a number and its set of locations on the grid
class Number:
    def __init__(self, num, x, y):
        self.num = int(num)
        self.points = set()
        for i in range(len(num)):
            self.points.add(Point(x, y-i))

def numberFound(line, x, y, numbers):
    num = line[y]
    while line[y+1].isdecimal():
        num += line[y+1]
        y += 1
    numbers.append(Number(num, x, y))
    return y

def symbolFound(x, y, validPoints):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0):
                validPoints.add(Point(x+i, y+j))

def main():

    numbers = []
    validPoints = set()

    with open("day03/input.txt") as file:

        #loop through like a 2D array, at point x, y
        x = 0
        for line in file:
            y = 0
            while y < len(line):
                #a number is found, find the entire number and store it
                if line[y].isdecimal():
                    y = numberFound(line, x, y, numbers)
                #a symbol is found, store all of its adjecent points
                elif line[y] not in {'.', '\n'}:
                    symbolFound(x, y, validPoints)
                y += 1
            x += 1

    sum = 0
    for number in numbers:
        #if at least one of the points in number is also in validPoints
        if len(validPoints.intersection(number.points)) > 0:
            sum += number.num
    print(sum)

main()