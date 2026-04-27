class Graph:

    def __init__(self, adjencyMatrix):
        self.adjency = adjencyMatrix


    def countDegrees(self)-> list[int]:

        result = []
        for i in range(len(self.adjency)):
            result.append(
                sum(self.adjency[i])
            )

        return result

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = []
        for _ in range(n):
            matrix.append(
                list(map(int,f.readline().split()))
            )
        graph = Graph(matrix)
        print(*graph.countDegrees())