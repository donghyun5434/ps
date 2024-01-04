import sys
input = sys.stdin.readline

def aft_num(i):

    return 
def bfr_num(i):

    return 
def ava_max():

    return 
def ava_min():

    return

obj = int(input())
n = int(input())
obj_n = len(str(obj))  #obj자릿수
obj_list = list(map(int,str(obj)))
ava = [i for i in range(10)]
d ={}
cmp_ava = []

for i in range(10):
    d[i] = "off"

if n == 0: #삭제되는게 하나도 없을 경우
    print(obj_n)
else: #삭제되는게 하나라도 있을경우
    l = list(map(int,input().split()))
    for i in l:
        ava[i] = 999
    count = 0
    ctg_obj = list(set(obj_list))
    for i in ctg_obj:
        if ava[i] == i:
            ava[i] = -ava[i]
            d[i] = "on"
            count += 1

    for i in ava:
        if i < 999:
            cmp_ava.append(abs(i))

    if count == len(ctg_obj): #필요한게 삭제되지않은경우
        print(obj_n)
    else: #필요한게 적어도 하나라도 삭제된경우
        
            


