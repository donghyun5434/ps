import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #다른 장치없으면 min_heap
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        #dist는 누적거리,now는 현재 노드
        if distance[now] < dist:
            continue
        for i in graph[now]:   #i는 graph[현재노드] i[0] = now노드와 연결된 노드 , i[1] = 그 노드까지 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
