#references
# https://www.w3schools.com/python/
# https://www.geeksforgeeks.org/python-check-if-all-elements-in-a-list-are-identical/
# https://www.cuemath.com/numbers/lcm-least-common-multiple/
# https://byjus.com/maths/lcm/#formula

def findSteps(starts, dirs, network):
    steps = []
    ends = []
    for loc in starts:
        #always take at least 1 step
        loc = network[loc][dirs[0]]
        step = 1
        while loc[2] != 'Z':
            loc = network[loc][dirs[step%len(dirs)]]
            step += 1
        steps.append(step)
        ends.append(loc)
    return steps, ends

def findLCM(first, second):
    #highest common factor
    for HCF in range(min(first, second), 0, -1):
        if first%HCF == 0 and second%HCF == 0:
            break
    return int(first * second / HCF)

def main():

    with open("day08/input.txt") as file:
        #instead of Ls and Rs, tuple of 0s and 1s for easy indexing
        line = file.readline().rstrip().replace('L', '0').replace('R', '1')
        dirs = tuple(map(int, line))
        file.readline()

        #dictionary, values of length 2 tuples
        network = {}
        starts = []
        for line in file:
            network[line[:3]] = (line[7:10], line[12:15])
            if line[2] == 'A':
                starts.append(line[:3])

        steps, ends = findSteps(starts, dirs, network)
        endLoopSteps, ends = findSteps(ends, dirs, network)

        #so apparently, the initial steps it takes for each of the start points to reach an end
        # is the same number of steps it takes for each end point to loop back around to itself again,
        # so we just need to find the least common multiple of these numbers
        assert(steps == endLoopSteps)

        #least common multiple
        LCM = steps[0]
        for i in range(1, len(steps)):
            LCM = findLCM(LCM, steps[i])
        print(LCM)

main()