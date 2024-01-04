from collections import deque

def bfs(graph,start,visited,parent_list):

    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                parent_list[i] = v
                q.append(i)
                visited[i] = True
    return

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
parent_list = [-1 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph,1,visited,parent_list)
#print(parent_list)

for i in range(2,n+1):
    print(parent_list[i])