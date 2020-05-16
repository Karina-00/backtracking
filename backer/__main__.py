# GRAPH REPRESENTATION


def read_graph():
    """Tworzy graf"""
    v = int(input("Podaj ilosc wierzcholkow grafu:"))
    print("Podaj kolejne wiersze macierzy sasiedztwa:")
    matrix = []
    for i in range(v):
        line = list(map(int, input(f"{i+1} linia:").split()))
        matrix.append(line)
    return matrix


def macierz_sasiedztwa(matrix: list):
    print(style("\nMacierz sasiedztwa", fg='blue'))
    headings = [" "] + [f"V{j+1}" for j in range(len(matrix))]
    i = 1
    for line in matrix:
        line.insert(0, f"V{i}")
        i += 1
    print(tabulate(matrix, headers=headings, tablefmt='orgtbl'))


def lista_nastepnikow(matrix: list):
    print(style("\nLista nastepnikow", fg='blue'))
    result = []
    result2 = []
    n = len(matrix)
    for i in range(n):
        nastepniki = []
        for j in range(n):
            if matrix[i][j] == 1:
                nastepniki.append(j + 1)
        result.append([i + 1, " -> ".join(list(map(str, nastepniki)))])
        result2.append([i + 1, nastepniki])
    print(tabulate(result, headers=['V', 'lista'], tablefmt='orgtbl'))
    return result2


def next_by_list(list, i):
    return list[i][1]


# MAIN --- HOME #

def main(argv):
    pass
