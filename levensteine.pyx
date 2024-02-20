import numpy as np

def cydist(string_1: str, string_2: str) -> int:
    return _distance(string_1.encode(), string_2.encode())


cdef int _distance(const char *a, const char *b):
    cdef int x = len(a) + 1
    cdef int y = len(b) + 1
    cdef int i, j
    cdef long[:, :] d = np.zeros((x, y), dtype=np.int_)

    for i in range(x):
        d[i][0] = i

    for j in range(1, y):
        d[0][j] = j

    for i in range(1, x):
        for j in range(1, y):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

    return d[x - 1][y - 1]


def test():
    return _test()

cdef void _test():
    cdef str x = " "
    cdef str y = " "

    print(x == y)