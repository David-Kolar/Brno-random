import random

from copy import deepcopy
from file import input_file
from algoritms import make_graph
from random import randint
from file import output
from test import summation, check_neighbours, check_path, all_visited, was_visited



def neighbours_in_path(key, path):
    neighbours = []
    try:
        neighbours.append(path[-(len(path)-key) - 1])
    except: pass
    try:
        neighbours.append(path[key + 1])
    except: pass
    return neighbours

def mark_as_visited(path, graph):
    visited = {}
    for key, val in enumerate(path):
        set_neighbours_as_visited(val, graph, visited)
    return visited

def set_neighbours_as_visited(node, graph, visited):
    for key in graph[node].keys():
        visited[key] = True

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
        limit = 50
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
    while(cont):
        neighbours = deepcopy(graph[node])
        del neighbours[node]
        neighbours = list(neighbours.keys())
        new = []
        for neighbour in neighbours:
            if not(was_visited(neighbour, visited)):
                new.append(neighbour)
        if not(new):
            cont = False
        length += graph[node][ancestor]
        path.append(node)
        set_neighbours_as_visited(node, graph, visited)
        ancestor = node
        key, node = random_node_list(new)
    return length, path

def find_random_long_path_len():
    graph, n = input_file()
    graph = make_graph(graph)
    visited = {}
    node = random_node(graph)
    l, old_path = random_path(node, graph, visited)
    for i in range(6000):
        path = deepcopy(old_path)
        key, node = random_node_list(path)
        start = path[:key+1]
        end = path[key::]
        if (len(start) >= len(end)):
            path = start
            visited = mark_as_visited(start[:-1], graph)
        else:
            path = end
            visited = mark_as_visited(end[1:], graph)
        to_end = (len(start) >= len(end))
        length, new_path = random_path(node, graph, visited)
        if (len(new_path) + len(path) - 2 > len(old_path)):
            if (to_end):
                path = path[0:-1] + new_path
            else:
                path = new_path[len(new_path)-1:0:-1] + path
            old_path = path
    s = summation(old_path, graph)
    return s, old_path

def find_random_long_path():
    graph, n = input_file()
    graph = make_graph(graph)
    visited = {}
    node = random_node(graph)
    l, old_path = random_path(node, graph, visited)
    for i in range(3000):
        path = deepcopy(old_path)
        key, node = random_node_list(path)
        start = path[:key+1]
        end = path[key::]
        if (summation(start, graph) >= summation(end, graph)):
            path = start
            visited = mark_as_visited(start[:-1], graph)
        else:
            path = end
            visited = mark_as_visited(end[1:], graph)
        to_end = (summation(start, graph) >= summation(end, graph))
        length, new_path = random_path(node, graph, visited)
        if (summation(new_path, graph) + summation(path, graph) - 2 > summation(old_path, graph)):
            if (to_end):
                path = path[0:-1] + new_path
            else:
                path = new_path[len(new_path)-1:0:-1] + path
            old_path = path
    s = summation(old_path, graph)
    return s, old_path

def record():
    record = 0
    record_path = []
    for i in range(100):
        s, path = find_random_long_path()
        if (s > record):
            record = s
            record_path = path
            print(record)
            output(record, record_path)
        print(i)
"""
print(key)

key, node = random_node_list(path)
print(key, node)
black_list = neighbours_in_path(key, path).append(node)
print(black_list)
l2, path2 = build_path(node, graph, visited)
"""
