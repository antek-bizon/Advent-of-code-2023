def get_race(file):
    time = "".join((filter(lambda x: x.isdigit(), map(lambda x: x.strip(), file.readline().split(":")[1].split(' ')))))

    distance = "".join((filter(lambda x: x.isdigit(), map(lambda x: x.strip(), file.readline().split(":")[1].split(' ')))))

    return (int(time),int(distance))


def calc_dist(whole_time: int, press_time: int):
    return press_time * (whole_time - press_time)


def calc_posibilities(race: (int, int)) -> int:
    low = 0
    high = race[0] // 2
    mid = None
    distance = None

    while low <= high:
        mid = (high + low) // 2
        distance = calc_dist(race[0], mid)
        if distance < race[1]:
            low = mid + 1
        elif distance > race[1]:
            high = mid - 1
        else:
            break

    if distance < race[1]:
        mid += 1

    if race[0] % 2 == 0:
        mid += 1

    return 2 * (race[0] // 2 - mid + 1) + (race[0] + 1) % 2 


def main():
    file = open("example.txt", "r")

    race = get_race(file)

    print(race)

    posibilities = calc_posibilities(race)

    print(posibilities)
    
    file.close()


if __name__ == "__main__":
    main()

