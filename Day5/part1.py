class RangeMap:
    def __init__(self, dest, src, range):
        self.dest = dest
        self.src = src
        self.range = range

    def __str__(self):
        return f"dest: {self.dest}, src: {self.src}, range: {self.range}"

    def tryGet(self, entry: int) -> (bool, int):
        diff = entry - self.src
        if diff >= 0 and diff < self.range:
            return (True, self.dest + diff)

        return (False, 0)
            
def getNumsInLine(line: str) -> list:
    return list(map(lambda x: int(x), filter(lambda x: x != " ", line.strip().split(" "))))


def getRangeMap(line: str) -> RangeMap:
    dest, src, range = getNumsInLine(line)    
    return RangeMap(dest, src, range)
    

def main():
    file = open("data.txt", "r")
    
    seeds = getNumsInLine(file.readline().split(":")[1])
    maps = []
    for line in file.readlines():
        if len(line) < 2:
            continue
        if line[0].isdigit():
            maps[-1].append(getRangeMap(line))
        else:
            maps.append([])

    locations = []

    for seed in seeds:
        entry = seed
        for map in maps:
            for range in map:
                ok, val = range.tryGet(entry)
                if ok:
                    entry = val
                    break
        
        locations.append(entry)

    print(min(locations))
        
    file.close()


if __name__ == "__main__":
    main()
