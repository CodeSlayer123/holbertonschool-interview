def rotate_2d_matrix(matrix):
    size = (len(matrix))
    result = []
    for i in range(size):
        result.append([])
    for i in range(size):
        index = size - 1
        index2 = 0

        for j in range(size):
            print(index)
            result[i].append(matrix[index][0])
            index -= 1
            index2 += 1
        index += 1
    #result[0].append(matrix[size - 1][0])
    #result[0].append(matrix[size - 1][1])
    #result[0].append(matrix[size - 1][2])

    #result[1].append(matrix[size - 1][0])
    #result[1].append(matrix[size - 1][1])
    #result[1].append(matrix[size - 1][2])

    #print(size)
    print(matrix[size - 2])
    print(result)