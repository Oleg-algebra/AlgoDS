

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)


    def dfs_vertsx_count(self,start):

        visited = {start}
        stack = [start]

        while stack:

            curr = stack.pop()
            for j in range(self.n):
                if self.matrix[curr][j] == 1 and j not in visited:
                    visited.add(j)
                    stack.append(j)


        return len(visited)


if __name__ == "__main__":
    with open("input.txt") as f:
        n,start = map(int, f.readline().split())

        matrix = [
            list(map(int, f.readline().split())) for _ in range(n)
        ]


        graph= Graph(matrix)
        print(graph.dfs_vertsx_count(start-1))