import math
import sys
from typing import Callable
import doctest
INF = math.inf
graph1 = [[0, 0, 1, 0, 0, 11],
          [20, 0, 11, 0, 7, 0],
          [2, 5, 0, 15, 32, 0],
          [0, 14, 0, 3, 8, 2],
          [0, 2, 9, 17, 0, 0],
          [0, 6, 8, 0, 1, 0]]

graph2 = {0: [(0, 0), (1, INF), (2, 7), (3, 5)],
          1: [(0, 4), (1, 0), (2, INF), (3, 40)],
          2: [(0, 25), (1, 12), (2, 0), (3, INF)],
          3: [(0, INF), (1, 3), (2, 7), (3, 0)]}

class Outputtype:
    def length_dict(self):  # find all distance of path from specific vertex to all the others
        d = dict()
        l = len(self)
        for element in range(l):
            d[element] = self[element]
        return d

    def max(self):  # max length of shortest paths
        max_len = 0
        for element in self:
            if max_len < element:
                max_len = element
        return max_len

def path_algo(algorithm: Callable, items: list, src, outputtype=Outputtype):
    '''
    >>> path_algo(algorithm=dijkstra, items=graph1, src=1, outputtype=Outputtype.length_dict)
    {0: 13, 1: 0, 2: 11, 3: 24, 4: 7, 5: 24}
    >>> path_algo(algorithm=floyd, items=graph1, src=1, outputtype=Outputtype.length_dict)
    {0: 13, 1: 0, 2: 11, 3: 24, 4: 7, 5: 24}
    >>> path_algo(algorithm=dijkstra, items=graph1, src=1, outputtype=Outputtype.max)
    24
    >>> path_algo(algorithm=floyd, items=graph1, src=1, outputtype=Outputtype.max)
    24
    >>> path_algo(algorithm=dijkstra, items=graph2, src=2, outputtype=Outputtype.length_dict)
    {0: 16, 1: 12, 2: 0, 3: 21}
    >>> path_algo(algorithm=floyd, items=graph2, src=2, outputtype=Outputtype.length_dict)
    {0: 16, 1: 12, 2: 0, 3: 21}
    >>> path_algo(algorithm=dijkstra, items=graph2, src=2, outputtype=Outputtype.max)
    21
    >>> path_algo(algorithm=floyd, items=graph2, src=2, outputtype=Outputtype.max)
    21
    '''
    if isinstance(items, list):
        return outputtype(algorithm(items, src))
    if isinstance(items, dict):
        r, c = len(items.keys()), len(items.keys())
        i, j = 0, 0
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        while i != r:
            for adj in items.values():
                for val in adj:
                    matrix[i][j] = val[1]
                    j += 1
                i += 1
                j = 0
    return outputtype(algorithm(matrix, src))


# floyd taken from https://favtutor.com/blogs/floyd-warshall-algorithm
def floyd(g, src):
    g = floyd_helper(g)
    nV = len(g[0])
    dist = list(map(lambda p: list(map(lambda q: q, p)), g))

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    return dist[src]

def floyd_helper(g):
    V = len(g[0])
    for p in range(V):
        for q in range(V):
            if p != q and g[p][q] == 0:
                g[p][q] = INF
    return g
# minDistance & dijkstra taken from https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
def minDistance(dist, sptSet, V):
    # Initialize minimum distance for next node
    min = 1e7
    # Search not nearest vertex not in the
    # shortest path tree
    min_index = 0
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v
    return min_index


def dijkstra(g, src):
    V = len(g[0])
    dist = [sys.maxsize] * V
    dist[src] = 0
    sptSet = [False] * V
    for cout in range(V):
        # Pick the minimum distance vertex from
        # the set of vertices not yet processed.
        # x is always equal to src in first iteration
        x = minDistance(dist, sptSet, V)
        # Put the minimum distance vertex in the
        # shortest path tree
        sptSet[x] = True
        # Update dist value of the adjacent vertices
        # of the picked vertex only if the current
        # distance is greater than new distance and
        # the vertex in not in the shortest path tree
        for y in range(V):
            if g[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + g[x][y]:
                dist[y] = dist[x] + g[x][y]
    return dist






if __name__ == "__main__":
    print(doctest.testmod())
