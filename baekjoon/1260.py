from collections import deque

def bfs(graph,visited,v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        print(x,end=" ")
        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

def dfs(graph,visited,v):
    print(v,end=" ")
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,visited,i)
    return

n,m,v = map(int,input().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in graph:
    i.sort()

visited = [False for _ in range(n+1)]
dfs(graph,visited,v)
print()
visited = [False for _ in range(n+1)]
bfs(graph,visited,v)
