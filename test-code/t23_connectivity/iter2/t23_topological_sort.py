
WHITE = 0
BLACK = 1

class Graph:

    def __init__(self,matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def dfs(self):
        visited = []
        colors = [WHITE for _ in range(self.n)]
        for j in range(self.n):
            if colors[j] == WHITE:
                self.dfs_helper(j,visited,colors)

        return visited[::-1]

    def dfs_helper(self,start,visited,colors):

        print(f"--> {start + 1}")
        colors[start] = BLACK
        for j in range(self.n):
            if self.matrix[start][j] == 1 and colors[j] == WHITE:
                self.dfs_helper(j,visited,colors)

        print(f"<-- {start + 1}(exit)")
        visited.append(start + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int,f.readline().split())) for _ in range(n)
        ]

        graph = Graph(matrix)
        print(*graph.dfs())





