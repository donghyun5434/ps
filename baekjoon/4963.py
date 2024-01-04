from collections import deque

def bfs(graph,start_row,start_col,visited):
    global n,m
    queue = deque([(start_row,start_col)])
    visited[start_row][start_col] = True
    
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]

    while queue:
        v = queue.popleft()
        #print(v)
        for i in range(len(dx)):
            nx = v[1] + dx[i]
            ny = v[0] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif graph[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny,nx))
            visited[ny][nx] = True
    #print(visited)

count_list = []

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    graph = []
    visited = [[False for i in range(n)] for j in range(m)]
    for _ in range(m):
        graph.append(list(map(int,input().split())))
    
    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(graph,i,j,visited)
                count += 1

    #print(visited)
    count_list.append(count)

for i in range(len(count_list)):
    print(count_list[i])