#references
# https://www.w3schools.com/python/

def main():
    
    with open("day06/input.txt") as file:

        times = list(map(int, file.readline().split()[1:]))
        distances = list(map(int, file.readline().split()[1:]))

        product = 1
        for i in range(len(times)):
            number = 0
            maxTime = times[i]
            for t in range(maxTime+1):
                #a calculation for the distance traveled given the timings
                distance = t * (maxTime-t)
                if distance > distances[i]:
                    number += 1
            product *= number
        print(product)

main()