def stuff_matrix(size,matrix):
    if size == 1:
        matrix[0][0] = 0
        matrix[0][1] = 1
        matrix[1][0] = 2
        matrix[1][1] = 3
        return
    else:
        stuff_matrix(size-1,matrix)
        for i in range(2**size):
            for j in range(2**size):
                sector = find_sector(size,i,j)
                if sector == 1:
                    matrix[i][j] = matrix[i][j-2**(size-1)] + 2**(2*(size-1))*sector
                elif sector == 2:
                    matrix[i][j] = matrix[i-2**(size-1)][j] + 2**(2*(size-1))*sector
                elif sector == 3:
                    matrix[i][j] = matrix[i-2**(size-1)][j-2**(size-1)] + 2**(2*(size-1))*sector

def find_sector(n,i,j):
    if 0 <= i and i <= 2**(n-1)-1:
        if 2**(n-1) <= j and j <=2**(n)-1:
            return 1
    if 2**(n-1) <= i and i <= 2**(n)-1:
        if 0 <= j and j <= 2**(n-1)-1:
            return 2
    if 2**(n-1) <= i and i <= 2**(n)-1:
        if 2**(n-1) <= j and j <=2**(n)-1:
            return 3
    if 0 <= i and i <= 2**(n-1)-1:
        if 0 <= j and j <=2**(n-1)-1:
            return 0


n,r,c = map(int,input().split())
#n = 3
matrix = [[0 for _ in range(2**n)] for _ in range(2**n)]
"""
for i in range(2**n):
    for j in range(2**n):
        matrix[i][j] = find_sector(3,i,j)

for i in range(2**n):
    print(matrix[i])
"""
stuff_matrix(n,matrix)

"""
for i in range(2**n):
    print(matrix[i])
"""
print(matrix[r][c])
