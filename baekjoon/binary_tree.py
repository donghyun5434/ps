import sys
def binary_search(target,start,end,arr):
    if start > end:
        return None
    mid = (start+end)//2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(target,start,mid-1,arr)
    else:
        return binary_search(target,mid+1,end,arr)

n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()

m = int(input())
l = list(map(int,sys.stdin.readline().rstrip().split()))

for i in l:
    if binary_search(i,0,len(arr)-1,arr) == None:
        print("no",end=" ")
    else:
        print("yes",end=" ")