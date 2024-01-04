def dfs(graph,visited,x,y):
    global m,n
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny] == False and graph[nx][ny] == 1:
            #visited[nx][ny] = True
            dfs(graph,visited,nx,ny)
    return


t = int(input())
bug_n_list = []

for i in range(t):
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    bug_n = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] ==False:
                dfs(graph,visited,i,j)
                bug_n += 1

    bug_n_list.append(bug_n)
    
for i in bug_n_list:
    print(i)




