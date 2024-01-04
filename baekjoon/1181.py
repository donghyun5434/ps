n = int(input())
l = []
for _ in range(n):
    l.append(input())

new_l = list(set(l)) 
new_l.sort()
new_l.sort(key=len)


for i in new_l:
    print(i)