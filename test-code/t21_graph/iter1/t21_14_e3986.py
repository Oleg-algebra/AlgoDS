class Graph:

    def __init__(self, adjencyMatrix):
        self.adjency = adjencyMatrix


    def leaks_and_drains(self) -> (list[int],list[int]):
        leaks = set(range(1,len(self.adjency)+1))
        drains = set(range(1,len(self.adjency)+1))

        n = len(self.adjency)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    drains.discard(i + 1)
                    leaks.discard(j + 1)
        leaks = list(leaks)
        drains = list(drains)
        leaks.sort()
        drains.sort()
        return leaks,drains



if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
        graph = Graph(matrix)
        leaks,drains = graph.leaks_and_drains()
        print(len(leaks),*leaks)
        print(len(drains),*drains)