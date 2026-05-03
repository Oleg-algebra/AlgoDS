from collections import deque



class Node:
    def __init__(self,key):
        self.key = key
        self.dist = -1
        self.neighbours = {}

    def add_neighbour(self, node: 'Node'):
        if node.key in self.neighbours:
            return
        self.neighbours[node.key] = node


    def get_neighbours(self) -> list['Node']:
        return self.neighbours.values()

class Graph:

    def __init__(self,vertices: dict):
        self.vertices = vertices

    def shortest_dist(self,start,finish):

        queue = deque()
        self.vertices[start].dist = 0
        queue.append(self.vertices[start])
        while queue:
            curr_vertex: Node = queue.popleft()
            if curr_vertex.key == finish:
                return curr_vertex.dist

            for neighbour in curr_vertex.get_neighbours():
                if neighbour.dist == -1:
                    neighbour.dist = curr_vertex.dist + 1
                    queue.append(neighbour)
        return 0


def build_graph(matrix) -> Graph:

    verticesList = {i : Node(i) for i in range(1,len(matrix) + 1)}

    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            if matrix[i][j] == 1:
                verticesList[i + 1].add_neighbour(verticesList[j + 1])
                verticesList[j + 1].add_neighbour(verticesList[i + 1])

    return Graph(verticesList)

if __name__ == "__main__":
    with open("input.txt") as f:
        n, start, finish = map(int,f.readline().split())
        matrix = []
        for _ in range(n):
            row = list(map(int,f.readline().split()))
            matrix.append(row)
        graph = build_graph(matrix)
        print(graph.shortest_dist(start, finish))
