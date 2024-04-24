import heapq

input_file = open('input2_1.txt', 'r')
output_file = open('output2_1.txt', 'w')
n, m = map(int, input_file.readline().split())
edges = [list(map(int, line.split())) for line in input_file.readlines()]

def lexicographical_topological_sort(n, m, edges):
    indegree = [0] * (n + 1)
    adjacency_list = [[] for _ in range(n + 1)]
    for a, b in edges:
        adjacency_list[a].append(b)
        indegree[b] += 1

    priority_queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            priority_queue.append(i)
    heapq.heapify(priority_queue)
    top_order = []

    while priority_queue:
        node = heapq.heappop(priority_queue)
        top_order.append(node)

        for neighbor in adjacency_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(priority_queue, neighbor)

    if len(top_order) != n:
        return "IMPOSSIBLE"
    return top_order


result = lexicographical_topological_sort(n, m, edges)
if result == "IMPOSSIBLE":
    output_file.write(result)
else:
    output_file.write(' '.join(map(str, result)))
print(result)

input_file.close()
output_file.close()