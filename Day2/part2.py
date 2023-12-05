def splitDraw(s: str):
    arr = s.split(",")
    for i in range(len(arr)):
        single = arr[i].split()
        arr[i] = (int(single[0]), single[1])
    return arr


def getId(gameWithId: str) -> int:
    return int(gameWithId.split()[1])


def getPowerOfGame(game) -> int:
    maxes = {"red": 0, "green": 0, "blue": 0}
    for draws in game:
        for draw in draws:
            num, color = draw
            if maxes[color] < num:
                maxes[color] = num

    power = 1
    for value in maxes.values():
        power *= value
    return power

def main():
    file = open("data.txt", "r")
    sum = 0
    for line in file.readlines():
        gameWithId, tail = line.split(":")
        game = list(map(splitDraw, tail.split(";")))
        sum += getPowerOfGame(game)
    print(sum)
    file.close()  


if __name__ == "__main__":
    main()
