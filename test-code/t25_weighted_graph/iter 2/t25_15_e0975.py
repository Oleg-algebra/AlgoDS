
from math import inf

def floyd(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(lambda x: int(x) if x != '-1' else inf,
                     f.readline().split()))
            for _ in range(n)
        ]


        floyd(matrix,n)
        # print(matrix)

        max_dist = 0
        for i in range(n):
            for j in range(n):
                if i != j and matrix[i][j] != inf and matrix[i][j]>max_dist:
                    max_dist = matrix[i][j]

        print(max_dist)