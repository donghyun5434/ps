n = int(input())
out = 1

for i in range(1,n+1):
    out = out * i

out_str = str(out)

count = 0
for i in range(len(out_str)-1,0,-1):
    if out_str[i] == 0:
        count += 1
    else:
        print(count) 
