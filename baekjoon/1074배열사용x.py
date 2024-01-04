def find_value(size,i,j):
    if i == 0 and j == 0:
        return 0
    if i == 0 and j == 1:
        return 1
    if i == 1 and j == 0:
        return 2
    if i == 1 and j == 1:
        return 3
    else:
        sector = find_sector(size,i,j)
        if sector == 1:
            out = find_value(size-1,i,j-2**(size-1)) + 2**(2*(size-1))*sector
            return out
        elif sector == 2:
            out = find_value(size-1,i-2**(size-1),j) + 2**(2*(size-1))*sector
            return out
        elif sector == 3:
            out = find_value(size-1,i-2**(size-1),j-2**(size-1)) + 2**(2*(size-1))*sector
            return out
        else:
            out = find_value(size-1,i,j)
            return out


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

print(find_value(n,r,c))

