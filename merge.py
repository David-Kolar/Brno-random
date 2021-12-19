from test import summation, check_path

def path_to_dict(path=[]):
    new = {}
    for key, node in enumerate(path):
        new[node] = key
    return new

def check_if_in_path(node, path):
    try:
        path[node]
        return True
    except:
        return False

def count_direction(p1, p2):
    return (p1 - p2 <= -1)

def find_intersections(path1, path2):
    intersections = []
    direction_negative = None
    first = True
    for key, val in path2.items():
        if (check_if_in_path(key, path1)):
            intersections.append(key)
            if (first):
                first = False
            else:
                if not(count_direction(path1[intersections[-2]], path1[intersections[-1]])):
                    return intersections[:-1]
    return intersections

def merge_two_paths(path1, path2, graph):
    path1_dict = path_to_dict(path1)
    path2_dict = path_to_dict(path2)
    intersections = find_intersections(path1_dict, path2_dict)
    key1 = 0
    key2 = 0
    new_path = []
    for n, node in enumerate(intersections):
        new_key1 = path1_dict[node]
        new_key2 = path2_dict[node]
        part1 = path1[key1:new_key1]
        part2 = path2[key2:new_key2]
        if (summation(part1, graph) >= summation(part2, graph)):
            new_path += part1
        else:
            new_path += part2
        key1 = new_key1
        key2 = new_key2
        if (n == len(intersections) - 1):
            new_path += path1[key1:]
    if not(intersections) or (check_path(new_path, graph) != True):
        return path1
    return new_path