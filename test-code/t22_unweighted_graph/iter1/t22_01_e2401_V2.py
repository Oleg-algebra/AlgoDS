from collections import deque



class Graph:

    def __init__(self,matrix):
        self.matrix = matrix

    def shortest_dist(self,start,finish):
        n = len(self.matrix)
        distances = [-1 for _ in range(n)]
        distances[start] = 0

        queue = deque()
        queue.append(start)
        while queue:
            curr_vertex = queue.popleft()
            if curr_vertex == finish:
                return distances[curr_vertex]

            for j in range(n):
                if self.matrix[curr_vertex][j] == 1 and distances[j] == -1:
                    distances[j] = distances[curr_vertex] + 1
                    queue.append(j)
        return 0



if __name__ == "__main__":
    with open("input.txt") as f:
        n, start, finish = map(int,f.readline().split())
        matrix = []
        for _ in range(n):
            row = list(map(int,f.readline().split()))
            matrix.append(row)
        graph = Graph(matrix)
        print(graph.shortest_dist(start - 1, finish - 1))
