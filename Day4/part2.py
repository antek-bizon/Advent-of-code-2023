def isNumber(c: str) -> bool:
    return c.isdigit()


def parseInt(c: str) -> bool:
    return int(c)


def getNumbers(string):
    return map(parseInt, filter(isNumber, string.strip().split(" ")))
    

def getCorrect(winNums: set, nums: list):
    correct = 0

    for num in nums:
        if num in winNums:
            correct += 1
        
    return correct
    

def main():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()
    
    cardsCount = [1 for line in lines]

    for i, line in enumerate(lines):
        winNums, restNums = line.split("|")
        winNums = set(getNumbers(winNums.split(":")[1]))
        restNums = list(getNumbers(restNums))
        correct = getCorrect(winNums, restNums)
        for j in range(i + 1, i + 1 + correct):
            cardsCount[j] += cardsCount[i]

    print(sum(cardsCount))


if __name__  == "__main__":
    main()

