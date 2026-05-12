def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[x] = y

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    parent = list(range(n))

    print("MST Edges:")

    for u, v, w in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            print(u, "-", v, "=", w)
            union(parent, x, y)


# -------- USER INPUT --------
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
for i in range(e):
    u = int(input("Enter u: "))
    v = int(input("Enter v: "))
    w = int(input("Enter weight: "))
    edges.append((u, v, w))

kruskal(edges, n)
