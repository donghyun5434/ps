import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n)]
node = []
result = 0
visited = [False for _ in range(n)]
for i in range(n):
    a,b,c = map(int,input().split())
    node.append((a,b,c,0)) #x,y,z,overlap

start = 0
edge = []
while True:
    edge.clear()
    for i in range(n):
        if i != start:
            x1,y1,z1 = node[i][0],node[i][1],node[i][2]
            x2,y2,z2 = node[start][0],node[start][1],node[start][2]
            cost = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
            edge.append((cost,start,i,node[start][3]))  #start->i 일때 cost , start의 중복 횟수
    edge.sort()
    node[start][3] += 1
    visited[start] = True
    #edge = [(0,0,0,0),(0,0,0,0),.....(0,0,0,0)]
    f_index = node[start][3]           #overlap이 0이면 0
    e_index = -(node[start][3] + 1)      #overlap이 0이면 -1
    if find_parent(parent,start) != find_parent(parent,edge[f_index][2]):   #min과 union작업
        union_parent(parent,start,edge[f_index][2])
        result += edge[f_index][0]
        visited[edge[f_index][2]] = True

    start = edge[e_index][2]