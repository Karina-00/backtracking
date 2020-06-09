from sys import argv
from copy import deepcopy

from tabulate import tabulate
from click import *

from backer.ggen import Generator
from backer.euler import euler
from backer.hamilton import hamilton
from backer.graph_utils import *


@command()
@option('-n', '--vert', '_opt_vert', default=10, help='set number of vertixes')
@option('-R', '--read', '_opt_read', default=False, is_flag=True, help='read graph\'s matrix trom stdin')
@option('-r', '--rand', '_opt_rand', default=0.50, help='generate random graph w/ set density (approx., 1=100%)')
@option('-H', '--non-hamiltonian', '_opt_nonh', default=False, is_flag=False, help='w/ --rand; generate non-hamiltonian graph')
def cli(_opt_vert, _opt_read, _opt_rand, _opt_nonh):
    if _opt_rand:
        _gen_size = int(_opt_vert) if _opt_vert else int(
            input("set number of vertexes-:"))

        hamiltonian = not _opt_nonh
        density = _opt_rand

        graph = Generator(_gen_size, density, hamiltonian)

        matrix = graph.matrix()
        lista = graph.lista()

    elif _opt_read:
        matrix = read_graph()
        lista = lista_nastepnikow(deepcopy(matrix))

    while True:
        try:
            n = int(input(style("\n(0) Wyjscie\n"
                                "(1) Znajdź cykl Hamiltona\n"
                                "(2) Znajdź cykl Eulera\n"
                                "(3) Wyświetl w postaci listy następników\n"
                                "(4) Wyświetl w postaci tabeli krawędzi\n"
                                "(5) Wyświetl w postaci macierzy sąsiedztwa\n", fg='black', bold=True) +
                          "    Wybierz dzialanie [0/1/2/3/4/5] -> "))
        except ValueError:
            print(style("[!] Nalezy podac liczbe z zakresu 0..5", fg='red'))
            continue

        if n == 0:
            break
        elif n == 1:
            print(style("\nCykl Hamiltona", fg='blue'))
            print(hamilton(lista))
        elif n == 2:
            print(style("\nCykl Eulera", fg='blue'))
            print(euler(deepcopy(matrix)))
        elif n == 3:
            successors_list = lista_nastepnikow(deepcopy(matrix))
        elif n == 4:
            print("Tabela krawedzi?")
            edge_table = tabela_krawedzi(deepcopy(matrix))
        elif n == 5:
            macierz_sasiedztwa(deepcopy(matrix))
        else:
            print("Nalezy podac liczbe 0-5.")
            continue
