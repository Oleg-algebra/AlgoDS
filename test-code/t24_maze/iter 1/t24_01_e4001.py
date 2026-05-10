from collections import deque



class Maze:
    def __init__(self,matrix):
        self.wave = matrix
        self.n = len(matrix)
        self.directions = ((0,1),(1,0),(-1,0),(0,-1))

    def bfs_count_area(self,si,sj):
        visited = [
            [-1] * self.n for _ in range(self.n)
        ]

        queue = deque()
        queue.append((si,sj))
        visited[si][sj] = 1
        count = 0
        while queue:
            count += 1
            i,j = queue.popleft()

            for di,dj in self.directions:
                i1 = i + di
                j1 = j + dj

                if visited[i1][j1] == -1 and self.wave[i1][j1] == ".":

                    queue.append([i1,j1])
                    visited[i1][j1] = 1

        return count

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        maze_matrix = [
            list(f.readline().strip()) for _ in range(n)
        ]

        si, sj = map(lambda x: int(x) - 1 ,f.readline().split())

        # print(maze_matrix)
        # print((si,sj))
        maze = Maze(maze_matrix)
        print(maze.bfs_count_area(si,sj))
