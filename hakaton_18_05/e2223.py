import os
import time
from collections import deque

# Константи для стану клітинок
EMPTY = -1


# Символи для відображення в консолі
WALL_CHAR = "o"  # Стіна
CELL_CHAR = "·"  # Недосліджена клітинка



class Maze:
    def __init__(self, maze,size):
        self.maze = maze
        self.size = size
        self.directions = ((1, 0, 0),
                           (0, 1, 0),
                           (-1, 0, 0),
                           (0, -1, 0),
                           (0,0,1))





    def bfs_count_area(self, si, sj,sk,ei,ej,ek):
        print(si,sj,sk)
        print(ei,ej,ek)
        print(self.size)
        wave_matrix = [[[EMPTY] * self.size[2]
                        for _ in range(self.size[1])]
                       for __ in range(self.size[0]) ]

        queue = deque()

        queue.append((si, sj, sk))
        wave_matrix[sk][si][sj] = 0
        while queue:
            i, j, k = queue.popleft()
            print(wave_matrix)
            print((i,j,k))

            # Візуалізуємо кожен крок
            if i == ei and j == ej and k == ek:
                return wave_matrix[k][i][j] * 5


            for di, dj, dk in self.directions:
                ni, nj, nk = i + di, j + dj, k + dk
                print(ni,nj,nk)
                # Перевірка меж та стану

                if nk < self.size[0] and self.maze[nk][ni][nj] == CELL_CHAR and wave_matrix[nk][ni][nj] == EMPTY:
                    wave_matrix[nk][ni][nj] = wave_matrix[k][i][j] + 1
                    queue.append((ni, nj, nk))





if __name__ == "__main__":
    # time.sleep(2)
    with open("input.txt") as f:
        h,m,n = map(int,f.readline().split())

        maze_matrix = []
        layer = []
        for _ in range(h*m + h):
            line = list(f.readline().strip())
            if line == []:
                maze_matrix.append(layer)
                layer = []
                continue
            layer.append(line)


        start = None
        end = None
        for k in range(h):
            for i in range(m):
                for j in range(n):
                    if maze_matrix[k][i][j] == "1":
                        start = (i,j,k)
                    elif maze_matrix[k][i][j] == "2":
                        end = (i,j,k)

        maze = Maze(maze_matrix,(h,m,n))
        print(maze.bfs_count_area(*start,*end))
