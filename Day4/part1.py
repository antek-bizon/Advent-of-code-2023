def isNumber(c: str) -> bool:
    return c.isdigit()


def parseInt(c: str) -> bool:
    return int(c)


def getNumbers(string):
    return map(parseInt, filter(isNumber, string.strip().split(" ")))
    

def getPoints(winNums: set, nums: list):
    correct = 0

    for num in nums:
        if num in winNums:
            correct += 1
        
    if correct == 0:
        return 0
    
    return 2 ** (correct - 1)
    

def main():
    file = open("data.txt", "r")

    sum = 0

    for line in file.readlines():
        winNums, restNums = line.split("|")
        winNums = set(getNumbers(winNums.split(":")[1]))
        restNums = list(getNumbers(restNums))
        sum += getPoints(winNums, restNums)

    print(sum)
    file.close()


if __name__  == "__main__":
    main()
