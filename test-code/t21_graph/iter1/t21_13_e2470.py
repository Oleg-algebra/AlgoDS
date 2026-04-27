class Graph:

    def __init__(self, adjencyMatrix):
        self.adjency = adjencyMatrix


    def is_oriented(self) -> bool:
        n = len(self.adjency)
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    if self.adjency[i][i] != 0:
                        return False
                else:
                    if self.adjency[i][j] != self.adjency[j][i]:
                        return False

        return True


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)
        graph = Graph(matrix)
        if graph.is_oriented():
            print("YES")
        else:
            print("NO")