import random

from copy import deepcopy
from file import input_file
from algoritms import make_graph
from random import randint

def was_visited(node, visited):
    try:
        visited[node]
    except:
        visited[node] = False
    finally:
        return visited[node]

def check_neighbours(node, ls, visited):
    for neighbour in ls:
        if (was_visited(neighbour, visited)):
            return False
    return True

def random_node(graph):
    keys = list(graph.keys())
    if (keys):
        n = random.randint(0, len(keys) - 1)
        return keys[n]
    return False

def random_node_list(keys):
    if (keys):
        n = random.randint(0, len(keys) - 1)
        return keys[n]
    return False

def random_path(graph, visited):
    cont = True
    node = random_node(graph)
    ancestor = node
    path = []
    length = 0
    while(cont):
        neighbours = deepcopy(graph[node])
        del neighbours[node]
        neighbours = list(graph[node].keys())
        new = []
        for key, neighbour in enumerate(neighbours):
            if (check_neighbours(neighbour, graph[neighbour].keys(), visited)):
                new.append(neighbour)
        if not(new):
            cont = False
        length += graph[node][ancestor]
        path.append(node)
        visited[node] = True
        ancestor = node
        node = random_node_list(new)
    return length, path

graph, n = input_file()
graph = make_graph(graph)
record = 0
for i in range(1000):
    visited = {}
    l, path = random_path(graph, visited)
    if (record < l):
        record = l
print(record, path)
