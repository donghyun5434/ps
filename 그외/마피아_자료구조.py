import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,visited,start_index,sec_generation_rank):
    start = graph_name_list[start_index]
    q = deque()
    q.append((start,0))
    visited[start_index] = True
    count = -1
    while q:
        x,generation = q.popleft()
        x_index = graph_name_list.index(x)
        count += 1
        for i in graph[x_index]:
            i_index = graph_name_list.index(i)
            if visited[i_index] == False:
                q.append((i,generation+1))
                visited[i_index] = True
    sec_generation_rank[start_index] = [-generation,start]
    final_rank[start_index][2] = -generation

    return count

def bfs_for_generation(graph,visited,start,generation_rank):
    start_index = graph_name_list.index(start)
    q = deque()
    q.append((start,0))
    visited[start_index] = True
    while q:
        x,generation = q.popleft()
        x_index = graph_name_list.index(x)
        generation_rank[x_index] = [generation,x]
        final_rank[x_index][1] = generation
        for i in graph[x_index]:
            i_index = graph_name_list.index(i)
            if visited[i_index] == False:
                q.append((i,generation+1))
                visited[i_index] = True
    return



n = int(input()) #n은 간선의 개수 
m = n - 1  #m은 노드의 개수

graph_name_list = []   #총 n개의 원소
graph = [[] for _ in range(n)] #총 n개의 원소
final_rank = [[0 for _ in range(4)] for _ in range(n)] #[(자식수R,계층R,관련계층R,사전R,"NODE")]

for i in range(m):
    b,a = map(str,input().split())  #a->b a가 parent임
    if a not in graph_name_list:
        graph_name_list.append(a)
    if b not in graph_name_list:
        graph_name_list.append(b)
    a_index = graph_name_list.index(a)
    graph[a_index].append(b)

#print(graph_name_list)

# 자식 수 구하기 & 자신 관할 계층구하기
child_rank = [0 for _ in range(n)]
sec_generation_rank = [0 for _ in range(n)]
for i in range(n):
    visited = [False for _ in range(n)]
    #graph_name_list = [(자식수,자기이름),....]
    child = bfs(graph,visited,i,sec_generation_rank)
    child_rank[i] = [-child,graph_name_list[i]]
    final_rank[i][0] = -child 
child_rank.sort()

#print(child_rank)
#print(final_rank)


# generation 구하기
visited = [False for _ in range(n)]
generation_rank = [0 for _ in range(n)]
bfs_for_generation(graph,visited,child_rank[0][1],generation_rank)


#generation_rank.sort()

#print(generation_rank)
#print(final_rank)

# 자신 관할 계층 구하기
#sec_generation_rank.sort()

#print(sec_generation_rank)
#print(final_rank)

# 사전순서
#dic_rank = sorted(graph_name_list)

#print(dic_rank)
for i in range(n):
    final_rank[i][3] = graph_name_list[i]
#print(final_rank)

for i in range(n):
    final_rank[i] = tuple(final_rank[i])
#print(final_rank)

"""
fi_final_rank = sorted(final_rank)

for i in range(n):
    print(fi_final_rank[3])

"""
b = sorted(final_rank)
#print(b)

for i in range(n):
    print(b[i][3])