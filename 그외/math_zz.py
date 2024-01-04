



z = [1,3,5,9,11,13]
out = []

for i in range(6):
    for j in range(6):
        non_mod = z[i]**(j+1)
        mod = non_mod % 14
        out.append(mod)
    out.append("ppp")

print(out)