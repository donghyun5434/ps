from queue import PriorityQueue

n = int(input())
l = []
que = PriorityQueue()

for _ in range(n):
    que.put(int(input()))

result = 0
for i in range(n-1):
    pack = que.get() + que.get()
    que.put(pack)
    result += pack

print(result)