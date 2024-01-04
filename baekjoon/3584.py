
test_n = int(input())

answer_list = []
for _ in range(test_n):
    node_n = int(input())
    child_graph = [[] for i in range(node_n + 1)]
    parent_graph = [-1 for i in range(node_n + 1)]
    parent_graph[0] = 0
    #인덱스와 노드의 번호를 일치시키기위하여 sub_list를 n+2개 를 만들어준다
    for _ in range(node_n-1):
        #만약 node value가 알파벳으로
        a,b = map(int,input().split())
        child_graph[a].append(b)
        parent_graph[b] = a

    ans = parent_graph.index(-1)
    generation_root = [-1 for _ in range(node_n+1)]

    node_1 , node_2 = map(int,input().split())


    #print(child_graph)
    #print(parent_graph)

    count_1 = 1
    obj = node_1
    generation_root[obj] = 0
    while True:
        if obj == ans:
            break
        obj = parent_graph[obj]
        generation_root[obj] = count_1
        count_1 += 1


    obj = node_2
    if generation_root[obj] != -1:
        answer_list.append(obj)
    while True: 
        if obj == ans:
            break
        obj = parent_graph[obj]
        if generation_root[obj] != -1:
            answer_list.append(obj)
            break

for i in answer_list:
    print(i)