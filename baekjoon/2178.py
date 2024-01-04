from collections import deque

def bfs(graph,start_row,start_col,count,visited):
    global row,col
    queue = deque([(start_row,start_col,count)])
    visited[start_row][start_col] = True
    dy = [-1,0,1,0]
    dx = [0,-1,0,1]
    while queue:
        v = queue.popleft()
        if v[0] == row-1 and v[1] == col-1:
            return v[2]
        for i in range(len(dx)):
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            if nx < 0 or ny < 0 or nx >= col or ny >= row:
                continue
            elif graph[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny,nx,v[2]+1))
                visited[ny][nx] = True

row,col = map(int,input().split())
graph = []
visited = [[False for i in range(col)] for j in range(row)]

for _ in range(row):
    graph.append(list(map(int,input())))

print(bfs(graph,0,0,1,visited))
