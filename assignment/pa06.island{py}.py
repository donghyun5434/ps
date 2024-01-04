def search(i,j,map):

    q = []
    q.append((i,j))
    check[i][j] = True
    count = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q: 
        x,y =q.pop(0)

        for k in range(4):
            nx,ny = x+dx[k] , y+dy[k]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            if map[nx][ny] == '0':
                if not check[nx][ny]:
                    map[nx][ny] = '9'
                    count += 1
                    check[nx][ny] = True
                    q.append((nx,ny))   
    return count


m,n = input().split()
m = int(m)
n = int(n)

if (m*n) % 80 == 0: 
    row = (m*n)//80
else:
    row = (m*n)//80 + 1

ip = ""
for i in range(0,row):
    new_ip = input()
    ip = ip + new_ip

u = input()

map = []
for i in range(0,n):
    start = m*i
    end = m*(i+1)
    map.append(list(ip[start:end]))


check = [ [False]*(m) for _ in range(n) ]

sea = search(0,0,map)

print(m*n - sea)