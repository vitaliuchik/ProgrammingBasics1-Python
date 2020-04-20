# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    f = open(file_name, encoding='utf-8')
    edges = []
    for row in f.readlines():
        edge = row[:-1].split(',')
        edges.append([int(edge[0]), int(edge[1])])
    return edges

def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    edge_dict = dict()
    for edge in edge_list:
        if edge[0] in edge_dict.keys():
            edge_dict[edge[0]].append(edge[1])
        else:
            edge_dict[edge[0]] = [edge[1]]
        if edge[1] in edge_dict.keys():
            edge_dict[edge[1]].append(edge[0])
        else:
            edge_dict[edge[1]] = [edge[0]]
    for i in range(len(list(edge_dict.values()))):
        list(edge_dict.values())[i].sort()
    return edge_dict


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> dict

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph.keys() and edge[1] in graph[edge[0]]:
        return True
    return False

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] not in graph.keys():
        graph[edge[0]] = [edge[1]]
    elif edge[1] not in graph[edge[0]]:
        graph[edge[0]].append(edge[1])
    if edge[1] not in graph.keys():
        graph[edge[1]] = [edge[0]]
    elif edge[0] not in graph[edge[1]]:
        graph[edge[1]].append(edge[0])

    return graph


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in graph.keys():
        if len(graph[edge[0]]) == 1:
            del graph[edge[0]]
        else:
            graph[edge[0]].remove(edge[1])
        if len(graph[edge[1]]) == 1:
            del graph[edge[1]]
        else:
            graph[edge[1]].remove(edge[0])
    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph.keys():
        graph[node] = []
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph.keys():
        del graph[node]
        for el in graph.keys():
            if node in graph[el]:
                graph[el].remove(node)
    return graph

def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    f = open('dot.txt', 'w', encoding = 'utf-8')
    f.write('graph {\n')
    for key in graph.keys():
        s = str(key) + ' -- '
        if len(graph[key]) == 1:
            s += (str(graph[key][0]) + ';\n')
        elif len(graph[key]) == 0:
            break
        else:
            s += '{ '
            for i in graph[key]:
                s += (str(i) + ' ')
            s += '};\n'
        f.write(s)
    f.write('}')
    f.close()



convert_to_dot({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})


import doctest
print(doctest.testmod())
