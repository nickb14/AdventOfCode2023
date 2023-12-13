def main():

    sum = 0

    with open("day09/input.txt") as file:
        for line in file:

            sequence = list(map(int, line.split()))
            next = sequence[0]
            alternate = -1
            while len(set(sequence)) != 1:
                for i in range(len(sequence)-1):
                    sequence[i] = sequence[i+1] - sequence[i]
                sequence = sequence[:-1]
                #similar to part one, but alternating subtracting and adding the first numbers
                next += sequence[0] * alternate
                alternate *= -1
            sum += next
    
    print(sum)

main()