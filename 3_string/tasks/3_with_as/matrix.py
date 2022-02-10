def read_matrix1():
    n = int(input())
    m = []
    for i in range(n):
        line = input()
        m.append(list(map(int, line.split())))
    return m

def read_matrix():
    # n = int(input())
    m = [list(map(int, input().split())) for i in range(int(input()))]
    return m
    
def trans1(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    nrow = len(m)                       # сколько строк в матрице
    ncol = len(m[0])                    # сколько столбцов в матрице
    tm = [[0]*nrow for i in range(ncol)]
    print(tm)                           # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for irow in range(nrow):
        for icol in range(ncol):
            tm[icol][irow] = m[irow][icol]

    print(tm)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

def trans2(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    nrow = len(m)                       # сколько строк в матрице
    ncol = len(m[0])                    # сколько столбцов в матрице
    tm = [[] for i in range(ncol)]
    print(tm)                           # [[], [], [], []]
    for irow in range(nrow):
        for icol in range(ncol):
            tm[icol].append(m[irow][icol])
        print(m)                        # [[1], [2], [3], [4]]
                                        # [[1, 5], [2, 6], [3, 7], [4, 8]]
                                        # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

def trans3(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    nrow = len(m)                       # сколько строк в матрице
    ncol = len(m[0])                    # сколько столбцов в матрице
    tm = [[m[irow][icol] for irow in range(nrow)] for icol in range(ncol)]
    print(tm)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

def trans(m):
    print(m)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(*m)                           # [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
    print(list(zip(*m)))                # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
    tm = [list(row) for row in zip(*m)]
    print(tm)                           # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    
m = read_matrix()
trans(m)