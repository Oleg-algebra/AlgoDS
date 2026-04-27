

def solve(dim: int ,matrix: list[list[int]]):
    for row in range(dim):
        for col in range(row,dim):
            if matrix[row][col] == 1:
                print(row + 1, col + 1)

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)

        solve(n,matrix)