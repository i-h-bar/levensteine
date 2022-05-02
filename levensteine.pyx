import numpy as np

def loop_distance(str string_1, str string_2):
    cdef int i
    for i in range(25_000):
        distance(string_1, string_2)


cdef int distance(str string_1, str string_2):
    cdef int x
    cdef int y

    cdef object[:, :] matrix = np.zeros((len(string_1) + 1, len(string_2) + 1), dtype=object)

    for x in range(matrix.shape[0]):
        matrix[x, 0] = x

    for y in range(matrix.shape[1]):
        matrix[0, y] = y

    for x in range(1, matrix.shape[0]):
        for y in range(1, matrix.shape[0]):
            if string_1[y - 1] == string_2[x - 1]:
                matrix[x, y] = matrix[x - 1, y - 1]
            else:
                matrix[x, y] = min(matrix[x - 1, y - 1], matrix[x - 1, y], matrix[x, y - 1]) + 1

    return matrix[-1, -1]