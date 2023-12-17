def get_races(file):
    times = list(filter(lambda x: x.isdigit(), map(lambda x: x.strip(), file.readline().split(":")[1].split(' '))))

    distances = list(filter(lambda x: x.isdigit(), map(lambda x: x.strip(), file.readline().split(":")[1].split(' '))))


    return [(int(times[i]), int(distances[i])) for i in range(0, len(times))]


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

# def brute_force(race: (int, int)):
#     posibilities = 0
#     for i in range(0, race[0]):
#         if calc_dist(race[0], i) > race[1]:
#             posibilities += 1

#     return posibilities 
    

def main():
    file = open("data.txt", "r")

    races = get_races(file)
    result = 1

    for race in races:
        posibilities = calc_posibilities(race)
        # posibilities = brute_force(race)
        print(posibilities)
        result *= posibilities

    print(result)
    
    file.close()


if __name__ == "__main__":
    main()
