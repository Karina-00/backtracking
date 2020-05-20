from sys import stderr
from time import time

from .ggen import Generator
from .hamilton import hamilton

for i in [10, 20, 30, 40, 50, 55, 60, 65, 70, 75]:
    print(i, end=" ", file=stderr)
    graph = Generator(i, 0.3).list

    time = 0
    for i in range(3):
        start = time()
        hamilton(graph)
        stop = time()
        time.append(stop - start)

    print(time / 3, end=" ", file=stderr)

    print(file=stderr)
