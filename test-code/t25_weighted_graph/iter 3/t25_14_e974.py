
def floyd(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        graph = [
            list(map(int, f.readline().split()))
            for _ in range(n)
        ]

        # print(graph)
        floyd(graph,n)

        for row in graph:
            print(*row)