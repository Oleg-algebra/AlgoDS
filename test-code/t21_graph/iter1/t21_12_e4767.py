
class Graph:

    def __init__(self,n):
        self.edges = {
            v: [] for v in range(1,n+1)
        }

    def addEdge(self,from_vertex, to_vertex):
        self.edges[from_vertex].append(to_vertex)

    def getAdjencyMatrix(self):
        matrix = [[0] * len(self.edges) for _ in range(len(self.edges))]

        for v in self.edges.keys():
            for neighbour in self.edges[v]:
                i = v - 1
                j = neighbour - 1
                matrix[i][j] = 1

        return matrix



if __name__ == "__main__":
    with open("input.txt") as f:
        n,k = map(int,f.readline().split())
        graph = Graph(n)
        for i in range(k):
            edge = list(map(int,f.readline().split()))
            graph.addEdge(*edge)

        matrix = graph.getAdjencyMatrix()
        for row in matrix:
            print(*row)



