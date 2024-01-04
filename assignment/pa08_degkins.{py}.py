n = int(input())
# n은 edge 개수 이고 n+1 은 노드의 개수이다
node_n = n + 1
child_graph = []
parent_graph = []
#인덱스와 노드의 번호를 일치시키기위하여 sub_list를 n+2개 를 만들어준다
graph_name_list = []
for _ in range(n):
    a,b = map(str,input().split())
    if a not in graph_name_list:
        graph_name_list.append(a)
        child_graph.append([])
        parent_graph.append(-1)
    if b not in graph_name_list:
        graph_name_list.append(b)
        child_graph.append([])
        parent_graph.append(-1)
    a_index = graph_name_list.index(a)
    b_index = graph_name_list.index(b)
    child_graph[a_index].append(b)
    parent_graph[b_index] = a

ans_index = parent_graph.index(-1)
generation_root = [-1 for _ in range(len(graph_name_list))]

node_1 = input()
node_2 = input()
"""
print(graph_name_list)
print(child_graph)
print(parent_graph)
"""
node_1_index = graph_name_list.index(node_1)
node_2_index = graph_name_list.index(node_2)

count_1 = 1
obj = -1
obj_index = node_1_index
generation_root[obj_index] = 0
while True:
    if obj == graph_name_list[ans_index]:
        break
    obj = parent_graph[obj_index]
    obj_index = graph_name_list.index(obj)
    generation_root[obj_index] = count_1
    count_1 += 1

#print(generation_root)

count_2 = 0
obj = -1
obj_index = node_2_index
if generation_root[obj_index] != -1:
    print(generation_root[obj_index])
while True: 
    if obj == graph_name_list[ans_index]:
        break
    obj = parent_graph[obj_index]
    count_2 += 1
    obj_index = graph_name_list.index(obj)
    if generation_root[obj_index] != -1:
        #print(count_1 + count_2 - 1)
        print(generation_root[obj_index] + count_2)
        #print(count_2)
        break

#print(count_1)
