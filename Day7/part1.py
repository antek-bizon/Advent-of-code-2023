def count_symbols(hand: str) -> list:
    counter = {}
    for c in hand:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return sorted(list(counter.values()), reverse=True)


def get_hand_value(hand: str) -> str:
    result = ""
    symbol_values = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "D",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M"
    }

    for i, c in enumerate(hand):
        result += symbol_values[c]

    return result
    
    
def parse_line(line: str) -> (str, int, int):
    hand, bid = filter(lambda x: x != "", map(lambda x: x.strip(), line.split(" ")))
    counted = count_symbols(hand) 
    value = 0

    if counted[0] > 3:
        value = counted[0] + 2
    elif 3 in counted:
        value = 4
        if 2 in counted:
            value += 1
    else:
        pars = 0
        for count in counted:
            if count < 2:
                break
            pars += 1
        value = min(pars, 2) + 1
        
    return (value, get_hand_value(hand), int(bid))


def main():
    file = open("data.txt", "r")
    buckets = {}

    for line in file.readlines():
        bucket_key, hand, bid = parse_line(line)
        to_append = (hand, bid)
        if bucket_key in buckets:
            buckets[bucket_key].append(to_append)
        else:
            buckets[bucket_key] = [to_append]

    for key in buckets:
        buckets[key].sort(reverse=True)

    total_points = 0
    rank = 1
    for key in sorted(buckets.keys()):
        for _, bid in buckets[key]:
            # print(rank, bid)
            total_points += rank * bid 
            rank += 1

    print(total_points)

    file.close()


if __name__ == "__main__":
    main()
