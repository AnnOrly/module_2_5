def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)


get_matrix(2, 5, 4)
get_matrix(3, 9, 11)
get_matrix(6, 7, 8)

