import sys
from collections import deque

input = sys.stdin.readline

class Node:
    def __init__(self,data,left_node,right_node,dis):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        self.dis = dis

def in_order(node,col_l):
    if node.left_node != None:
        in_order(tree[node.left_node],col_l)
    col_l.append(node.data)
    if node.right_node != None:
        in_order(tree[node.right_node],col_l)

def bfs(tree,visited,depth,start):
    q = deque()
    q.append(tree[start])
    depth[start] = 1
    while q:
        v = q.popleft()
        visited[v.data][0] = True
        if v.left_node != None and visited[v.left_node][0] == False:
            q.append(tree[v.left_node])
            depth[v.left_node] = depth[v.data] + 1
        if v.right_node != None and visited[v.right_node][0] == False:
            q.append(tree[v.right_node])
            depth[v.right_node] = depth[v.data] + 1

n = int(input().rstrip())
tree = {}
col_l = [0]
visited = [[False,0] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]
root = n*(n+1)//2

for i in range(n):
    data, left_node, right_node = map(int,input().rstrip().split())
    if left_node != -1:
        root -= left_node
    if right_node != -1:
        root -= right_node

    if left_node == -1:
        left_node = None
    if right_node == -1:
        right_node = None
    tree[data] = Node(data,left_node,right_node,0)
#print("root",end = " ")
#print(root)

in_order(tree[root],col_l)
#print("col_l",end = " ")
#print(col_l) 
col_index = [0 for _ in range(n+1)]
for i in range(1,n+1):
    col_index[col_l[i]] = i
#print("col_index",end = " ")
#print(col_index)

bfs(tree,visited,depth,root)
#print("depth",end = " ")
#print(depth)

set_l = []
for i in range(1,n+1):
    set_l.append((depth[i],col_index[i]))
#print("set_l",end = " ")
#print(set_l)
sorted_list = sorted(set_l, key=lambda x: (x[0], x[1]))
sorted_list.insert(0,0)
#print("sorted_list",end=" ")
#print(sorted_list)

out_l = []
index = 1
for i in range(1,n+1): #1이랑 2만 돌림 1돌렸을때는 어떤 if문도 x  2일때 2번째를 돌려야 하는데 1번째 돌리고 끝남
    if i == n:
        width = sorted_list[i][1] - sorted_list[index][1] + 1
        out_l.append((sorted_list[index][0],width))
        break
    if sorted_list[index][0] != sorted_list[i+1][0]: #깊이가 달려질때
        width = sorted_list[i][1] - sorted_list[index][1] + 1
        out_l.append((sorted_list[index][0],width))
        index = i + 1
#print("out_l",end = " ")
#print(out_l)
last_depth = 0
last_width = 0
for i in range(len(out_l)):
    if out_l[i][1] > last_width:
        last_depth = out_l[i][0]
        last_width = out_l[i][1]
print(last_depth, end = ' ')
print(last_width)