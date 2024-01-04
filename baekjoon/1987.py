def dfs(graph,stack,i,j):
    global r,c,max
    l.append(graph[i][j])
    stack[graph[i][j]] = 'on'
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if y < 0 or y >= r or x < 0 or x >= c:
            continue
        if stack[graph[y][x]] == 'on':
            continue
        dfs(graph,stack,y,x)

    count = 0
    for i in range(26):
        if stack[chr(i+65)] == 'on':
            count += 1
    if count > max:
        max = count
    
    out=l.pop()
    stack[out] = 'off'
    return

r,c = map(int,input().split())
graph = []
stack = {}
l = []
for i in range(26):
    stack[chr(i+65)] = "off"
max = 0
for _ in range(r):
    l = list(map(str,input()))
    graph.append(l)

dfs(graph,stack,0,0)

print(max)