import sys
input = sys.stdin.readline
INF = int(1e9)

def find_max(left,right):
    if left >= right:
        return left
    else: 
        return right

def find_min(left,right):
    if left >= right:
        return right
    else:
        return left

def build_max(stree,node,left,right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]

    mid = left + (right - left)//2 
    left_val = build_max(stree,2*node,left,mid)
    right_val = build_max(stree,2*node+1,mid+1,right)
    stree[node] = find_max(left_val,right_val)
    return stree[node]

def build_min(stree,node,left,right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]

    mid = left + (right - left)//2 
    left_val = build_min(stree,2*node,left,mid)
    right_val = build_min(stree,2*node+1,mid+1,right)
    stree[node] = find_min(left_val,right_val)
    return stree[node]

def query_max(start,end,node,left,right):
    if end < left or start > right:
        return 0
    if start <= left and right <= end:
        return stree_max[node]
    
    mid = left + (right-left)//2
    left_val = query_max(start,end,2*node,left,mid)
    right_val = query_max(start,end,2*node+1,mid+1,right)
    return find_max(left_val,right_val)

def query_min(start,end,node,left,right):
    if end < left or start > right:
        return INF
    if start <= left and right <= end:
        return stree_min[node]
    
    mid = left + (right-left)//2
    left_val = query_min(start,end,2*node,left,mid)
    right_val = query_min(start,end,2*node+1,mid+1,right)
    return find_min(left_val,right_val)


n,m = map(int,input().rstrip().split())
arr = []

i = 1
while(True):
    if (2**i-1) >= n:
        stree_num = 2**i-1
        break
    i += 1
stree_min = [0 for _ in range(4*n)]
stree_max = [0 for _ in range(4*n)]

for i in range(n):
    arr.append(int(input().rstrip()))

build_max(stree_max,1,0,n-1)
build_min(stree_min,1,0,n-1)


max_l = []
min_l = []

for j in range(m):
    a,b = map(int,input().rstrip().split())
    max_l.append(query_max(a-1,b-1,1,0,n-1))
    min_l.append(query_min(a-1,b-1,1,0,n-1))

for i in range(len(max_l)):
    print(min_l[i],end=" ")
    print(max_l[i])

