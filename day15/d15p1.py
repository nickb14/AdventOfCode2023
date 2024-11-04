#references
# https://www.toppr.com/guides/python-guide/questions/how-do-i-get-the-ascii-value-of-a-character-in-python-and-python-3/

def main():

    with open("day15/input.txt") as file:
        input = file.readline().split(',')

    total = 0
    for s in input:

        #HASH algorithm
        current = 0
        for c in s:
            current += ord(c)
            current *= 17
            current %= 256
        total += current

    print(total)


main()