from collections import deque


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_edge(self,v1,v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def next_vertices(self, current):

        next_vert = []
        if int(current[0]) < 9:
            next_vert.append(
                str(int(current[0]) + 1) + current[1:]
            )

        if int(current[-1]) > 1:
            next_vert.append(
                current[:-1] + str(int(current[-1]) - 1)
            )
        next_vert.append(current[-1] + current[:-1])
        next_vert.append(current[1:] + current[0])

        return next_vert

    def shortest_path(self, start, finish):

        source = {start : None}

        queue = deque()
        queue.append(start)

        while queue:

            curr = queue.popleft()

            if curr == finish:
                break

            next_vert = self.next_vertices(curr)
            for neigh in next_vert:
                if neigh not in source:
                    source[neigh] = curr
                    queue.append(neigh)


        path = [finish]
        curr = finish

        while source[curr] is not None:
            path.append(source[curr])
            curr = source[curr]


        return path[::-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        start = f.readline().strip()
        finish = f.readline().strip()

        graph = Graph()


        path = graph.shortest_path(start, finish)
        for step in path:
            print(step)