import sys
input = sys.stdin.readline

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
node = []
edge = []
parent = [i for i in range(n)]
result = 0
for i in range(n):
    x,y,z = map(int,input().split())
    node.append((x,y,z,i))

for i in range(3):
    node.sort(key=lambda x:x[i])
    for j in range(n-1):
        edge.append((node[j+1][i]-node[j][i],node[j][3],node[j+1][3]))

edge.sort(key=lambda x:x[0])
m = len(edge)

for i in range(m):
    if find_parent(parent,edge[i][1]) != find_parent(parent,edge[i][2]): #같으면 cycle임
        union_parent(parent,edge[i][1],edge[i][2])
        result += edge[i][0]

print(result)