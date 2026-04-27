
def edges_to_matrix(dim: int, adjList: dict) -> list[list[int]]:
    # print(adjList)
    matrix = [[0] * dim for _ in range(dim)]
    for row in adjList.keys():
        for neigh in adjList[row]:
            # print(matrix[row])
            matrix[row][neigh - 1] = 1
            # print(matrix)


    return matrix

if __name__ == "__main__":
    with open("input.txt") as f:
        dim  = int(f.readline().strip())
        adjList = {}
        for i in range(dim):
            data = list(map(int,f.readline().split()))
            N = data[0]
            if N > 0:
                adjList[i] = data[1:]

        matrix = edges_to_matrix(dim, adjList)
        for row in matrix:
            print(*row)


