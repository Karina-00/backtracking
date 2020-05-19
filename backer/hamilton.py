from click import secho


def hamilton(graph):
    start = 0
    counter = 0
    path = [start]
    visited = [False for i in range(len(graph))]
    print(visited)
    visited[start] = True
    cycle(graph, start, start, visited, path, counter)


def cycle(graph, current, start, visited, path, counter):
    secho(f"at {current}", fg="blue")
    visited[current] = True
    counter += 1
    secho(f"visited: {visited}", fg="blue")
    for next in graph[current]:
        if next == start and counter == len(graph):
            return True
        if not visited[next]:
            if cycle(graph, next, start, visited, path, counter):
                path.append(current)
                print(path)
                return True
    visited[current] = False
    counter -= 1
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
    hamilton(graph)
