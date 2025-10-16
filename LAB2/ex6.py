def prob_6() -> None:
    rows, columns = map(int, input().split())

    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                if matrix[i][j] % 2 != 0:
                    matrix[i][j] = "X"
            else:
                if matrix[i][j] % 2 == 0:
                    matrix[i][j] = "X"

    for row in matrix:
        print(*row)
print (prob_6)
