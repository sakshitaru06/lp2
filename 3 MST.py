def prim_mst(graph, n):
    selected = [False] * n
    selected[0] = True

    print("Edges in MST:")
    
    for _ in range(n - 1):
        minimum = float('inf')
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True


# -------- USER INPUT --------
n = int(input("Enter number of vertices: "))

graph = []
print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph, n)
