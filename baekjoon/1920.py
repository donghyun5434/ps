def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:#arr[mid] = target 찾았당
            return 1
    return 0



n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()

for i in b:
    print(binary_search(a,i,0,len(a)-1))