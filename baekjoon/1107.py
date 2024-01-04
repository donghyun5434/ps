import sys
input = sys.stdin.readline

def possible(obj_list):
    global obj_n
    set_list = list(set(obj_list))
    set_list.sort()                         #set_list는 obj에 포함된 숫자 종류를 오름차순으로 정렬한 리스트임
    count = 0
    """
    for i in range(len(set_list)):          #ava_num(index와 value를 동기화 시킨 리스트)에서 obj포함 숫자있는지 확인 
        if set_list[i] in ava_num:
            count += 1
            d[set_list[i]] = 'on'
    """
    
    #print(ava_num)
    #print(count)
    for i in ava_num:
        if i != 'X':
            comp_ava_num.append(i)

    if count == len(set_list):
        return True
    else:
        return False

def find(n):
    global out,obj_n,obj,ava_min,ava_max

    while d[obj_list[n]] == 'on':
        out = out*10 + obj_list[n]
        n += 1
    
    big_out = out
    i = obj_list[n]
    while True:
        if ava_num[i] != 'X':
            big_out = big_out*10 + ava_num[i]
            while len(str(big_out)) < obj_n:
                big_out = big_out*10 + ava_min
            gap.append((big_out,abs(obj-big_out)))
            break
        if i >= 9:
            if n == 0:
                big_out = 10**(obj_n)
                gap.append((big_out,abs(obj-big_out)))
            break
        i += 1
    
    small_out = out
    i = obj_list[n]
    while True:
        if ava_num[i] != 'X':
            small_out = small_out*10 + ava_num[i]
            while len(str(small_out)) < obj_n:
                small_out = small_out*10 + ava_max 
            gap.append((small_out,abs(obj-small_out)))
            break
        if i <= 0:
            if n == 0:
                small_out = 10**(obj_n-1)-1
                gap.append((small_out,abs(obj-small_out)))
            break
        i -= 1
    
    




obj = int(input())
n = int(input())
obj_n = len(str(obj)) #obj자릿수
obj_list = list(map(int,str(obj))) #obj 접근을 위해 list에 넣은 것 obj_list = [3,4,5]
ava_num = [i for i in range(10)]  #index와 동기화한리스트 삭제된 val = 'X' obj와 동일 
comp_ava_num = []
ava_min = -1
ava_max = -1

if n != 0:
    l = list(map(int,input().split())) #l은 사용못하는 번호 리스트
    out = 0
    d = {}
    gap = []

    for i in range(10):
        d[i] = "off"

    for i in l:
        ava_num[i] = "X"



    if obj == 100:
        print(0)
    elif possible(obj_list) == True:
        #obj와 동일하게 만들수 있는경우
        print(obj_n)
    else:#번호입력으로 obj를 만들 수 없을 경우
        #재귀를 통한 찾기
        if len(comp_ava_num) == 0:
            print(abs(obj-100))
        else:
            ava_min= comp_ava_num[0]
            ava_max= comp_ava_num[-1]
            find(0)
            gap.sort(key=lambda x:x[1])
            answer = len(str(gap[0][0])) + gap[0][1]
            #print(gap)
            print(answer)
else:
    print(obj_n)