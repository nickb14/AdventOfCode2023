def main():

    sum = 0

    with open("day09/input.txt") as file:
        for line in file:

            sequence = list(map(int, line.split()))
            next = sequence[-1]
            while len(set(sequence)) != 1:
                for i in range(len(sequence)-1):
                    sequence[i] = sequence[i+1] - sequence[i]
                sequence = sequence[:-1]
                #the next in the original sequence is the sum of the last numbers of these subsequent sequences
                next += sequence[-1]
            sum += next
    
    print(sum)

main()