WHITE = 0
GREY = 1
BLACK = 2

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def has_cycle(self):
        visited = []
        colors = [WHITE for _ in range(self.n)]
        for i in range(self.n):
            if colors[i] == WHITE:
                if self.dfs_helper(i,visited,colors)[0]:
                    return True, []


        return False, visited[::-1]


    def dfs_helper(self,current,visited,colors):

        # print(f"-->{current + 1}")
        colors[current] = GREY

        for j in range(self.n):
            if self.matrix[current][j] == 1:
                if colors[j] == WHITE:
                    if self.dfs_helper(j,visited,colors)[0]:
                        return True, []
                elif colors[j] == GREY:
                    return True, []

        # print(f"<--{current + 1} (exit) ")
        colors[current] = BLACK
        visited.append(current + 1)
        return False, visited


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int, f.readline().split())) for _ in range(n)
        ]

        graph = Graph(matrix)
        res, sorted_graph = graph.has_cycle()
        if res:
            print(1)
        else:
            print(0)
