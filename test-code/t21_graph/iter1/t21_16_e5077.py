class Graph:

    def __init__(self, n):
        self.edges = {
            v: [] for v in range(1, n + 1)
        }
        self.adjency = self.getAdjencyMatrix()

    def addEdge(self, from_vertex, to_vertex):
        self.edges[from_vertex].append(to_vertex)

    def getAdjencyMatrix(self):
        matrix = [[0] * len(self.edges) for _ in range(len(self.edges))]

        for v in self.edges.keys():
            for neighbour in self.edges[v]:
                i = v - 1
                j = neighbour - 1
                matrix[i][j] = 1
        return matrix

    def update_adjency(self):
        self.adjency = self.getAdjencyMatrix()

    def is_semiComplete(self) -> bool:

        n = len(self.adjency)
        for i in range(n):
            for j in range(i+1,n):
                if self.adjency[i][j] == 0 and self.adjency[j][i] == 0:
                    return False


        return True


if __name__ == "__main__":
    with open("input.txt") as f:
        n, k = map(int, f.readline().split())
        graph = Graph(n)
        for i in range(k):
            edge = list(map(int, f.readline().split()))
            graph.addEdge(*edge)

        graph.update_adjency()
        if graph.is_semiComplete():
            print("YES")
        else:
            print("NO")