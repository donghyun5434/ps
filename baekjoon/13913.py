from collections import deque

def bfs ():
    global n,k
    q = deque()
    q.append(n)
    graph[n] = True
    generation[n] = 0

    while q:
        x = q.popleft()
        if x == k:
            print(generation[x])
            for j in range(generation[x]+1):
                path.append(x)
                x = move[x]
            path.reverse()
            for i in path:
                print(i,end = " ")
            break
        n1 = x + 1
        if n1 >= 0 and n1<=100000 and graph[n1] != True:
            q.append(n1)
            graph[n1] = True
            move[n1] = x
            generation[n1] = generation[x] + 1
        n2 = x - 1
        if n2 >= 0 and n2 <= 100000 and graph[n2] != True:
            q.append(n2)
            graph[n2] = True
            move[n2] = x
            generation[n2] = generation[x] + 1
        n3 = x * 2
        if n3 >= 0 and n3 <= 100000 and graph[n3] != True:
            q.append(n3)
            graph[n3] =True
            move[n3] = x
            generation[n3] = generation[x] + 1
    return 


n,k = map(int,input().split())
graph = [False for i in range(100001)]
move = [-1 for i in range(100001)]
generation = [-1 for i in range(100001)]
path = []
"""
x = 0 ~ x = 100000 동안 겹치는 지점을 중복해서 가는 경우는 애초에 무시한다
겹치는 경우는 (1)이전 generation에서 한번 지났던 곳
(2)같은 generation에서 겹치는 경우
아무튼 겹치는 지점을 다시 취급하면 이후가 반복됨
곧, 반복되는 경로를 카운트하는 경우 자체는 최단경로가 될 수 없다. 
"""
bfs()