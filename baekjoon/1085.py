n = int(input())
l = []
for _ in range(n):
    l.append(input())

l.sort(key=len)

for i in l:
    print(i)