import sys
sys.setrecursionlimit(10**5)

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

n,m = map(int,input().split())
parent = [(i) for i in range(n+1)]
out_list = []

for _ in range(m):
    w,a,b = map(int,input().split())
    if w == 0: #union 연산
        union_parent(parent,a,b)
    if w == 1: #find 연산
        parent_a = find_parent(parent,a)
        parent_b = find_parent(parent,b)
        if parent_a == parent_b:
            out_list.append("YES")
        else:
            out_list.append("NO")

for i in out_list:
    print(i)