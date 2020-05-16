from time import time

from mejn import *
from ggen import *

# wygeneruj graf

TESTS = 10

print("n;przegladanie_dfs;przegladanie_bfs;dfs_sort_matrix;dfs_sort_list;dfs_sort_table;")

for _size in [100 * (i + 1) for i in range(10)]:
    matrix = Generator(_size).matrix
    successors_list = lista_nastepnikow(deepcopy(matrix))
    edge_table = tabela_krawedzi(deepcopy(matrix))
    print(f'{_size};', end='')

    # DFS
    _record = []
    for i in range(TESTS):
        start = time()
        przegladanie_dfs(successors_list)
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # BSF
    _record = []
    for i in range(TESTS):
        start = time()
        przegladanie_bfs(successors_list)
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # sort_bfs_by_matrix
    _record = []
    for i in range(TESTS):
        start = time()
        dfs_sort_matrix(matrix)
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # sort_bfs_by_list
    _record = []
    for i in range(TESTS):
        start = time()
        dfs_sort_list(successors_list, len(matrix))
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    # sort_bfs_by_table
    _record = []
    for i in range(TESTS):
        start = time()
        dfs_sort_table(edge_table, len(matrix))
        end = time()
        _record.append(end - start)
    print(f'{sum(_record)/10};', end='')

    print()
