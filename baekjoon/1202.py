import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
l = []
heap = []

for i in range(n):
    wei,cost = map(int,input().rstrip().split())
    l.append((-cost,wei))
for i in range(k):
    bag_wei = int(input().rstrip())
    l.append((0,bag_wei))

sort_l = sorted(l,key=lambda x : x[1])
#print(sort_l)
cost_sum = 0
for i in sort_l:
    if i[0] == 0:
        if len(heap) != 0:
            out = heappop(heap)
            out_cost = -out[0]
            cost_sum += out_cost
    else:
        heappush(heap,i)
print(cost_sum)