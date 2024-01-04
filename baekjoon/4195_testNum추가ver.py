import sys
input = sys.stdin.readline

def union_parent(parent,a,b):
    global node_n
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
        node_n[a] = node_n[a] + node_n[b]
    elif a > b:
        parent[a] = b
        node_n[b] = node_n[a] + node_n[b]

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a] 

test_n = int(input())
for _ in range(test_n):
    m = int(input()) 
    name = {}
    parent = [] 
    num = 0
    node_n = []
    for _ in range(m):
        a,b = map(str,input().split())
        if a not in name:
            name[a] = num
            parent.append(num)
            node_n.append(1)
            num += 1
        if b not in name:
            name[b] = num
            parent.append(num)
            node_n.append(1)
            num += 1
        a_id = name[a]
        b_id = name[b]
        union_parent(parent,a_id,b_id)
        print(node_n[find_parent(parent,a_id)])
