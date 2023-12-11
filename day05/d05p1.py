#refernces
# https://www.w3schools.com/python/

def main():
    
    with open("day05/input.txt") as file:

        seeds = set()
        newSeeds = set(map(int, file.readline().split()[1:]))
        oldSeeds = set()

        for line in file:
            #for each new section, combine newSeeds with the seeds that weren't updated
            if line[0] == '\n':
                seeds.update(newSeeds)
                newSeeds.clear()
                file.readline()
                continue

            vals = tuple(map(int, line.split()))
            #for each seed that hasn't been updated this section, check if it should be a newSeed
            for seed in seeds:
                if seed in range(vals[1], vals[1]+vals[2]):
                    newSeeds.add(seed + vals[0]-vals[1])
                    oldSeeds.add(seed)
            #if a seed became a newSeed this section, also remove it from seeds
            seeds.symmetric_difference_update(oldSeeds)
            oldSeeds.clear()
        
        print(min(seeds.union(newSeeds)))

    

main()