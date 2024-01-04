import sys
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input().rstrip())
max_heap = PriorityQueue() #maxheap을 구현하기 위해서는 -data로 입력,다시 -data로 출력
min_heap = PriorityQueue() 
pre_mid = 0
l = [] #중간값을 모아두는 리스트

for i in range(n): #번갈아가며 넣되 min_val > max_val 이면 이 둘을 교환한다
    data = int(input().rstrip())
    if i == 0:
        min_heap.put(data)
        l.append(data)
        continue
    if i % 2 == 1:
        max_heap.put(-(data))
    else:
        min_heap.put(data)
    max_val = -(max_heap.get())
    min_val = min_heap.get()
    if max_val > min_val:
        min_heap.put(max_val)
        max_heap.put(-(min_val))
    else:
        max_heap.put(-(max_val))
        min_heap.put(min_val)
    if i % 2 == 0:
        mid_val = min_heap.get()
        min_heap.put(mid_val)
        l.append(mid_val)
    else:
        mid_val = -(max_heap.get())
        max_heap.put(-(mid_val))
        l.append(mid_val)

for i in l:
    print(i)
    