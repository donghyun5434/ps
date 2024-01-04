tree_n,target_sum_l = map(int,input().split())
tree = list(map(int,input().split()))
longest_tree = max(tree)
"""
h에대해서 start = 0 , end =longest_cake 로 이진 탐색해야함 
어차피 자연수에 대해 이진탐색이므로 (어떤 data_structure item에 대한게 아님) 정렬필요
없음
"""
start = 0 
end = longest_tree
optimized_h = 0
while (start <= end):#이진탐색이 멈추는 순간은 start와 end가 어긋날때이므로 start <= end 일때동안은 반복문이 계속 돌아가도록 한다
    mid = (start + end)//2
    sum = 0
    for i in tree:
        if i > mid:
            sum += (i - mid)

    if sum < target_sum_l: #h가 너무긴
        end = mid - 1
    elif sum >= target_sum_l: #h가 좀 짧은
        optimized_h = mid
        start = mid + 1

print(optimized_h)