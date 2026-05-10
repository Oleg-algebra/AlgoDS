
WHITE = 0
BLACK = 1
GREY = 2

class Graph:

    def __init__(self,matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def has_cycle(self):
        colors = [WHITE for _ in range(self.n)]
        for j in range(self.n):
            if colors[j] == WHITE:
                if self.dfs(j, colors):
                    return True

        return False

    def dfs(self, start, colors):

        # print(f"--> {start + 1}")
        colors[start] = GREY
        for j in range(self.n):
            if self.matrix[start][j] == 1:
                if colors[j] == WHITE:
                    if self.dfs(j, colors):
                        return True
                elif colors[j] == GREY:
                    return True


        # print(f"<-- {start + 1}(exit)")
        colors[start] = BLACK
        return False



if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int,f.readline().split())) for _ in range(n)
        ]

        graph = Graph(matrix)
        print(int(graph.has_cycle()))





