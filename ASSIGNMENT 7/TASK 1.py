input_file = open("input1_1.txt", 'r')
output_file = open("output1_1.txt", 'w')
n, k = map(int, input_file.readline().split())
parent = list(range(n + 1))
size = [1] * (n + 1)

def union(x, y, parent, size):
    rootX = find_parent(x, parent)
    rootY = find_parent(y, parent)

    if rootX != rootY:
        if size[rootX] < size[rootY]:
            parent[rootX] = rootY
            size[rootY] += size[rootX]
        else:
            parent[rootY] = rootX
            size[rootX] += size[rootY]


def find_parent(node, parent):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)
    return parent[node]


for i in range(k):
    a, b = map(int, input_file.readline().strip().split())
    union(a, b, parent, size)
    root = find_parent(a, parent)
    output_file.write(f"{size[root]}\n")
input_file.close()
output_file.close()
