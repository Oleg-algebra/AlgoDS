from collections import deque


class Graph:
    def __init__(self, v_num):
        self.vertices = {i: set() for i in range(1,v_num + 1)}

    def add_edge(self,from_vert, to_vert):
        self.vertices[from_vert].add(to_vert)
        self.vertices[to_vert].add(from_vert)

    def shodrtest_path(self,start,finish) -> list[int]:

        source = {start: None}

        queue = deque()
        queue.append(start)
        is_found = False
        while queue:

            curr_vert = queue.popleft()
            if curr_vert == finish:
                break
            for neighbour in self.vertices[curr_vert]:
                # if neighbour == finish:
                #     source[neighbour] = curr_vert
                #     is_found = True
                #     break

                if neighbour not in source:
                    source[neighbour] = curr_vert
                    queue.append(neighbour)

            # if is_found:
            #     break
        else:
            return []

        path = [finish]

        curr = finish
        while source[curr] is not None:
            path.append(source[curr])
            curr = source[curr]


        return path[::-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        n,m = map(int,f.readline().split())
        start,finish = map(int,f.readline().split())
        graph = Graph(n)
        for _ in range(m):
            a,b = map(int,f.readline().split())
            graph.add_edge(a,b)
        path = graph.shodrtest_path(start, finish)
        print(len(path) - 1)
        print(*path)