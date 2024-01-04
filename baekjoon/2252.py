import sys
input = sys.stdin.readline

def topology_sort(graph,indegree,visited):
    s = []
    out_list = []
    for i in range(1,n+1):
        if indegree[i] == 0:
            s.append(i)
            visited[i] = True

    while s:
        x = s.pop()
        out_list.append(x)
        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                s.append(i)
                visited[i] = True

    return out_list

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())  #a->b
    graph[a].append(b)
    indegree[b] += 1

l = topology_sort(graph,indegree,visited)

for i in l:
    print(i,end=" ")