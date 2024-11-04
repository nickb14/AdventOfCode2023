#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
# https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/

def HASH(s):
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current

def main():

    with open("day15/input.txt") as file:
        input = file.readline().split(',')

    #dict, key: box number, value: 2 lists, a list of labels and a list of focal lengths
    boxes = {}

    for step in input:
        if '-' in step:
            label = step[:-1]
            box = HASH(label)
            if box in boxes:
                #if label exists, remove it
                if label in boxes[box][0]:
                    i = boxes[box][0].index(label)
                    boxes[box][0].pop(i)
                    boxes[box][1].pop(i)
                    #if there is nothing in a box, remove it from the dictionary
                    if not boxes[box][0]:
                        boxes.pop(box)
        else: #if '=' in step
            label = step[:-2]
            length = step[-1:]
            box = HASH(label)
            if box in boxes:
                if label in boxes[box][0]:
                    #if the box exists and the label exists, replace the lens
                    i = boxes[box][0].index(label)
                    boxes[box][1][i] = length
                else:
                    #if the box exists but the label doesn't exist, add the lens
                    boxes[box][0].append(label)
                    boxes[box][1].append(length)
            else:
                #if the box is empty, add the lens
                boxes[box] = [[label], [length]]
    
    total = 0
    for box in boxes:
        for i in range(len(boxes[box][1])):
            total += (box+1) * (i+1) * int(boxes[box][1][i])
    print(total)

main()