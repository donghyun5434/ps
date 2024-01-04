num_lst = [1,2,5,3,9,6,5,3,2]
print('num_lst : ',num_lst)

"""
-create segment tree
-segment tree의 크기를 "넉넉하게"많이 잡아 준거임
-정확히는 num_lst의 원소들이 binary_tree에 할당되기때문에 노드의 개수는 2^(n-1)-1 <= 개수 <= 2^n-1
-객체 리스트를 먼저 (1)segment_tree에 할당시키고 (2)트리의 노드를 다시 정렬된 리스트에 할당한다

-자료구조 (1) 원시 list >> (2) 구간합을 노드 값으로 가지는 segment_tree >> (3) 정렬된 리스트
-정렬된 리스트?????
    이진 분할(: 리스트의 원소 개수가 1개 될때까지 길이를 1/2로 나눠서 새로운 리스트를 만드는 작업)
    이진 분할된 리스트의 누적합을 어떤 순서로 리스트에 담는지
    
"""
stree = [0 for x in range(4*len(num_lst))]

def merge(left,right):
    return left + right

def build(stree,node,left,right):
    #leaf node
    if left == right:
        stree[node] = num_lst[left]
        return stree[node]
    
    mid = left + (right - left)//2   # left(start)와right(end)의 중앙 == left + 길이의 절반을 붙여주기
    left_val = build(stree,2*node,left,mid)
    right_val = build(stree,2*node+1,mid+1,right)
    stree[node] = merge(left_val,right_val)
    return stree[node]

build(stree,1,0,len(num_lst)-1)

def query(start,end,node,left,right):
    if end < left or start > right:
        return 0
    if start <= left and right <= end:
        return stree[node]
    
    mid = left + (right-left)//2
    left_val = query(start,end,2*node,left,mid)
    right_val = query(start,end,2*node+1,mid+1,right)
    return merge(left_val,right_val)

print("===query===")
print("sum 0 to 5 : ",query(0,5,1,0,len(num_lst)-1))
print("sum 4 to 7 : ",query(4,7,1,0,len(num_lst)-1))