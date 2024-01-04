import heapq

n = int(input())
h = []
output = []

for _ in range(n):
    ip = int(input())
    if ip == 0:
        if len(h) == 0:
            output.append(0)
        else:
            output.append(heapq.heappop(h))
    else:
        heapq.heappush(h,ip)

for i in output:
    print(i)   
