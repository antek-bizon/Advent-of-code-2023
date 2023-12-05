def splitDraw(s: str):
    arr = s.split(",")
    for i in range(len(arr)):
        single = arr[i].split()
        arr[i] = (int(single[0]), single[1])
    return arr


def getId(gameWithId: str) -> int:
    return int(gameWithId.split()[1])


def checkPossibility(game, limits) -> bool:
    for draws in game:
        for draw in draws:
            num, color = draw
            if limits[color] < num:
                return False
    return True


def main():
    file = open("data.txt", "r")
    limits = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for line in file.readlines():
        gameWithId, tail = line.split(":")
        game = list(map(splitDraw, tail.split(";")))
        if checkPossibility(game, limits):
            sum += getId(gameWithId)
    print(sum)
    file.close()  


if __name__ == "__main__":
    main()
