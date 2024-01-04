# BFS로 풀어 보겠읍니다
from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph,visited,graph_size,start):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue = deque([(start[0],start[1])])
    visited[start[0]][start[1]] = True

    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        #visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > (graph_size-1) or ny < 0 or ny > (graph_size-1):
                continue
            elif visited[nx][ny] == False and graph[start[0]][start[1]] == graph[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
            else:
                continue



n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(str,input())))


visited = [[False for _ in range(n)] for _ in range(n)]
normal_count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(graph,visited,n,(i,j))
            #print(visited)
            normal_count += 1
print(normal_count,end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False for _ in range(n)] for _ in range(n)]
jrsy_count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(graph,visited,n,(i,j))
            #print(visited)
            jrsy_count += 1

print(jrsy_count)