def main():

    numbers = {'zero': '0',
               'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}
    sum = 0
    
    with open("day01/input.txt") as f:
        line = f.readline()
        while line:

            lineDecimals = ''
            for i in range(len(line)):
                num = line[i]
                if num.isdecimal():
                    lineDecimals += num
                else:
                    for j in range(3, 6):
                        num = line[i:i+j]
                        if num in numbers:
                            lineDecimals += numbers[num]
                            break
            
            sum += int(lineDecimals[0] + lineDecimals[-1])
            
            line = f.readline()
    
    print(sum)
    # try again
main()