day: str = "01"
filepath: str = "{}/input.txt".format(day)

with open("./{}".format(filepath), "r") as file:
    fileData = file.readlines()

list1: list[int] = []
list2: list[int] = []

def createLists():
    global list1, list2
    for line in fileData:
        [element1, element2] = [int(num) for num in line.split("   ")]
        list1.append(element1)
        list2.append(element2)
    list1.sort()
    list2.sort()

def part1() -> int:
    answer: int = 0
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            answer += list1[i] - list2[i]
        else:
            answer += list2[i] - list1[i]
    return answer

def part2() -> int:
    cache: dict[int, int] = {}
    answer: int = 0
    for i in range(len(list1)):
        number: int = list1[i]

        if number in cache:
            answer += cache[number]
            continue

        cache[number] = number * list2.count(number)
        answer += cache[number]

    return answer

createLists()
print("Part 1 answer: {}".format(part1()))
print("Part 2 answer: {}".format(part2()))

