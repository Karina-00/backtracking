from sys import argv
from copy import deepcopy

from tabulate import tabulate
from click import *

from backer.ggen import Generator
from backer.euler import euler
from backer.hamilton import hamilton
from backer.graph_utils import *


def read_graph():
    v = int(input("Podaj ilosc wierzcholkow grafu: "))
    print("Podaj kolejne wiersze macierzy sasiedztwa: ")
    matrix = []
    for i in range(v):
        line = list(map(int, input(f"{i + 1} linia:").split()))
        matrix.append(line)
    return matrix


def macierz_sasiedztwa(matrix: list):
    print(style("\nMacierz sasiedztwa", fg='blue'))
    headings = [" "] + [f"V{j}" for j in range(len(matrix))]
    i = 0
    for line in matrix:
        line.insert(0, f"V{i}")
        i += 1
    print(tabulate(matrix, headers=headings, tablefmt='orgtbl'))


def lista_nastepnikow(matrix: list):
    print(style("\nLista nastepnikow", fg='blue'))
    _result = []
    result = {}
    n = len(matrix)

    for i in range(n):
        nastepniki = []
        for j in range(n):
            if matrix[i][j] == 1:
                nastepniki.append(j)
        _result.append([i, " -> ".join(list(map(str, nastepniki)))])
        result[i] = nastepniki

    print(tabulate(_result, headers=['V', 'lista'], tablefmt='orgtbl'))
    return result


def tabela_krawedzi(matrix):
    print(style("\nTabela krawedzi", fg='blue'))
    n = len(matrix)
    table = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table.append([i, j])
    print(tabulate(table, headers=["out", "in"], tablefmt='orgtbl'))
    return table


def next_by_list(list, i):
    return list[i][1]
