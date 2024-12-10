
day: str = "05"
filepath: str = "{}/input.txt".format(day)
fileData: list[str] = []

with open("./{}".format(filepath), "r") as file:
    fileData = [line.rstrip("\n") for line in file.readlines()]

breakline: int = 0
updateCache: dict[str, list[int]] = {}
invalidOrders: list[int] = []

def createUpdateCache():
    global breakline, updateCache
    for i in range(len(fileData)):
        line = fileData[i]
        if line == "":
            breakline = i
            break
        [parent, child] = line.split("|")
        if child not in updateCache:
            updateCache[child] = []
        updateCache[child].append(int(parent))
    return None

def invalidOrder(futureUpdates: list[int], currentUpdate: str) -> bool:
    if currentUpdate not in updateCache or len(futureUpdates) == 0:
        return False

    for number in futureUpdates:
        if number in updateCache[currentUpdate]:
            return True
    return False

def part1() -> int:
    global invalidOrders
    answer: int = 0
    for i in range(breakline+1, len(fileData)):
        updateList: list[int] = [int(num) for num in fileData[i].split(",")]
        validUpdate: bool = True

        for j in range(len(updateList)):
            if j == len(updateList)-1:
                break
            if invalidOrder(updateList[j+1:], str(updateList[j])):
                invalidOrders.append(i)
                validUpdate = False
                break

        if validUpdate:
            answer += updateList[int((len(updateList)-1)/ 2)]

        pass
    return answer

def part2() -> int:
    answer: int = 0
    for i in invalidOrders:
        updateList: list[int] = [int(num) for num in fileData[i].split(",")]
        orderedList: list[int] = []

        for i in range(len(updateList)):
            current: int = updateList[i]

            if len(orderedList) == 0:
                orderedList.append(current)
                continue

            for j in range(len(orderedList)+1):
                if j == len(orderedList):
                    orderedList.append(current)
                    break

                if not invalidOrder(orderedList[j:], str(current)):
                    orderedList.insert(j, current)
                    break

        answer += orderedList[int( (len(orderedList)-1) / 2)]

    return answer

createUpdateCache()
print("Part 1 answer: {}".format(part1()))
print("Part 2 answer: {}".format(part2()))

