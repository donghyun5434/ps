import heapq
INF = int(1e9)
acc_time = [INF for _ in range(100001)]

def dijkstra(start,end):
    q = []
    heapq.heappush(q,(0,start))
    acc_time[start] = 0
    while q:
        time,now = heapq.heappop(q)
        if acc_time[now] < time:
            continue
        if (now+1) >=0 and (now+1) <= 100000:
            cost = time + 1 
            if cost < acc_time[now+1]:
                acc_time[now+1] = cost
                heapq.heappush(q,(cost,now+1))
        if (now-1) >= 0 and (now-1) <= 100000:
            cost = time + 1
            if cost <  acc_time[now-1]:
                acc_time[now-1] = cost
                heapq.heappush(q,(cost,now-1))
        if (now*2) >= 0 and (now*2) <= 100000:
            cost = time
            if cost < acc_time[now*2]:
                acc_time[now*2] = cost
                heapq.heappush(q,(cost,now*2))
    return

start,end = map(int,input().split())

dijkstra(start,end)

print(acc_time[end])