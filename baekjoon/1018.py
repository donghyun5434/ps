n,m = map(int,input().split())
graph = [] 
for _ in range(n):
    graph.append(list(input()))

result_l = []
for i in range(7,n):
    for j in range(7,m):
        modfi_graph = [[0 for _ in range(m)] for _ in range(n)]
        for s in range(i-7,i+1):
            for t in range(j-7,j+1):
                if s % 2 == 0 and t % 2 == 0 and graph[s][t] == 'W':
                    modfi_graph[s][t] = 1
                elif s % 2 == 1 and t % 2 == 1 and graph[s][t] == 'W':
                    modfi_graph[s][t] = 1
                elif s % 2 == 0 and t % 2 == 1 and graph[s][t] == 'B':
                    modfi_graph[s][t] = 1
                elif s % 2 == 1 and t % 2 == 0 and graph[s][t] == 'B':
                    modfi_graph[s][t] = 1
        out = 0
        for k in range(8):
            out += sum(modfi_graph[i-7+k][j-7:j+1])
        result_l.append(out)

        modfi_graph = [[0 for _ in range(m)] for _ in range(n)]
        for s in range(i-7,i+1):
            for t in range(j-7,j+1):
                if s % 2 == 0 and t % 2 == 0 and graph[s][t] == 'B':
                    modfi_graph[s][t] = 1
                elif s % 2 == 1 and t % 2 == 1 and graph[s][t] == 'B':
                    modfi_graph[s][t] = 1
                elif s % 2 == 0 and t % 2 == 1 and graph[s][t] == 'W':
                    modfi_graph[s][t] = 1
                elif s % 2 == 1 and t % 2 == 0 and graph[s][t] == 'W':
                    modfi_graph[s][t] = 1
        out = 0
        for k in range(8):
            out += sum(modfi_graph[i-7+k][j-7:j+1])
        result_l.append(out)

print(min(result_l))