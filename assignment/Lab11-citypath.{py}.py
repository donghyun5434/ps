import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

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
                distance[i[0]] = cost+1
                heapq.heappush(q,(cost,i[0]))

n = int(input())
graph = [[] for _ in range(n+1)]
graph_deg = [0 for _ in range(n+1)]
distance = [INF for _ in range(n+1)]


for i in range(n):
    input_list = list(map(int,input().split()))
    s = input_list[0]
    for j in range(1,len(input_list)-1):
        graph[s].append([input_list[j],0])  #graph = [[],[(1,cost)]] 
for i in range(1,n+1):
    graph_deg[i] = len(graph[i])
for i in range(1,n+1):
    for j in graph[i]:
        j[1] = graph_deg[j[0]]

#print(graph)

out_list = []
for i in range(1,n+1):
    distance = [INF for _ in range(n+1)]
    dijkstra(i)
    for j in range(1,n+1):
        distance[j] = distance[j] - graph_deg[j]
    #print(max(distance[1:]))
    out_list.append(max(distance[1:]))

print(max(out_list))