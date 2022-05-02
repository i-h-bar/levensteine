
def distance(string_1, string_2):
    matrix: list[list[int]] = [[0 for _ in range(len(string_1) + 1)] for _ in range(len(string_2) + 1)]

    for i in range(len(string_1) + 1):
        matrix[0][i] = i

    for i in range(len(string_2) + 1):
        matrix[i][0] = i

    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[x])):
            if string_1[y - 1] == string_2[x - 1]:
                matrix[x][y] = matrix[x - 1][y - 1]
            else:
                matrix[x][y] = min(matrix[x - 1][y - 1], matrix[x - 1][y], matrix[x][y - 1]) + 1

    return matrix[-1][-1]
