input_file = open('input3_3.txt', 'r')
output_file = open('output3_3.txt', 'w')

n, m = map(int, input_file.readline().strip().split())
edges = [list(map(int, line.strip().split())) for line in input_file]


def dfs(graph, vertex, visited, stack):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(vertex)


def reverse_graph(graph):
    reversed_graph = []
    for i in range(len(graph)):
        reversed_graph.append([])
    for vertex, neighbors in enumerate(graph):
        for neighbor in neighbors:
            reversed_graph[neighbor].append(vertex)
    return reversed_graph


def dfs_for_scc(reversed_graph, v, vis, current_scc):
    vis[v] = True
    current_scc.append(v)
    for neighbor in reversed_graph[v]:
        if not vis[neighbor]:
            dfs_for_scc(reversed_graph, neighbor, vis, current_scc)


def kosaraju(n, edges):
    graph = []
    for i in range(n):
        graph.append([])
    for u, v in edges:
        graph[u - 1].append(v - 1)

    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    reversed_graph = reverse_graph(graph)

    visited = [False] * n
    sccs = []
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            current_scc = []
            dfs_for_scc(reversed_graph, vertex, visited, current_scc)
            sccs.append(sorted([x + 1 for x in current_scc]))

    return sccs


sccs = kosaraju(n, edges)
for scc in sccs:
    output_file.write(" ".join(map(str, scc)) + "\n")
    print(" ".join(map(str, scc)))
