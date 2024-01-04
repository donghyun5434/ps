from collections import deque

def bfs(graph,start_row,start_col,visited):
    global n
    queue = deque([(start_row,start_col)])
    visited[start_row][start_col] = True
    popular = 0

    dx = [0,-1,1,0]
    dy = [-1,0,0,1]

    while queue:
        v = queue.popleft()
        popular += 1
        for i in range(len(dx)):
            nx = v[1] + dx[i]
            ny = v[0] + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif graph[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny,nx))
                visited[ny][nx] = True
    #print(visited)
    return popular

n = int(input())
popular_list = []
graph = []
visited = [[False for i in range(n)] for j in range(n)]
for _ in range(n):
    graph.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            popular_list.append(bfs(graph,i,j,visited))

popular_list.sort() 
print(len(popular_list))       
for i in range(len(popular_list)):
    print(popular_list[i])