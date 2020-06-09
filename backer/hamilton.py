from click import style

from .ggen import Generator


def hamilton(graph: list) -> list:
    start = 0
    counter = 0
    path = [start]
    visited = [False for i in range(len(graph))]
    visited[start] = True
    cycle(graph, start, start, visited, path, counter)
    return path[::-1]


def cycle(graph: list, current: int, start: int, visited: list, path: list, counter: int) -> bool:
    """
    This recursive function performs DF-searches of the solution tree
    for first possible hamiltonian cycle [-> True].

    If no cycle is found in any of the candidates -> False.

    path: list  –current path; first cycle found when -> True; lase path checked when -> False
    """
    # print(style(f" → {current}", fg="blue"), end="")
    visited[current] = True
    counter += 1
    for next in graph[current]:
        if next == start and counter == len(graph):
            path.append(current)
            return True
        if not visited[next]:
            if cycle(graph, next, start, visited, path, counter):
                path.append(current)
                # if len(path) == len(graph):
                # print(" → ".join(str(p) for p in path[::-1]))
                return True
    visited[current] = False
    counter -= 1
    # print(style(" ←", fg="red"), end="")
    return False


if __name__ == '__main__':
    graph = Generator(20, 0.3).print_list().list
    hamilton(graph)
