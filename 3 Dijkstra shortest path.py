def dijkstra(graph, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        min_dist = float('inf')
        u = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    print("Shortest distances:", dist)


# -------- USER INPUT --------
n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter source vertex: "))

dijkstra(graph, n, start)
