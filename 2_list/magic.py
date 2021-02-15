def read_matrix():
    n = int(input())
    m = []
    for i in range(n):
        a = [int(x) for x in input().split()]
        m.append(a)


    return m
    
def print_matrix(m):
    for row in m:   # для каждой строки
        print(*row) # печатать все элементы строки через пробел
        
def sum_row(m, i):
    return sum(m[i])
    
def sum_col(m, col):
    b = [m[i][col] for i in range(len(m))]
    return sum(b)
    
def sum_diag(m):
    b = [m[i][i] for i in range(len(m))]
    return sum(b)
        
def sum_diag2(m):
    n = len(m)
    b = [m[i][n-1-i] for i in range(n)]
    return sum(b)
    
def magic(m):
    n = len(m)
    d = sum_diag(m)
    if d != sum_diag2(m):
        return False
    for i in range(n):
        if d != sum_col(m, i) or d != sum_row(m, i):
            return False
            
    return True

m = read_matrix()
#k = int(input())
#print_matrix(m)
#print(sum_diag2(m))        
if magic(m):
    print('MAGIC')
else:
    print('NO')
