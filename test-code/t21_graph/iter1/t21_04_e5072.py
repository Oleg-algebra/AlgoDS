

def count_edges(matrix:list[list[int]]) -> int:
    counter = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            counter += matrix[i][j]

    return counter


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(int,f.readline().split()))
            matrix.append(row)

        print(count_edges(matrix))