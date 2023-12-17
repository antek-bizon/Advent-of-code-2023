class RangeMap:
    def __init__(self, dest: int, src: int, range: int):
        self.dest = dest
        self.destEnd = dest + range - 1
        self.src = src
        self.srcEnd = src + range - 1

    def __str__(self):
        return f"dest: {self.dest}, destEnd: {self.destEnd}, src: {self.src}, srcEnd: {self.srcEnd}"

    def union(self, interval):
        # print("---------check---------")
        # print(self)
        # print(interval)

        commonStart = max(self.src, interval[0])
        commonEnd = min(self.srcEnd, interval[1])

        if commonStart <= commonEnd:
            diffStart = commonStart - self.src
            diffEnd = commonEnd - self.srcEnd
            # print("1", self.dest + diffStart, self.destEnd + diffEnd)
            return ((commonStart, commonEnd), (self.dest + diffStart, self.destEnd + diffEnd))

        return None


            
def getNumsInLine(line: str) -> list:
    return list(map(lambda x: int(x), filter(lambda x: x != " ", line.strip().split(" "))))


def getRangeMap(line: str) -> RangeMap:
    dest, src, range = getNumsInLine(line)    
    return RangeMap(dest, src, range)


def getSeedsWithRanges(seeds: list) -> list:
    return [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]


def interval_difference(interval_A, interval_B):
    result = []

    # Check if intervals overlap
    if interval_A[1] < interval_B[0] or interval_A[0] > interval_B[1]:
        # If there is no overlap, return interval A as the difference
        result.append(interval_A)
    else:
        # Compute the difference when there is an overlap
        if interval_A[0] < interval_B[0]:
            result.append((interval_A[0], min(interval_A[1], interval_B[0] - 1)))
        if interval_A[1] > interval_B[1]:
            result.append((max(interval_A[0], interval_B[1] + 1), interval_A[1]))

    return result


def findMin(maps, mapIndex: int, toCheck) -> int:
    if mapIndex >= len(maps):
        # print("return", toCheck)
        return toCheck[0]

    minVal = None
    
    commonParts = []
    for rangeMap in maps[mapIndex]:
        common = rangeMap.union(toCheck)
        if common is None:
            continue
        commonParts.append(common)

    diff = [toCheck]
    for common in commonParts:
        nextDiff = []
        while diff:
            interval = diff.pop()
            nextDiff.extend(interval_difference(interval, common[0]))
        diff = nextDiff
    
    diff.extend(map(lambda x: x[1], commonParts))

    for parts in diff:
        val = findMin(maps, mapIndex + 1, parts)
        if minVal is None:
            minVal = val
        else:
            minVal = min(minVal, val)

    return minVal


def main():
    file = open("data.txt", "r")
    
    seeds = getSeedsWithRanges(getNumsInLine(file.readline().split(":")[1]))
    maps = []
    for line in file.readlines():
        if len(line) < 2:
            continue
        if line[0].isdigit():
            maps[-1].append(getRangeMap(line))
        else:
            maps.append([])

    minVal = None
    # seed = seeds[1]
    # findMin(maps, 0, seed)
    # for rangeMap in maps[0]:
    #     print(rangeMap.intersectionUnion(seed))
    for seed in seeds:
        val = findMin(maps, 0, seed)
        if minVal is None:
            minVal = val
        else:
            minVal = min(minVal, val)
        
    print(minVal)    
    
    file.close()


if __name__ == "__main__":
    main()

