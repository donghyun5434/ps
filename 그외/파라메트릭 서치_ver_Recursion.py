import sys
sys.setrecursionlimit(100000)

"""
find_h 함수 설명 만족하는 h를 이진탐색을 통해 찾는 함수임
start는 0 디폴트이지만 end longest_cake와 동일 (애초에 어떻게 자르는게 문제인데 자르지 않는 경우면 너무 허무맹랑하지 않나)
"""
def find_h(arr,start,end):
    global target_sum_l , cake_n
    mid = (start+end)//2
    sum = 0

    for i in cake:
        if i >= mid:
            sum = sum + (i-mid)

    if sum == target_sum_l:
        return mid
    elif sum < target_sum_l:
        return find_h(arr,start,mid-1)
    elif sum > target_sum_l:
        return find_h(arr,mid+1,end)

cake_n,target_sum_l = map(int,input().split())
cake = list(map(int,input().split()))
#이진 탐색을 써야 하기 때문에 cake리스트를 정열해준다 (x) ==> H 를 이진탐색하기 때문에 cake리스트를 정렬할 필요없이 max(cake)만 구하면 된다 
#cake.sort() 불필요함 오히려 runtimeerror유발
longest_cake = max(cake)

print(find_h(cake,0,longest_cake))
"""
최적화문제 : 문제상황을 만족하는 특정변수의 최솟값 혹은 최댓값을 구하는 문제
보통의 최적화 문제 풀이 알고리즘 == 파라메트릭 서치
파라메트릭 서치란 특정 변수의 최댓값 혹은 최솟값을 구하는 문제에서 이진 탐색 알고리즘을 사용하는 알고리즘
특정 변수의 후보를 대입해서 target과의 대소비교로 이진 탐색으로 최종의 변수의 최적화 값을 찾는다
******"이진탐색을 사용한다"의 의미*******
이진탐색 구현을 떠올려본다
우선 정렬된 수열에 대하여,
후보중 가장 min & max를 상정하고 (min+max)//2 를 mid로 결정하여 변수가 mid일때 target과의 대소관계를 파악함
mid>target이면 min(start)~mid 사이에 target이 있으므로 max(end) = mid - 1 로 설정 후 다시 위의 과정을 반복한다
mid<target이면 mid~max(end)사이에 target이 있으므로 min(start) = mid + 1 로 설정 후 다시 위의 과정을 반복한다
언제까지? (정답이 있을테니까) mid값이 target과 같을 때까지
"""



