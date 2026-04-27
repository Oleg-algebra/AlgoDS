class Graph:

    def __init__(self, adjencyMatrix):
        self.adjency = adjencyMatrix


    def edges_by_first(self):
        edges = []
        dim = len(self.adjency)
        for row in range(dim):
            for col in range(dim):
                if self.adjency[row][col] == 1:
                    edges.append((row + 1, col + 1))

        return edges

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
        graph = Graph(matrix)
        edges = graph.edges_by_first()
        for edge in edges:
            print(*edge)