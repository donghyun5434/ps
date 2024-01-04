import sys
from heapq import heappush,heappop
input = sys.stdin.readline

max_heap = []
min_heap = []
n = int(input().rstrip())
l = []

for i in range(n):
    data = int(input().rstrip())
    if i == 0:
        heappush(min_heap,data)
        l.append(data)
        continue
    if i % 2 == 1:
        heappush(max_heap,-data)
    else:
        heappush(min_heap,data)
    max_val = -(heappop(max_heap))
    min_val = heappop(min_heap)
    if max_val > min_val:
        heappush(min_heap,max_val)
        heappush(max_heap,-(min_val))
    else:
        heappush(min_heap,min_val)
        heappush(max_heap,-(max_val))
    if i % 2 == 0:
        l.append(min_heap[0])
    else:
        l.append(-(max_heap[0]))

for i in l:
    print(i)