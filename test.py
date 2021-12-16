def summation(path, graph):
    length = 0
    ancestor = path[0]
    for node in path:
        length += graph[ancestor][node]
        ancestor = node
        print(length)
    return length