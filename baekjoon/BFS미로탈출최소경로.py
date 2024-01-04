from collections import deque

def bfs():
    global row , col
    q = deque()
    q.append((0,0,1))   #q.append((row,col,generation))
    visited[0][0] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 
    
    while q:
        x,y,len = q.popleft()
        if x == (row-1) and y == (col-1):
            len_min = len
            break

        len += 1
        for k in range(4):
            #nx ,ny = x+dx[k], y+dy[k]
            nx = x + dx[k]
            ny = y + dy[k]
            if nx<0 or ny<0 or nx>=row or ny>=col:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx,ny,len))
                visited[nx][ny] = True

    return len_min

row,col = map(int,input().split())
graph = []
for i in range(row):
    graph.append(list(map(int,input())))
visited = [[False for i in range(col)] for j in range(row)]

len_min = bfs()

print(len_min)
