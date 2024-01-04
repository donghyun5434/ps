from collections import deque

def bfs (n,k):
    q = deque()
    q.append((n,0))
    graph[n] = True

    while q:
        x,generation = q.popleft()
        if x == k:
            min_len = generation
            break
        generation += 1
        n1 = x + 1
        if n1 >= 0 and n1<=100000 and graph[n1] != True:
            q.append((n1,generation))
            graph[n1] = True
        n2 = x - 1
        if n2 >= 0 and n2 <= 100000 and graph[n2] != True:
            q.append((n2,generation))
            graph[n2] = True
        n3 = x * 2
        if n3 >= 0 and n3 <= 100000 and graph[n3] != True:
            q.append((n3,generation))
            graph[n3] =True


    return min_len


n,k = map(int,input().split())
graph = [False for i in range(100001)]
output = bfs(n,k)
print(output)