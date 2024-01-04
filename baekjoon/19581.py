import sys
from collections import deque

def bfs(graph,visited,start,cost_sum):
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
l = []
for i in range(n-1):
    parent,child,cost = map(int,input().rstrip().split())
    graph[parent].append((child,cost))
    graph[child].append((parent,cost))
bfs(graph,visited,1,cost_sum)
dot1 = cost_sum.index(max(cost_sum))

visited = [False for _ in range(n+1)]
from_dot1_cost_sum = [0 for _ in range(n+1)]
bfs(graph,visited,dot1,from_dot1_cost_sum)
dot2 = from_dot1_cost_sum.index(max(from_dot1_cost_sum))
#지름 양 끝의 점은 dot1 과 dot2이다
from_dot2_cost_sum = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
bfs(graph,visited,dot2,from_dot2_cost_sum)
del from_dot1_cost_sum[dot2]
del from_dot2_cost_sum[dot1]
new_cost_sum = from_dot2_cost_sum + from_dot1_cost_sum
new_cost_sum.sort()

print(new_cost_sum[-1])