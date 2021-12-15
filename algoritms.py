from pqdict import minpq


def dijkstra(graph, source, target=None):
    """source: https://gist.github.com/nvictus/7854213"""
    dist = {}  # lengths of the shortest paths to each node
    pred = {}  # predecessor node in each shortest path

    # Store distance scores in a priority queue dictionary
    pq = minpq()
    for node in graph:
        if node == source:
            pq[node] = 0
        else:
            pq[node] = float('inf')

    # popitems always pops out the node with min score
    # Removing a node from pqdict is O(log n).
    for node, min_dist in pq.popitems():
        dist[node] = min_dist
        if node == target:
            break

        for neighbor in graph[node]:
            if neighbor in pq:
                new_score = dist[node] + graph[node][neighbor]
                if new_score < pq[neighbor]:
                    # Updating the score of a node is O(log n) using pqdict.
                    pq[neighbor] = new_score
                    pred[neighbor] = node

    return dist, pred


def bellman_ford(graph, source):
    """https://gist.github.com/ngenator/6178728"""
    # Step 1: Prepare the distance and predecessor for each node
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."

    return distance, predecessor


def shortest_path(graph, source, target):
    dist, pred = dijkstra(graph, source, target)
    end = target
    path = [end]
    while end != source:
        end = pred[end]
        path.append(end)
    path.reverse()
    return dist, path


def negation_graph(graph):
    new_graph = {}
    for key, val in graph.items():
        new_graph[key] = {}
        for key2 in val.keys():
            new_graph[key].update({key2 : -val[key2]})
    return new_graph

def make_graph(paths=(), n=0):
    graph = dict()
    for a, b, distance in paths:
        try:
            graph[a]
        except:
            graph[a] = {a: 0}
        try:
            graph[b]
        except:
            graph[b] = {b: 0}
        graph[a].update({b: distance})
        graph[b].update({a: distance})
    return graph
