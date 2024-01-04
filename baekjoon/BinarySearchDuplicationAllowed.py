def lowerbound(array, target):
  start, end = 0, len(array)
  while start < end:
    mid = (start+end)//2
    if target <= array[mid]:
      end=mid
    else:
      start=mid+1
  return start

def upperbound(array, target):
  start, end = 0, len(array)
  while start < end:
    mid = (start+end)//2
    if target < array[mid]:
      end=mid
    else:
      start=mid+1
  return start -1

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a.sort()
result = []
for i in b:
    lb = lowerbound(a,i)
    ub = upperbound(a,i)
    if lb > ub:
        result.append(0)
    else:
        result.append(ub-lb+1)

for i in result:
    print(i,end=" ")