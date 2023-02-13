def rotate_2d_matrix(matrix):
    size = (len(matrix))
    original = matrix[:]

    matrix.clear()
    for i in range(size):
        matrix.append([])

    for i in range(size):
        for j in range(size - 1, -1, -1):
            matrix[i].append(original[j][i])
