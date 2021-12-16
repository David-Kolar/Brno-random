import random

from copy import deepcopy
from file import input_file
from algoritms import make_graph
from random import randint
from file import output
from test import summation

def was_visited(node, visited):
    try:
        visited[node]
    except:
        visited[node] = False
    finally:
        return visited[node]

def neighbours_in_path(key, path):
    neighbours = []
    try:
        neighbours.append(path[-(len(path)-key) - 1])
    except: pass
    try:
        neighbours.append(path[key + 1])
    except: pass
    return neighbours

def check_neighbours(node, ls, visited, ancestor):
    if (was_visited(node, visited)):
        return False
    for neighbour in ls:
        if (was_visited(neighbour, visited) and not(ancestor)):
            return False
    return True

def mark_as_visited(path):
    visited = {}
    for key in path:
        visited[key] = True
    return visited

def random_node(graph):
    keys = list(graph.keys())
    if (keys):
        n = random.randint(0, len(keys) - 1)
        return keys[n]
    return False

def random_node_list(keys):
    if (keys):
        n = random.randint(0, len(keys) - 1)
        return n, keys[n]
    return False, False

def random_node_list(keys):
    if (keys):
        limit = 100
        if (len(keys) > 2*limit + 1):
            if (random.randint(0, 1)%2==0):
                n = random.randint(0, limit - 1)
            else: n =  random.randint(len(keys) - limit, len(keys)-1)
        else:
            n = random.randint(0, len(keys) - 1)
        return n, keys[n]
    return False, False

def random_path(node, graph, visited):
    cont = True
    ancestor = node
    path = []
    length = 0
    visited[node] = True
    while(cont):
        neighbours = deepcopy(graph[node])
        del neighbours[node]
        neighbours = list(neighbours.keys())
        new = []
        for key, neighbour in enumerate(neighbours):
            if (check_neighbours(neighbour, graph[neighbour].keys(), visited, ancestor)):
                new.append(neighbour)
        if not(new):
            cont = False
        length += graph[node][ancestor]
        path.append(node)
        visited[node] = True
        ancestor = node
        key, node = random_node_list(new)
    return length, path

graph, n = input_file()
graph = make_graph(graph)
visited = {}
node = random_node(graph)
l, old_path = random_path(node, graph, visited)
for i in range(10000):
    path = deepcopy(old_path)
    key, node = random_node_list(path)
    start = path[:key + 1]
    end = path[key::]
    if (len(start) >= len(end)):
        path = start
    else:
        path = end
    path = start
    to_end = (len(start) >= len(end))
    to_end = False
    visited = mark_as_visited(path)
    length, new_path = random_path(node, graph, visited)
    if (len(new_path) + len(path) > len(old_path)):
        if (to_end):
            path = path[0:-1] + new_path
        else:
            path = new_path[len(new_path)-1:1:-1] + path

        old_path = path
print(summation(old_path, graph))
"""
print(key)

key, node = random_node_list(path)
print(key, node)
black_list = neighbours_in_path(key, path).append(node)
print(black_list)
l2, path2 = build_path(node, graph, visited)
"""
