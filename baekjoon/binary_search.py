#binary_search
def binary_search_recur(target,start_i,end_i,mid_i,arr):
    if target < arr[mid_i]:
        return binary_search_recur(target,start_i,mid_i-1,mid_i//2,arr)
    elif target > arr[mid_i]:
        return binary_search_recur(target,mid_i+1,end_i,mid_i//2,arr)
    elif target == arr[mid_i]:
        return mid_i
def binary_search_loop(target,start,end,arr):
    while True:
        mid = (start + end)//2
        if target < arr[mid]:
            end = mid-1
        elif target > arr[mid]:
            start = mid+1
        else:
            return mid


arr = [0,2,4,6,8,10,12,14,16,18]
target = 4
result = binary_search_recur(target,0,len(arr)-1,len(arr)//2,arr)
print(result)