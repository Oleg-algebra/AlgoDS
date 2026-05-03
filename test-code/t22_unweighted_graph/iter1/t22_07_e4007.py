from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self,from_vert, to_vert):
        self.vertices[from_vert].add(to_vert)
        self.vertices[to_vert].add(from_vert)

    def get_next_vertices(self, current):
        next_vertices = []
        if int(current[0]) < 9:
            next_vertices.append(str(int(current[0]) + 1) + current[1:])

        if int(current[-1]) > 1:
            next_vertices.append(current[:-1] + str(int(current[-1]) - 1))

        next_vertices.append(current[-1] + current[:-1])
        next_vertices.append(current[1:] + current[0])

        return next_vertices


    def shodrtest_path(self,start,finish) -> list[int]:



        source = {start: None}

        queue = deque()
        queue.append(start)
        is_found = False
        while queue:

            curr = queue.popleft()
            if curr == finish:
                break
            next_vertices = self.get_next_vertices(curr)
            for vertex in next_vertices:
                # if vertex == finish:
                #     source[vertex] = curr
                #     is_found  = True
                #     break
                if vertex not in source:
                    source[vertex] = curr
                    queue.append(vertex)


            # if is_found:
            #     break



        path = [finish]

        curr = finish
        while source[curr] is not None:
            path.append(source[curr])
            curr = source[curr]


        return path[::-1]


if __name__ == "__main__":
    with (open("input.txt") as f):

        start = f.readline().strip()
        finish = f.readline().strip()
        graph = Graph()
        path = graph.shodrtest_path(start, finish)
        for step in path:
            print(step)

        # print(graph.get_next_vertices("1234"))