from collections import deque

def bfs (n,k):
    #graph = [False for i in range(100001)]
    q = deque()
    q.append((n,1))
    min_len = 9999
    #graph[n] = True
    while q:
        x,generation = q.popleft()
        #print(x)
        if min_len < generation:
            break
        all_path.append(x)
        if x == k:
            min_len = generation
        generation += 1
        n1 = x + 1
        #if n1 >= 0 and n1<=100000: #and graph[n1] != True:
        q.append((n1,generation))
            #graph[n1] = True
        n2 = x - 1
        #if n2 >= 0 and n2 <= 100000: #and graph[n2] != True:
        q.append((n2,generation))
            #graph[n2] = True
        n3 = x * 2
        #if n3 >= 0 and n3 <= 100000: #and graph[n3] != True:
        q.append((n3,generation))
            #graph[n3] =True
        
    return min_len

def sum(g):
    return int((3**g-1)/2)

def path_finder(path,generation):
    #generation을 1씩 줄이면서 재귀함수쓰면서 프린트 하면 될듯한?
    global n
    if generation == 1:
        shortest_path.append(n)
        return
    generation_list = all_path[sum(generation-1):sum(generation)]
    shortest_path.append(path)
    #print(shortest_path)
    #print(generation_list)
    #print(len(generation_list))
    path_index = generation_list.index(path)
    parent_index = path_index//3
    #print(parent_index)
    generation_list = all_path[sum(generation-2):sum(generation-1)]
    #parent_path = generation_list.index(path)//3
    return path_finder(generation_list[parent_index],generation-1)


#입력부
n,k = map(int,input().split())
all_path = []
shortest_path = []
#최단경로 도출부 bfs
output = bfs(n,k)
print(output-1)
#print(all_path)
path_finder(k,output)
shortest_path.reverse()
for i in shortest_path:
    print(i,end=" ")


