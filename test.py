def summation(path, graph):
    length = 0
    ancestor = path[0]
    for node in path:
        length += graph[ancestor][node]
        ancestor = node
    return length
def all_visited(visited):
    new = []
    for key, val in visited.items():
        if (val): new.append(key)
    return new

def set_neighbours_as_visited(node, graph, visited):
    for key in graph[node].keys():
        visited[key] = True

def was_visited(node, visited):
    try:
        visited[node]
    except:
        visited[node] = False
    finally:
        return visited[node]

def check_neighbours(node, ls, visited, ancestor):
    for neighbour in ls:
        if (was_visited(neighbour, visited) and not ancestor):
            return False
    return True

def check_path(path, graph):
    visited = {}
    for node in path:
        if (was_visited(node, visited)):
            return node
        set_neighbours_as_visited(node, graph, visited)
    return True