def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


def Kruskal(n, roads):
    roads.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    mst_cost = 0
    edges_used = 0

    for u, v, w in roads:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += w
            edges_used += 1
            if edges_used == n - 1:
                break

    return mst_cost



input_file = open('input2_2.txt', 'r')
output_file = open("output2_2.txt", 'r')

data = input_file.read().split()

n = int(data[0])
m = int(data[1])

roads = []

index = 2
for i in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    roads.append((u, v, w))
    index += 3

min_cost = Kruskal(n, roads)
output_file.write(str(min_cost) + "\n")
