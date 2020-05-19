from sys import argv
from random import randint


def _random_pair(size):
    return randint(0, size - 1), randint(0, size - 1)


def _min_rich(size, constr):
    return constr * (size * (size - 1) // 2)


def _randomize_matrix(arr):
    l = len(arr)
    for i in range(_min_rich(l)):
        x, y = randint(0, l - 1), randint(0, l - 1)
        arr[x][y] = 0
        arr[y][x] = 0

    return arr


def list_to_matrix(s_list):
    n = len(s_list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for el in s_list[i]:
            matrix[i][el] = matrix[el][i] = 1
    return matrix


class FriendList:
    def __init__(self, list):
        self.list = list

    def friends_of(self, vertex):
        pos = self.list.index(vertex)
        return [
            vertex,
            self.list[pos - 1],
            self.list[pos + 1]
        ]


def _rich(graph):
    tab = []
    for i in range(len(graph)):
        tab += graph[i]
    print(tab)
    return len(tab)


def gen_list(size, constr):
    list = [i + 1 for i in range(size - 1)]
    for i in range(size):
        a, b = _random_pair(size - 1)
        list[a], list[b] = list[b], list[a]
    list = [*list, 0]
    way = {}
    way[0] = [list[0]]
    print(list)

    for i in range(size - 1):
        way[list[i]] = [list[i + 1]]

    #
    list = FriendList(list)

    while _rich(way) < _min_rich(size, constr):
        i = randint(1, size - 2)
        a, b = i, i
        forbiden = list.friends_of(i)
        while a in forbiden or b in forbiden:
            a, b = _random_pair(size)
            print(a, b)
        way[i].append(a)
        way[i].append(b)

    for i in range(size):
        a, b = _random_pair(len(way[i]))
        way[i][a], way[i][b] = way[i][b], way[i][a]

    return(way)


class Generator:
    def __init__(self, size, density, hamilton):
        self.size

    def matrix(self):
        pass


if __name__ == '__main__':
    # _cli()
    print(
        gen_list(20, 0.5)
    )
