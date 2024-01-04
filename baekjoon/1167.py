import sys
from collections import deque

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True
    cost_sum[start] = 0
    while queue:
        v = queue.popleft()  #첫번째 v는 1이고 그 다음부터는 v = [(child1,cost1),(child2,cost2)...]
        for i in graph[v]:
            child = i[0]
            cost = i[1]
            if not visited[child]:
                queue.append(child)
                visited[child] = True
                cost_sum[child] = cost_sum[v] + cost

input = sys.stdin.readline
n = int(input().rstrip())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cost_sum = [0 for _ in range(n+1)]
for i in range(n-1):
    #parent,child,cost = map(int,input().rstrip().split())
    #graph[parent].append((child,cost))
    #graph[child].append((parent,cost))
    arr = list(map(int,input().rstrip().split()))
    parent = arr[0]
    j = 1
    while arr[j] != -1:
        graph[parent].append((arr[j],arr[j+1]))
        graph[arr[j]].append((parent,arr[j+1]))
        j += 2
bfs(graph,visited,1)
dot1 = cost_sum.index(max(cost_sum))
#print(dot1)

visited = [False for _ in range(n+1)]
cost_sum = [0 for _ in range(n+1)]
bfs(graph,visited,dot1)
print(max(cost_sum))
#print(graph)
#print(graph)