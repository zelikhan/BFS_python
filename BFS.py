mygraph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'D': [],
    'C': ['E', 'F'],
    'E': [],
    'F': []
}

visited = []
queue = []


def mybfs(mygraph, visited, starting_node):
    visited.append(starting_node)
    queue.append(starting_node)
    while queue:
        a = queue.pop(0)
        print(a, end=" ")
        for neighbour in mygraph[a]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Bredth First Search Traversal : ")
mybfs(mygraph, visited, "A")
