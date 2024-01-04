def dfs(graph,visited,start):
    visited[start] = True
    for i in graph[start]:
        if not(visited[i]):
            dfs(graph,visited,i)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
    first,second = map(int,input().split())
    graph[second].append(first)
    graph[first].append(second)

dfs(graph,visited,1)
print(visited.count(True)-1)