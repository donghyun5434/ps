
out_old_m = []
out_old_f = []
out_adult_m = []
out_adult_f = []
out_child = []

n = int(input())

for i in range(n):
    id, age, sex= map(str,input().split())
    id = int(id)
    age = int(age)

    if age <= 15:
        age_generation = "Child"
    elif age >= 61:
        age_generation = "Old"
    else:
        age_generation = "Adult"

    if age_generation == "Old":
        if sex == "M":
            out_old_m.append(id)
        elif sex == "F":
            out_old_f.append(id)
    elif age_generation == "Adult":
        if sex == "F":
            out_adult_f.append(id)
        elif sex == "M":
            out_adult_m.append(id)
    elif age_generation == "Child":
        out_child.append(id)


for i in range(len(out_old_m)):
    print(out_old_m[i])
for i in range(len(out_old_f)):
    print(out_old_f[i])
for i in range(len(out_child)):
    print(out_child[i])
for i in range(len(out_adult_f)):
    print(out_adult_f[i])
for i in range(len(out_adult_m)):
    print(out_adult_m[i])