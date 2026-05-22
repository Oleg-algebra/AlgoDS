from math import inf


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
            list(map(lambda x: int(x) if x != "-1" else inf,
                     f.readline().split()))
            for _ in range(n)
        ]

        # print(graph)
        floyd(graph,n)

        max_dist = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] != inf and graph[i][j] > max_dist:
                    max_dist = graph[i][j]


        print(max_dist)