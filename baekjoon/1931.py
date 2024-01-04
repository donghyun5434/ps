n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x : (x[1],x[0]))
sel_arr = []
sel_arr.append(arr[0])
for i in range(1,len(arr)):
    if arr[i][0] >= sel_arr[len(sel_arr)-1][1]:
        sel_arr.append(arr[i])
print(len(sel_arr))
#종료시간을 기준으로 오름차순하고 같은 종료시간인 후보 중에서는 