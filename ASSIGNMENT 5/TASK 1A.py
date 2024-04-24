input_file = open('input1_1.txt', 'r')
n, m = map(int, input_file.readline().split())
edges = [list(map(int, line.split())) for line in input_file.readlines()]
output_file = open('output1A_1.txt', 'w')

def dfs(node, adjac_list, vis, stack, rec_stack):
    vis[node] = True
    rec_stack[node] = True

    for neighbor in adjac_list[node]:
        if not vis[neighbor]:
            if dfs(neighbor, adjac_list, vis, stack, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    stack.insert(0, node)
    return False

def topological_sort(n, m, edges):
    adjacency_list = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    recursion_stack = [False] * (n + 1)
    stack = []

    for a, b in edges:
        adjacency_list[a].append(b)

    for node in range(1, n + 1):
        if not visited[node]:
            if dfs(node, adjacency_list, visited, stack, recursion_stack):
                return "IMPOSSIBLE"

    return stack

result = topological_sort(n, m, edges)

if result == "IMPOSSIBLE":
    output_file.write(result)
else:
    output_file.write(' '.join(map(str, result)))

print(result)