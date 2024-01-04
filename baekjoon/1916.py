import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

#n , m = map(int,input().split())
#start = int(input())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        if distance[node] < dis:
            continue
        for i in graph[node]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start , end = map(int,input().split())

dijkstra(start)

#print(distance)
print(distance[end])