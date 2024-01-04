import sys
from heapq import heappush,heappop
input = sys.stdin.readline

negt_heap = []
post_heap = []

n = int(input().rstrip())
l = []

for i in range(n):
    data = int(input().rstrip())
    if data < 0:
        heappush(negt_heap,-data)
    elif data > 0:
        heappush(post_heap,data)
    else: # 0일때 가장작은 값을 출력
        if len(negt_heap) == 0 and len(post_heap) == 0:
            l.append(0)
        elif len(negt_heap) == 0 and len(post_heap) != 0:
            l.append(heappop(post_heap))
        elif len(negt_heap) != 0 and len(post_heap) == 0:
            l.append(-heappop(negt_heap))
        else:
            neg_abs = negt_heap[0]
            pos_abs = post_heap[0]
            if neg_abs <= pos_abs:
                l.append(-neg_abs)
                heappop(negt_heap)
            elif neg_abs > pos_abs:
                l.append(pos_abs)
                heappop(post_heap)
for i in l:
    print(i)
