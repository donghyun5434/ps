import sys
input = sys.stdin.readline
INF = int(1e9)

def min_finder(left,right):
    if left >= right:
        return right
    else:
        return left

def builder(stree,node,left,right): 
    if left == right:
        stree[node] = ori_l[left]
        return stree[node]
    
    mid = left + (right-left)//2
    left_val = builder(stree,2*node,left,mid)
    right_val = builder(stree,2*node+1,mid+1,right)
    stree[node] = min_finder(left_val,right_val)
    return stree[node]


def min_query(start,end,node,left,right):
    if start < left or start >right:
        return INF
    if start <= left and right <= end:
        return stree[node]
    mid = left +(right-left)//2
    left_val = min_query(start,end,2*node,left,mid)
    right_val = min_query(start,end,2*node+1,mid+1,right)
    return min_finder(left_val,right_val)
    

n,m = map(int,input().rstrip().split())
ori_l = []

i = 0
while(True):
    if 2**i-1 > len(ori_l):
        stree_n = 2**i-1
        break
stree = [0 for _ in range(stree_n+1)]

for _ in range(n):
    data = int(input().rstrip())
    ori_l.append()

builder(stree,1,0,len(ori_l))

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    print(min_query(stree,1,a,b))
