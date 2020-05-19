from click import style

from .ggen import gen_list


def hamilton(graph):
    start = 0
    counter = 0
    path = [start]
    visited = [False for i in range(len(graph))]
    # print(visited)
    visited[start] = True
    cycle(graph, start, start, visited, path, counter)


def cycle(graph, current, start, visited, path, counter):
    print(style(f" → {current}", fg="blue"), end="")
    visited[current] = True
    counter += 1
    # secho(f"visited: {visited}", fg="blue")
    for next in graph[current]:
        if next == start and counter == len(graph):
            return True
        if not visited[next]:
            if cycle(graph, next, start, visited, path, counter):
                path.append(current)
                print(path[::-1])
                return True
    visited[current] = False
    counter -= 1
    print(style(" ←", fg="red"), end="")
    return False


if __name__ == '__main__':
    graph = {
        0: [1],
        1: [2, 4],
        2: [0, 3],
        3: [5],
        4: [2, 3],
        5: [0],
    }
    hamilton(gen_list(15, 0.3))
