def main():

    sum = 0

    with open("day02/input.txt") as f:
        line = f.readline()
        while line:

            minCubes = {'red': 0, 'green': 0, 'blue': 0}
            values = line.split()
            for i in range(2, len(values), 2):
                color = values[i+1].rstrip(',;')
                minCubes[color] = max(minCubes[color], int(values[i]))
            sum += minCubes['red'] * minCubes['green'] * minCubes['blue']
        
            line = f.readline()

    print(sum)
    
main()