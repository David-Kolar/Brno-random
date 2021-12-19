def input_file(name="input"):
    with open(name) as file:
        n_crosses = None
        n_streets = None
        graph = []
        for key, line in enumerate(file):
            if (key == 0):
                n_crosses, n_streets = [int(i) for i in line.split()]
            if (key > n_crosses):
                l = line.split()
                l[2] = int(l[2])
                graph.append(l)
        return graph, n_streets

def load_path():
    with open("output.txt") as file:
        first = True
        path = []
        for line in file:
            if (first): first = False
            else: path.append(line[0:-1])
    return path
def input_with_cordinates(name="input"):
    with open(name) as file:
        n_crosses = None
        n_streets = None
        graph = []
        cordinates = {}
        for key, line in enumerate(file):
            l = line.split()
            if (key == 0):
                n_crosses, n_streets = [int(i) for i in line.split()]
            elif (key > n_crosses):
                l[2] = int(l[2])
                graph.append(l)
            else:
                cordinates[l[0]] = {"x": float(l[1]), "y" : float(l[2])}
        return graph, n_streets, cordinates

def output(longest, path, file="output.txt"):
    longest = str(longest)
    with open(file, "w") as file:
        file.write(longest + "\n")
        for line in path:
            file.write(line + "\n")