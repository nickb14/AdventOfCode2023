#references
# https://www.w3schools.com/python/
# https://stackoverflow.com/questions/12933964/printing-a-list-of-objects-of-user-defined-class
# https://www.geeksforgeeks.org/dunder-magic-methods-python/

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'({self.start}, {self.end})'
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        return self.start < other.start
    
    #returns 2 lists, a new Range and old Ranges (either list could be empty)
    def addRange(self, start, end, amount):
        if start <= self.start:
            #if new range is entirely less than
            if end <= self.start:
                return [], [Range(self.start, self.end)]
            #if new range entirely encloses
            elif end >= self.end:
                return [Range(self.start+amount, self.end+amount)], []
            #if new range partially encloses the beginning
            else:
                return [Range(self.start+amount, end+amount)], [Range(end, self.end)]
        #if new range is entirely greater than
        elif start >= self.end:
            return [], [Range(self.start, self.end)]
        else:
            #if new range partially encloses the end
            if end >= self.end:
                return [Range(start+amount, self.end+amount)], [Range(self.start, start)]
            #if new range is entirely enclosed
            else:
                return [Range(start+amount, end+amount)], [Range(self.start, start), Range(end, self.end)]

def main():
    
    with open("day05/input.txt") as file:

        #lists of Ranges of seeds
        seeds = []

        seedRanges = list(map(int, file.readline().split()[1:]))
        newSeeds = []
        for i in range(0, len(seedRanges), 2):
            newSeeds.append(Range(seedRanges[i], seedRanges[i]+seedRanges[i+1]))
        
        oldSeeds = []

        for line in file:
            #for each new section, combine newSeeds with the seeds that weren't updated
            if line[0] == '\n':
                seeds += newSeeds
                newSeeds.clear()
                file.readline()
                continue

            vals = tuple(map(int, line.split()))
            #for each Range of seeds that hasn't been updated this section, check if there shold be a new Range of seeds
            for seed in seeds:
                new, old = seed.addRange(vals[1], vals[1]+vals[2], vals[0]-vals[1])
                newSeeds += new
                oldSeeds += old
            #copy oldSeeds back into seeds and reset
            seeds = oldSeeds.copy()
            oldSeeds.clear()
        
        print(min(seeds + newSeeds).start)


main()