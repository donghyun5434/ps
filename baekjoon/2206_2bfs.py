import sys
from collections import deque
INF = int(1e9)

def bfs(graph,visited,start):
    global n,m 
    q = deque() 
    start_y = start[0]
    start_x = start[1]
    q.append([start_y,start_x,1])
    if start_y == 0 and start_x == 0:
        from_start = 0
    else:
        from_start = 1

    visited[start_y][start_x] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while q:
        data = q.popleft()
        y = data[0]
        x = data[1]
        dis = data[2]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif graph[ny][nx] == 1:
                if from_start == 0:
                    #dup[ny][nx][from_start] = dis
                    if dup[ny][nx][from_start] > dis:
                        dup[ny][nx][from_start] = dis
                elif from_start == 1:
                    if dup[ny][nx][from_start] > dis:
                        dup[ny][nx][from_start] = dis
            else:
                if visited[ny][nx] == False and graph[ny][nx] == 0:
                    q.append((ny,nx,dis+1))
                    visited[ny][nx] = True
    if y == n-1 and x == m-1:
        return dis
    else:
        return -1 

input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
graph =[]
result_l = []
dup = [[[INF,INF] for _ in range(m)] for _ in range(n)]

for i in range(n):
    data = list(map(int,input().rstrip()))
    graph.append(data)
 
visited = [[False for _ in range(m)] for _ in range(n)]
result_l.append(bfs(graph,visited,[0,0]))
visited = [[False for _ in range(m)] for _ in range(n)]
bfs(graph,visited,[n-1,m-1])

for i in range(n):
    for j in range(m):
        if dup[i][j][0] != INF and dup[i][j][1] !=INF and dup[i][j][0] > 0 and dup[i][j][1]> 0 :
            result_l.append(dup[i][j][0]+dup[i][j][1]+1)

result_l.sort()

if result_l[-1] == -1:
    print(-1)
else:
    for i in result_l:
        if i > 0:
            print(i)
            break