def getInput():
    file = open("./example1.txt", "r")
    lines = file.readlines()
    file.close()
    return lines


def main():
    input = getInput()
    sum = 0
    for line in input:
        num = 0
        for c in line:
            if c.isdigit():
                num += int(c) * 10
                break
        for c in reversed(line):
            if c.isdigit():
                num += int(c)
                break
        sum += num
    print(sum)


if __name__ == '__main__':
    main()
