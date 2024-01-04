#import sys

def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return "yes"
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"

#n = int(sys.stdin.readline().rstrip())
n = int(input())
#store = list(map(int,sys.stdin.readline().rstrip().split()))
store = list(map(int,input().split()))

#m = int(sys.stdin.readline().rstrip())
m = int(input())
#hope = list(map(int,sys.stdin.readline().rstrip().split()))
hope = list(map(int,input().split()))

store.sort()

for i in hope:
    print(binary_search(store,i,0,n-1),end=" ")
