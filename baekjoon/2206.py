import sys
from collections import deque

def bfs(graph,visited,result_l):
    global n,m 
    q = deque() #y,x,dis
    q.append([0,0,1])
    visited[0][0] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    #동,서,북,남
    while q:
        data = q.popleft()
        #print(data)
        y = data[0]
        x = data[1]
        dis = data[2]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            else:
                if visited[ny][nx] == False and graph[ny][nx] == 0:
                    q.append((ny,nx,dis+1))
                    visited[ny][nx] = True
    if y == n-1 and x == m-1:
        result_l.append(dis)
        return
    else:
        result_l.append(-1)
        return 


input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
graph =[]
result_l = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    data = list(map(int,input().rstrip()))
    graph.append(data)

bfs(graph,visited,result_l)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            visited = [[False for _ in range(m)] for _ in range(n)]
            graph[i][j] = 0 #다시 1로 복원시켜줘야함
            bfs(graph,visited,result_l)
            graph[i][j] = 1

result_l.sort()

#print(result_l)
if result_l[-1] == -1:
    print(-1)
else: 
    for i in result_l:
        if i > 0:
            print(i)
            break