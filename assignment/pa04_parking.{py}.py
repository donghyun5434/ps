k , n = input().split()
k = int(k)
n = int(n)

slot = [0 for i in range(k)]
k0 = k

for moving in range(0,n):

    car_id = int(input())

    if car_id > 0: 
        yes_block = k - slot.count(0)  
        if yes_block == k: 
            new_k = k * 2
            new_slot = [0 for i in range(k)]
            slot.extend(new_slot)
            slot[k] = car_id
            k = new_k
        else:                          
            slot[slot.index(0)] = car_id


    else: 
        if (-1*car_id) in slot:
            out_car_index = slot.index(-1*car_id)
            slot[out_car_index] = 0
            yes_block = k - slot.count(0)  
            if yes_block == (k//3) and k!=k0:
                new_k = k // 2
                new_slot = [0 for i in range(new_k)]
                j = 0
                for i in range(0,k):
                    if slot[i] != 0:
                        new_slot[j] = slot[i]
                        j = j +1
                k = new_k
                slot = new_slot


for i in range(0,k):
    if slot[i] != 0:
        print("{0} {1}".format(i+1,slot[i]))