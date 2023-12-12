#references
# https://www.w3schools.com/python/
# https://rollbar.com/blog/python-recursionerror/

def main():

    with open("day08/input.txt") as file:
        #instead of Ls and Rs, tuple of 0s and 1s for easy indexing
        line = file.readline().rstrip().replace('L', '0').replace('R', '1')
        dirs = tuple(map(int, line))
        file.readline()

        #dictionary, values of length 2 tuples
        network = {}
        for line in file:
            network[line[:3]] = (line[7:10], line[12:15])
        
        loc = 'AAA'
        step = 0
        while loc != 'ZZZ':
            #step%len(dirs) to loop over dirs multiple times
            loc = network[loc][dirs[step%len(dirs)]]
            step += 1
        print(step)

main()