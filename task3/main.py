from io import StringIO
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')

    struct = []
    for row in reader:
        struct.append(row)
    print(struct)

    direct_controler = []
    for i in struct:
        print(i)
        direct_controler.append(i[0])
    direct_controler = list(map(int, set(direct_controler)))
    direct_controler.sort()

    direct_subordinate = []
    for i in struct:
        direct_subordinate.append(i[1])
    direct_subordinate = list(map(int, set(direct_subordinate)))
    direct_subordinate.sort()

    indirectly_controler = []
    for i in struct:
        for j in struct:
            if j[0] == i[1]:
                indirectly_controler.append(i[0])
    indirectly_controler = list(map(int, set(indirectly_controler)))
    indirectly_controler.sort()

    indirectly_subordinate = []
    for i in struct:
        for j in struct:
            if j[1] == i[0]:
                indirectly_subordinate.append(i[1])
    indirectly_subordinate = list(map(int, set(indirectly_subordinate)))
    indirectly_subordinate.sort()

    subordination = []

    max_node = -1
    for i in struct:
        if max_node < max(*map(int,i)):
            max_node = max(*map(int,i))

    depths = [-1 for _ in range(max_node)]

    depths[0] = 0
    for i in range(max_node):
        for j in struct:
            if int(j[0]) - 1 != i:
                continue
            depths[int(j[1]) - 1] = depths[int(j[0]) - 1] + 1

    for i in range(max_node):
        for j in range(max_node):
            if depths[i] == depths[j] and i != j:
                subordination.append(i + 1)
                subordination.append(j + 1)

    subordination = list(map(int, set(subordination)))
    subordination.sort()

    return [direct_controler, direct_subordinate, indirectly_controler, indirectly_subordinate, subordination]

reference = [[1,3],[2,3,4,5],[1],[4,5],[2,3,4,5]]

if __name__ == '__main__':
    with open('1.csv') as file:
        csvString = file.read()
        result = task(csvString)
        print(result == reference)

