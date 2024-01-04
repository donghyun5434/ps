#셔플 함수  shuffling(la,lb,l_sort)
def shuffling (la,lb,l):
    n = len(l)
    half_n = n//2
    shuffle_count = 0
    tmp_l = l[:]
    obj_index = [-1]*2
    if n % 2 == 0:  #짝수일때
        k = 0
        while True:
            if tmp_l == l and shuffle_count != 0:
                break
            l1 = tmp_l[:half_n]
            l2 = tmp_l[half_n:]
            for i in range(0,half_n):
                tmp_l[(2*i)] = l1[i]
                tmp_l[(2*i)+1] = l2[i]
            shuffle_count = shuffle_count + 1
            if tmp_l == la or tmp_l == lb:
                obj_index[k] = shuffle_count
                k = k +1
            #print(tmp_l,end='')
            #print(shuffle_count)
    else:   #홀수일때
        k = 0
        while True:
            if tmp_l == l and shuffle_count != 0:
                break
            l1 = tmp_l[:half_n+1]
            l2 = tmp_l[half_n+1:]
            for i in range(0,half_n):
                tmp_l[(2*i)] = l1[i]
                tmp_l[(2*i)+1] = l2[i]
            tmp_l[n-1] = l1[half_n]
            shuffle_count = shuffle_count + 1
            if tmp_l == la or tmp_l == lb:
                obj_index[k] = shuffle_count
                k = k + 1
            #print(tmp_l,end='')
            #print(shuffle_count)

    output = 0

    for i in range(0,2):
        if obj_index[i] == -1:
            output = -1
            break
        else:
            pass
    
    if output == -1:
        return -1
    else:
        distance_1 = obj_index[1] - obj_index[0]
        distance_2 = obj_index[0] + (shuffle_count - obj_index[1])
    

    if distance_1 > distance_2:
        return distance_2
    elif distance_1 < distance_2:
        return distance_1
    else:
        return distance_1


#리스트 입력받기
la = list(map(int,input().split()))
while True:
    la_ = list(map(int,input().split()))
    if la_[0] == -9:
        break
    else:
        la.extend(la_)


lb = list(map(int,input().split()))
while True:
    lb_ = list(map(int,input().split()))
    if lb_[0] == -9:
        break
    else:
        lb.extend(lb_)

#정렬리스트 만들기
l_sort = sorted(la)

final = shuffling(la,lb,l_sort)

if final == -1:
    print("NOT")
else:
    print(final)

