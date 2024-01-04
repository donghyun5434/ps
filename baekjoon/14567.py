from collections import deque

def topology_sort(graph,indegree,out):
    q = deque()
    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            q.append((i,1))
    while q:
        x,generation = q.popleft()
        out.append((x,generation))
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i,generation+1))
                

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
out = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

topology_sort(graph,indegree,out)

out.sort()

for i in range(n):
    print(out[i][1],end =" ")