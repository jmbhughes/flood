import copy
from collections import deque
from typing import Tuple
from flood.grid import FloodGrid
import numpy as np


class Tree(object):
    def __init__(self):
        self.children = dict()
        self.data = None
        self.name = ""

    def get(self, path):
        if path:
            return self.children[path[0]].get(path[1:])
        else:
            return self


def search(f: FloodGrid) -> Tuple[int, str]:
    root = Tree()
    root.data = copy.deepcopy(f)

    current = root
    q = deque()
    q.append(current)
    i = 0
    while q:
        i += 1
        current = q.pop()
        for color in range(1, f.n_colors + 1):
            current.children[str(color)] = Tree()
            current.children[str(color)].name = current.name + str(color)
            current.children[str(color)].data = copy.deepcopy(current.data)
            current.children[str(color)].data.fill(color)
            if current.children[str(color)].data.won():
                return i, current.children[str(color)].name
            else:
                q.appendleft(current.children[str(color)])


def analyze():
    sizes = list(range(3, 16))
    mean_length = []
    std_length = []
    min_length = []
    max_length = []
    for size in sizes:
        soln_lengths = []
        shape = (size, size)
        num_colors = 3
        for i in range(500):
            f = FloodGrid(shape, num_colors)
            nodes, soln = search(f)
            soln_lengths.append(len(soln))
        mean_length.append(np.mean(soln_lengths))
        std_length.append(np.std(soln_lengths))
        min_length.append(np.min(soln_lengths))
        max_length.append(np.max(soln_lengths))
