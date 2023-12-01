def getInput():
    file = open("./data1.txt", "r")
    lines = file.readlines()
    file.close()
    return lines


def getCorrectNumber(line: str) -> int:
    nums = []
    for i, c in enumerate(line):
        if c.isdigit():
            nums.append((i, int(c)))

    elementsToFind = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, e in enumerate(elementsToFind):
        index = 0
        while True:
            index = line.find(e, index)
            if index == -1:
                break
            nums.append((index, i + 1))
            index += 1

    nums.sort()
    num = nums[0][1] * 10 + nums[-1][1]
    return num


def main():
    input = getInput()
    sum = 0
    for line in input:
        sum += getCorrectNumber(line)
    print(sum)


if __name__ == "__main__":
    main()
