from collections import deque

def bfs(graph,start,visited):
    q = deque()
    q.append((start,0))
    visited[start] = True 
    count = 0
    while q:
        x,generation = q.popleft()
        visited[x] = True
        count = count + generation
        for i in graph[x]:
            if visited[i] == False:
                q.append((i,generation+1))
    return count

n,m = map(int,input().split()) #n==노드개수 m==엣지개수
graph = [[] for _ in range(n+1)]
count_list = [0 for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited = [False for _ in range(n+1)]
    count_list[i] = bfs(graph,i+1,visited)

print(count_list.index(min(count_list))+1)

