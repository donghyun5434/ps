from collections import deque

def bfs (n,k):
    q = deque()
    q.append((n,0,0))
    graph[n] = True

    while q:
        t = [0,0,0]
        #x,generation,parent_x = q.popleft()
        x,generation = q.popleft()
        l.append(t)
        if x == k:
            min_len = generation
            break
        generation += 1
        n1 = x + 1
        if n1 >= 0 and n1<=100000 and graph[n1] != True:
            q.append((n1,generation,x))
            graph[n1] = True
        n2 = x - 1
        if n2 >= 0 and n2 <= 100000 and graph[n2] != True:
            q.append((n2,generation,x))
            graph[n2] = True
        n3 = x * 2
        if n3 >= 0 and n3 <= 100000 and graph[n3] != True:
            q.append((n3,generation,x))
            graph[n3] =True


    return min_len

"""
def path_finder(sub_list):
    path.append(sub_list[0])
    if sub_list[1] == 0:
        return
    new_list = l[0:l.index(sub_list)]
    for i in new_list:
        if i[0] == sub_list[2]:
            sub_list = i 
    return path_finder(sub_list)

def path_finder(sub_list):
    global output , l
    p = sub_list
    path.append(p)
    for j in range(output):
        for i in l:
            if i[0] == p[2]:
                path.append(i)
                p = i
                l = l[:l.index(i)]
                #print(l)
    return 
"""

n,k = map(int,input().split())
graph = [False for i in range(100001)]
l = []
path = []
#(위치,generation,부모위치)
output = bfs(n,k)
print(output)
"""
path_finder(l[-1])
path.reverse()
for i in path:
    print(i[0],end=" ")
"""
print(l)