def search_ccw_and_go():
    #현재 보고있는 방향 인자 필요 + 현재 방향에서 시작하여 반시계 탐색 필요
    global dir,loc,graph,visited,total_visited
    if dir[0]-loc[0] == -1 and dir[1]-loc[1] == 0:
        # 현재 방향이 북쭉을 향할 때
        #print("start if _1")
        new_dir = [loc[0],loc[1]-1] #시선은 서쪽
        dir = new_dir[:]
        if graph[new_dir[0]][new_dir[1]] == 0 and visited[new_dir[0]][new_dir[1]] == False :
            loc = new_dir[:]
            dir = [loc[0],loc[1]-1]
            visited[loc[0]][loc[1]] = True
            total_visited += 1 
            return 1
    elif dir[0]-loc[0] == 0 and dir[1]-loc[1] == -1:
        # 현재 방향이 서쭉을 향할 때
        #print("start if_2")
        new_dir = [loc[0]+1,loc[1]] 
        dir = new_dir[:]
        if graph[new_dir[0]][new_dir[1]] == 0 and visited[new_dir[0]][new_dir[1]] == False :
            loc = new_dir[:]
            dir = [loc[0]+1,loc[1]]
            visited[loc[0]][loc[1]] = True
            total_visited += 1
            return 1
    elif dir[0]-loc[0] == 1 and dir[1]-loc[1] == 0:
        # 현재 방향이 남쭉을 향할 때
        #print("start if_3")
        new_dir = [loc[0],loc[1]+1]
        dir = new_dir[:]
        if graph[new_dir[0]][new_dir[1]] == 0 and visited[new_dir[0]][new_dir[1]] == False :
            #print("start")
            loc = new_dir[:]
            dir = [loc[0],loc[1]+1]
            visited[loc[0]][loc[1]] = True
            total_visited += 1
            return 1 
    elif dir[0]-loc[0] == 0 and dir[1]-loc[1] == 1:
        # 현재 방향이 북쭉을 향할 때
        #print("start if 4")
        new_dir = [loc[0]-1,loc[1]]
        dir = new_dir[:]
        if graph[new_dir[0]][new_dir[1]] == 0 and visited[new_dir[0]][new_dir[1]] == False :
            loc = new_dir[:]
            dir = [loc[0]-1,loc[1]]
            visited[loc[0]][loc[1]] = True
            total_visited += 1
            return 1   
    return 0

n,m = map(int,input().split())
a,b,d = map(int,input().split())

graph = []
visited = [[False for j in range(n)] for i in range(m)]
for _ in range(n):
    graph.append(list(map(int,input().split())))


loc = [a,b]
visited [a][b] = True
if d == 0:    #북
    dir = [a-1,b]
elif d == 1:  #동
    dir = [a,b+1]
elif d == 2:  #남
    dir = [a+1,b]
elif d == 3:  #서
    dir = [a,b-1]

total_break = 0
total_visited = 0
while True:
    #가장큰 반복문이 정지하기 위한 조건 : 반시계탐색 결과 움직일 곳이 없다 and 
    count = 0
    #print(visited)
    while True:
        whether_go =search_ccw_and_go()
        count += 1
        if whether_go == 1:
            #print("q")
            #print(dir)
            #print(loc)
            break
        if count == 4:   #ccw탐색 결과 사방향 모두 갈 곳이 없음
            #print("나 어떡해")
            #print(dir)
            #print(loc)
            #dir을 기준으로 뒤로 loc을 옮겨야함 그리고 dir은 기존의 loc으로 할당해주면 된다
            if dir[0]-loc[0] == -1 and dir[1]-loc[1] == 0 :
                #dir이 북쪽일 때
                if graph[loc[0]+1][loc[1]] == 0:
                    loc[0] += 1
                    dir[0] += 1
                elif graph[loc[0]+1][loc[1]] == 1:
                    total_break = 1
            elif dir[0]-loc[0] == 0 and dir[1]-loc[1] == -1 :
                #dir이 서쪽일 때
                if graph[loc[0]][loc[1]+1] == 0:
                    loc[1] += 1
                    dir[1] += 1
                elif graph[loc[0]][loc[1]+1] == 1:
                    total_break = 1
            elif dir[0]-loc[0] == 1 and dir[1]-loc[1] == 0 :
                #dir이 남쪽일 때
                if graph[loc[0]-1][loc[1]] == 0:
                    loc[0] -= 1
                    dir[0] -= 1
                elif graph[loc[0]-1][loc[1]] == 1:
                    total_break = 1
            elif dir[0]-loc[0] == 0 and dir[1]-loc[1] == 1 :
                #dir이 동쪽일때
                if graph[loc[0]][loc[1]-1] == 0:
                    loc[1] -= 1
                    dir[1] -= 1
                elif graph[loc[0]][loc[1]-1] == 1:
                    total_break = 1
            break
    if total_break == 1:
        break

print(total_visited+1)