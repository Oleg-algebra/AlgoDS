import os
import time
from collections import deque

# Константи для стану клітинок
EMPTY = 0
VISITED = 1

# Символи для відображення в консолі
WALL_CHAR = "*"  # Стіна
CELL_CHAR = "·"  # Недосліджена клітинка
VISITED_CHAR = "▒"  # Досліджена клітинка
CURRENT_CHAR = "@"  # Поточна клітинка в обробці


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def _clear_console(self):
        # Очищення консолі для Windows (cls) та Linux/Mac (clear)
        os.system('clear')

    def _draw(self, wave_matrix, current_pos):
        """Метод для малювання поточного стану лабіринту"""
        self._clear_console()
        output = []
        for i in range(self.n):
            row = []
            for j in range(len(self.maze[i])):
                if (i, j) == current_pos:
                    row.append(CURRENT_CHAR)
                elif self.maze[i][j] == WALL_CHAR:
                    row.append(WALL_CHAR)
                elif wave_matrix[i][j] == VISITED:
                    row.append(VISITED_CHAR)
                else:
                    row.append(CELL_CHAR)
            output.append(" ".join(row))

        print("\n".join(output))
        print(f"\nExplored cells: {sum(row.count(VISITED) for row in wave_matrix)}")
        time.sleep(1)

    def bfs_count_area(self, si, sj):
        wave_matrix = [[EMPTY] * self.n for _ in range(self.n)]
        wandering =  [[EMPTY] * self.n for _ in range(self.n)]
        count = 0
        queue = deque()

        queue.append((si, sj))
        wave_matrix[si][sj] = VISITED
        while queue:
            i, j = queue.popleft()
            count += 1

            # Візуалізуємо кожен крок
            self._draw(wandering, (i, j))
            wandering[i][j] = VISITED

            for di, dj in self.directions:
                ni, nj = i + di, j + dj

                # Перевірка меж та стану

                if self.maze[ni][nj] == "." and wave_matrix[ni][nj] == EMPTY:
                    wave_matrix[ni][nj] = VISITED
                    queue.append((ni, nj))


        return count


if __name__ == "__main__":
    # time.sleep(2)
    with open("input.txt") as f:
        n = int(f.readline().strip())

        maze_matrix = [
            list(f.readline().strip()) for _ in range(n)
        ]

        si,sj = map(lambda x: int(x) - 1, f.readline().split())

        maze = Maze(maze_matrix)
        print(maze.bfs_count_area(si,sj))
