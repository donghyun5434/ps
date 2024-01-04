from random import randrange

#node = int(input())
node = 4
table = [[] for _ in range(node)]
#edge = (node**2-node)//2

for i in range(node):
    for j in range(node-1):
        table[i].append(randrange(10))
    node -= 1
print(table)