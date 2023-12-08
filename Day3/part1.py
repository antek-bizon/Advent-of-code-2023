def getRigthSide(line: str, i: int, visited) -> str:
    nextIndex = i + 1
    if nextIndex < len(line) and line[nextIndex].isdigit():
        visited[nextIndex] = True
        return line[nextIndex] + getRigthSide(line, nextIndex, visited)
    return ""


def getLeftSide(line: str, i: int, visited) -> str:
    nextIndex = i - 1
    if nextIndex >= 0 and line[nextIndex].isdigit():
        visited[nextIndex] = True
        return getLeftSide(line, nextIndex, visited) + line[nextIndex]
    return ""


def getWholeNumber(line: str, i: int, visited) -> int:
    visited[i] = True
    numStr = getLeftSide(line, i, visited) + line[i] + getRigthSide(line, i, visited)
    return int(numStr)
    

def checkAround(lines, x: int, y: int, visited):
    sum = 0
    for i in range(max(y - 1, 0), min(y + 2, len(lines))):
        for j in range(max(x - 1, 0), min(x + 2, len(lines[i]))):
            c = lines[i][j]
            if c.isdigit() and visited[i][j] == False:
                num = getWholeNumber(lines[i], j, visited[i]) 
                # print(num)
                sum += num
    return sum


def main():
    file = open("data.txt", "r")
    lines = [line.strip() for line in file.readlines()]    
    file.close()
    visited = [[False for c in line] for line in lines]
    sum = 0

    for i in range(0, len(lines)):
        for j, c in enumerate(lines[i]):
            if not c.isdigit() and c != ".":
                sum += checkAround(lines, j, i, visited)                
    print(sum)


if __name__ == "__main__":
    main()
