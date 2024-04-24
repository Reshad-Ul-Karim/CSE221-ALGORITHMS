input_file = open('input1_3.txt', 'r')
output_file = open('output1B_3.txt', 'w')
n, m = map(int, input_file.readline().split())
edges = [list(map(int, line.split())) for line in input_file.readlines()]


def kahn_topological_sort(n, m, edges):
    indegree = [0] * (n + 1)
    adjacency_list = [[] for i in range(n + 1)]

    for a, b in edges:
        adjacency_list[a].append(b)
        indegree[b] += 1

    queue = [i for i in range(1, n + 1) if indegree[i] == 0]
    top_order = []
    count = 0

    while queue:
        node = queue.pop(0)
        top_order.append(node)
        for neighbor in adjacency_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

        count += 1
    if count != n:
        return "IMPOSSIBLE"
    return top_order


result = kahn_topological_sort(n, m, edges)

if result == "IMPOSSIBLE":
    output_file.write(result)
else:
    output_file.write(' '.join(map(str, result)))

print(result)


input_file.close()
output_file.close()