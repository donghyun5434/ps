from collections import deque
import copy
import sys 
input = sys.stdin.readline

def bfs():
    test_graph = copy.deepcopy(graph)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([])
    for i in virus:
        queue.append((i[0],i[1]))
        visited[i[0]][i[1]] = True

    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>(n-1) or ny<0 or ny>(m-1):
                continue
            elif test_graph[nx][ny] == 1:
                continue
            elif visited[nx][ny] == False and test_graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny))

    sum = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == True:
                sum += 1
    sum_l.append(sum)


def makewall(count):
    if count == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    makewall(count+1)
                    graph[i][j] = 0  

n,m = map(int,input().split())
graph = []
virus = [] #바이러스 위치를 튜플 형태로 가진다. 원소 개수는 바이러스 개수이다 
sum_l = []

# graph 완성 + virus 좌표 확보
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 2:
            virus.append((i,j))
    graph.append(row)

makewall(0)
print(sum_l.max())