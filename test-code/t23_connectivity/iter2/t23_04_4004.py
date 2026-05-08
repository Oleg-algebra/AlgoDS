
WHITE = 0   # не відвідували
GREY = 1    # в процесі обробки
BLACK = 2   # завершено обробку


class Graph:
    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)

    def dfs(self, i, vertices):
        vertices[i] = GREY
        for j in range(self.n):
            if self.matrix[i][j] == 1:
                # Якщо вершина біла, йдемо в рекурсію
                if vertices[j] == WHITE:
                    if self.dfs(j, vertices):
                        return True
                # Якщо зустріли сіру — це зворотне ребро (цикл)
                elif vertices[j] == GREY:
                    return True

        vertices[i] = BLACK
        return False

    def has_cycle(self):
        vertices = [WHITE for _ in range(self.n)]
        for i in range(self.n):
            if vertices[i] == WHITE:
                if self.dfs(i, vertices):
                    return True
        return False


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = [int(a) for a in f.readline().split()]
            matrix.append(row)

        graph = Graph(matrix)
        print(int(graph.has_cycle()))