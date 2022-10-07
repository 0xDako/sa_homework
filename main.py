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

    print([direct_controler, direct_subordinate, indirectly_controler, indirectly_subordinate, subordination])
    return [direct_controler, direct_subordinate, indirectly_controler, indirectly_subordinate, subordination]

reference = [[1,3],[2,3,4,5],[1],[4,5],[2,3,4,5]]

if __name__ == '__main__':
    with open('1.csv') as file:
        csvString = file.read()
        result = task(csvString)
        print(result == reference)

