from collections import deque
INF = int(1e9)

def bfs(start,weight):
    #이거는 최단 거리 구하는 거임 실제 움직임을 구현할 필요없음

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    l = len(graph)
    visited = [[False for _ in range(l)] for _ in range(l)]
    queue = deque([(start[0],start[1],0)])

    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        dis = v[2]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > (l-1) or ny < 0 or ny > (l-1):
                continue
            # 지나갈 수 없는 조건 (1)자기보다 큰 물고기
            elif weight < graph[nx][ny]:
                dis_graph[nx][ny] = INF
                continue
            # 지나가기만 하는 조건 (1)Empty, (2)같은 크기 물고기
            elif graph[nx][ny] == 0 or weight == graph[nx][ny]:
                if visited[nx][ny] == False:
                    queue.append((nx,ny,dis+1))
                    visited[nx][ny] = True
                    dis_graph[nx][ny] = INF
            # 지나가서 먹는 조건 (1)자기보다 작은 물고기 
            elif weight > graph[nx][ny]:
                if visited[nx][ny] ==False:
                    queue.append((nx,ny,dis+1))
                    visited[nx][ny] = True
                    dis_graph[nx][ny] = dis + 1



n = int(input())
graph = []
for i in range(n):
    row = list(map(int,input().split()))
    if 9 in row:
        present_x = i
        present_y = row.index(9)
    graph.append(row)

graph[present_x][present_y] = 0

#print(len(graph))

time = 0
weight = 2
eat_count = 0
while True:
    # bfs로 최단거리 테이블 작성 (찾기)
    dis_graph = [[INF for i in range(n)] for j in range(n)]
    bfs((present_x,present_y),weight)
    #print(dis_graph)
    dis = INF
    # 이제 dis테이블에서 목표물 선택 (선택/냠냠 아님)
    for i in range(n):
        for j in range(n):
            if dis_graph[i][j] < dis:
                obj_x = i
                obj_y = j
                dis = dis_graph[i][j]
    # 종료 컨디션
    if dis == INF:
        break
    # 목표물을 향하여 이동(이제 냠냠)!!! 
    if dis != INF:
        # 먹을게 적어도 하나는 있다는 말
        eat_count += 1
        if eat_count == weight:
            eat_count = 0
            weight += 1
        present_x = obj_x
        present_y = obj_y
        graph[present_x][present_y] = 0
        time += dis

print(time)

