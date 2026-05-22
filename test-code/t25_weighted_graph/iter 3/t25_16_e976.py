from math import inf

changes_matrix: list

def floyd(graph, n):

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    global changes_matrix
    changes_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                changes_matrix[i][j] += 1

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        graph = [
            list(map(lambda x: int(x) if x != "0" else inf,
                     f.readline().split()))
            for _ in range(n)
        ]

        # print(graph)
        floyd(graph,n)

        # for row in graph:
        #     print(*row)

        # print("=======")
        # for row in changes_matrix:
        #     print(*row)

        for i in range(n):
            for j in range(n):
                if graph[i][j] != inf:
                    if changes_matrix[i][j] == 0:
                        changes_matrix[i][j] = 1
                    elif changes_matrix[i][j] > 0:
                        changes_matrix[i][j] = 2

        # print("=======")
        for row in changes_matrix:
            print(*row)