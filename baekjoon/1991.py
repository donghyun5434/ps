import sys

class Node:
    def __init__(self,data,l_node,r_node):
        self.data = data
        self.l_node = l_node
        self.r_node = r_node
        """
        if l_node == ".":
            self.l_node = None
        if r_node == ".":
            self.r_node = None
        """
def pre_order(node):#like DFS
    print(node.data,end="")
    if node.l_node != None:
        pre_order(tree[node.l_node])
    if node.r_node != None:
        pre_order(tree[node.r_node])


def in_order(node):
    if node.l_node != None:
        in_order(tree[node.l_node])
    print(node.data,end="")
    if node.r_node != None:
        in_order(tree[node.r_node])
    

def post_order(node):
    if node.l_node != None:
        post_order(tree[node.l_node])
    if node.r_node != None:
        post_order(tree[node.r_node])
    print(node.data,end="")

n = int(sys.stdin.readline().rstrip())
tree = {}
for _ in range(n):
    data,l_node,r_node = map(str,sys.stdin.readline().rstrip().split())
    if l_node == ".":
        l_node = None
    if r_node == ".":
        r_node = None
    tree[data] = Node(data,l_node,r_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])