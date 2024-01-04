from collections import deque

def bfs(graph,o_tomato_list):
    global row,col
    queue = deque()
    if len(o_tomato_list) == 0:
        return -1
    
    for i in o_tomato_list:
        queue.append(i)

    dx = [0,-1,1,0]
    dy = [-1,0,0,1]

    while queue:
        v = queue.popleft()
        for i in range(len(dx)):
            nx = v[1] + dx[i]
            ny = v[0] + dy[i]
            if nx < 0 or ny < 0 or nx >= col or ny >= row:
                continue
            elif graph[ny][nx] == 0:
                queue.append((ny,nx,v[2]+1))
                graph[ny][nx] = 1
    #print(graph)
    return v[2]
    

col, row = map(int,input().split())
graph = []
o_tomato_list = []
for _ in range(row):
    graph.append(list(map(int,input().split())))

#최초에 존재하는 토마토를 알아내기
for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            o_tomato_list.append((i,j,0))

result = bfs(graph,o_tomato_list)

for i in range(row):
    for j in range(col):
        if graph[i][j] == 0:
            result = -1

if result == -1:
    print(result)   
else:
    print(result)