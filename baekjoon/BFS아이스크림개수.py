#Queue + BFS + 2차원배열 graph 탐색

from collections import deque

def bfs(graph,i,j,visited):
    global row , col
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx ,ny = x+dx[k], y+dy[k]
            if nx<0 or ny<0 or nx>=row or ny>=col:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx,ny))
                visited[nx][ny] = True
    return 

row , col = map(int,input().split()) 
box = []
for i in range(row):
    box.append(list(map(int,input())))

#map함수는 리스트 혹은 str을 받아와서 이 덩어리에서 각각의 요소로 객체화 시킴
"""
"""

visited = [[False for i in range(col)] for j in range(row)]
count = 0

for i in range(row):
    for j in range(col):
        if box[i][j] == 0 and visited[i][j] == False:
            bfs(box,i,j,visited)
            count += 1

print(count)