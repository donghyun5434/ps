n ,a = map(int,input().split())
l = [i for i in range(n+1)]
visited = [False for _ in range(n+1)]
visited[0] = True
visited[1] = True

count = 0
while True:
    if False not in visited:
        break
    start = visited.index(False)
    loop_n = n//start
    for i in range(1,loop_n+1):
        if visited[start*i] == False:
            count += 1
            visited[start*i] = True
            if count == a:
                print(l[start*i])
                break
            l[start*i] = -1
