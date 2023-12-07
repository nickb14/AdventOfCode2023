def main():

    maxCubes = {'red': 12, 'red,': 12, 'red;': 12,
                'green': 13, 'green,': 13, 'green;': 13,
                'blue': 14, 'blue,': 14, 'blue;': 14}
    sum = 0

    with open("day02/input.txt") as f:
        line = f.readline()
        while line:

            values = line.split()
            id = int(values[1][:-1])
            for i in range(2, len(values), 2):
                if int(values[i]) > maxCubes[values[i+1]]:
                    id = 0
                    break
            sum += id
        
            line = f.readline()

    print(sum)
    
main()