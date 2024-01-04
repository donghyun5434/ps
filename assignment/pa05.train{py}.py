def dis_fun(set_max,set_min,v):         #v는 mg 또는 ip이다
    
    if set_max < v:  #v가 top보다 크거나 bottom보다 작을경우 즉 "붙을 수 있을 경우"
        distance = v - set_max  #v가 top위에서 붙을 수 있을경우 distance를 양수 처리
    elif set_min > v:
        distance = v - set_min  #v가 bot아래서 붙을 수 있을 경우 distance를 음수 처리 
    else:               #v가 setting 사이에 존재해서 "붙을 수 없을 경우"
        distance = 0      #v가 붙을 수 없다면 distance는 0 처리
    
    return distance
def finding(count,mg,re_index): #re_index는 case분류될때의 순서로 돌아갈 index 기억하는 용도   
    if count == len(list):
        max_list.append(len(setting))       
        return 
    ip = list[count]  
    set_max = max(setting)
    set_min = min(setting)
    mg_dis = dis_fun(set_max,set_min,mg) #mg이 위에 붙을 수 있으면 양수 , 밑에 붙을 수 있으면 음수, 못붙으면 0
    ip_dis = dis_fun(set_max,set_min,ip) #ip가...
    if mg_dis == 0 and ip_dis == 0:
        if re_index == -1:          
            max_list.append(len(setting))
            return
        elif re_index > 0:
            max_list.append(len(setting))
            for i in range(count-re_index):
                setting.pop(-1)
            return 
    elif mg_dis != 0 and ip_dis != 0: #2개다 붙을수 있는경우 하위 조건으로 (1)같은 뱡향 2개인지 (2)서로 다른 방향인지 확인 필요
        if (mg_dis * ip_dis) > 0: #같은뱡향
            if abs(mg_dis) > abs(ip_dis):
                setting.append(ip)
            else:
                setting.append(mg)
                mg = ip
        else: #곱이 음수일때 즉 서로 다른 뱡향일때 *****CASE분류가 필요함*******
            #mg을 먼저 append
            re_index = count
            index_mg = mg
            setting.append(mg)
            mg = ip
            count = count + 1   
            finding(count,mg,re_index)  
            #ip append
            setting.append(ip)
            mg = index_mg
            return finding(count,mg,re_index)
    else:  #1개만 붙을 수 있을경우
        if mg_dis != 0:
            setting.append(mg)
            mg = ip
        else:
            setting.append(ip)    
    count = count + 1
    return finding(count,mg,re_index)    

n = int(input())
list = []
for i in range(n):
    train = int(input())
    list.append(train)

setting = []
max_list =[]
#1st를 setting으로
setting.append(list[0])   #setting에 1st를 할당
count = 2
finding(count,list[1],-1)          #3rd부터 탐색을 시작한다
setting.clear()
#2nd를 setting으로 
setting.append(list[1])
count = 2
finding(count,list[0],-1)
print(max(max_list))