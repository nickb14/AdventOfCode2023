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

#stores a number and its set of locations (including adjacent points) on the grid
class Number:
    def __init__(self, num, x, y):
        self.num = int(num)
        self.points = set()
        for n in range(len(num)):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.points.add(Point(x+i, y-n+j))


def numberFound(line, x, y, numbers):
    num = line[y]
    while line[y+1].isdecimal():
        num += line[y+1]
        y += 1
    numbers.append(Number(num, x, y))
    return y

def main():

    numbers = []
    astericks = set()

    with open("day03/input.txt") as file:

        #loop through like a 2D array, at point x, y
        x = 0
        for line in file:
            y = 0
            while y < len(line):
                #a number is found, find the entire number and store it
                if line[y].isdecimal():
                    y = numberFound(line, x, y, numbers)
                #an asterisk is found, store its location
                elif line[y] not in {'.', '\n'}:
                    astericks.add(Point(x, y))
                y += 1
            x += 1

    sum = 0
    for asterick in astericks:
        nums = []
        for number in numbers:
            if asterick in number.points:
                nums.append(number.num)
        if len(nums) == 2:
            sum += nums[0] * nums[1]
    print(sum)

main()