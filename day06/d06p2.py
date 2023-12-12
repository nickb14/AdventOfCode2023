#references
# https://www.w3schools.com/python/
# https://realpython.com/python-range/#the-history-of-pythons-range-function

def main():

    with open("day06/input.txt") as file:

        maxTime = int(file.readline()[5:-1].replace(' ', ''))
        minScore = int(file.readline()[9:].replace(' ', ''))

        #t1 minimum time to beat the score
        for t1 in range(maxTime):
            if t1*(maxTime-t1) > minScore:
                break
        #t2 maximum time that beats the score
        for t2 in range(maxTime, 0, -1):
            if t2*(maxTime-t2) > minScore:
                break
        #+1, because range of times include the maximim time
        print(t2-t1+1)

main()