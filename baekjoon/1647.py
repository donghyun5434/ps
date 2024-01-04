def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]


n,m = map(int,input().split())
table = []
parent = [i for i in range(n+1)]
result = 0
result_list = []

for _ in range(m):
    a,b,c = map(int,input().split()) #a->b c는 비용
    table.append((c,a,b))

table.sort() 

for i in table:
    #i[0] == cost, i[1] == 시작노드, i[2] == 도착노드
    if find_parent(parent,i[1]) != find_parent(parent,i[2]):
        union_parent(parent,i[1],i[2])
        result_list.append(i[0])

print(sum(result_list)-result_list[-1])