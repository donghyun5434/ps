from collections import Counter
n = int(input())
l1 = list(map(int,input().split()))
m = int(input())
l2 = list(map(int,input().split()))
cl1 = Counter(l1)

for i in l2:
    if i in cl1:
        print(cl1[i],end =' ')
    else:
        print(0,end=' ')