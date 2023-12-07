def main():

    sum = 0
    
    with open("day01/input.txt") as f:
            line = f.readline()
            while line:

                lineDecimals = ''
                for c in line:
                    if c.isdecimal():
                         lineDecimals += c
                
                sum += int(lineDecimals[0] + lineDecimals[-1])
                
                line = f.readline()
    
    print(sum)
main()