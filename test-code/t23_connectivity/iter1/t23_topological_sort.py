WHITE = 0
GRAY = 1
BLACK = 2

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def topological_sort(self):
        visited = []
        colors = [WHITE for _ in range(self.n)]
        for i in range(self.n):
            if colors[i] is WHITE:
                self.dfs_helper(i,visited,colors)

        print(visited[::-1])


    def dfs_helper(self,current,visited,colors):

        print(f"-->{current + 1}")
        colors[current] = BLACK

        for j in range(self.n):
            if self.matrix[current][j] == 1 and colors[j] is WHITE:
                self.dfs_helper(j,visited,colors)

        print(f"<--{current + 1} (exit) ")
        visited.append(current + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int, f.readline().split())) for _ in range(n)
        ]

        graph = Graph(matrix)
        graph.topological_sort()
