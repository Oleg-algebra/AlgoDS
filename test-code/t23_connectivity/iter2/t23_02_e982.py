from random import shuffle


class Graph:

    def __init__(self,n):
        self.vertices = { i : set() for i in range(1,n+1)}


    def add_edge(self,v1,v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def is_connected(self):

        remaining = list(self.vertices)
        shuffle(remaining)

        stack = [remaining.pop()]

        while stack:
            print(f"remaining: {remaining}, stack: {stack}, current: {stack[-1]}")
            curr  = stack.pop()

            for neigh in self.vertices[curr]:
                if neigh in remaining:
                    stack.append(neigh)
                    remaining.remove(neigh)


        return len(remaining) == 0

if __name__ == "__main__":
    with open("input.txt") as f:
        n,m = map(int, f.readline().split())

        graph = Graph(n)

        for _ in range(m):
            a,b = map(int, f.readline().split())
            graph.add_edge(a,b)

        if graph.is_connected():
            print("YES")
        else:
            print("NO")