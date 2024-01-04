import sys
input = sys.stdin.readline

def union_parent(parent,a,b): #union하는 것은 같은 집합으로 묶는 것이므로 각각의 두노드가 속하는 집합이 포함하는 원소개수를 더해서 똑같이 갱신해주면 될 듯 함
    a = find_parent(parent,a) 
    b = find_parent(parent,b)
    if a < b:
        parent[b][0] = a
    else:
        parent[a][0] = b

def find_parent(parent,a):
    if parent[a][0] != a:
        parent[a][0] = find_parent(parent,parent[a][0])
    return parent[a][0] #id를 반환한다

test_n = int(input())
for _ in range(test_n):
    m = int(input()) #m은 edge개수
    l = []
    name = {} #name딕셔너리를 사용하는 이유는 친구 추가시에 있는지 없는지 확인할때 시간복잡도를 상수로 줄이기 위해서 사용 
    parent = [] #parent table에 순차대로 친구이름이 append됨 따라서 (친구들의 저장 순서) == (parent.index(친구이름))
    # 마지막에 같은 집합에 속하는 원소 개수를 구하기 위해서 parent table을 1회 순회해야 하는데 이때 O(n)이 추가적으로 (loop안에서) 사용되는데 이는 
    # 총개수를 "누적"으로 각 id에 저장하면 O(1)으로 해결 할 수 있다 
    num = 0
    for _ in range(m):
        a,b = map(str,input().split())
        if a not in name: #딕셔너리를 사용하여 노드가 있는지? 판단시간을 줄였다
            name[a] = (num) #딕셔너리 value는 (id,count)
            parent.append([num,1])
            num += 1
        if b not in name:
            name[b] = (num)
            parent.append([num,1])
            num += 1
        a_id = name[a]
        b_id = name[b]
        union_parent(parent,a_id,b_id)

        parent[a_id][1] = parent[a_id][1] + parent[b_id][1]
        parent[parent[a_id][0]][1] = parent[a_id][1]
        parent[b_id][1] = parent[b_id][1] + parent[b_id][1]
        parent[parent[b_id][0]][1] = parent[b_id][1]

        print(parent[a_id][1])



