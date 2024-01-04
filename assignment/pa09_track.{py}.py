n = int(input())
track = [0 for _ in range(10001)]

for _ in range(n):
    b,w = map(int,input().split())
    for i in range(w):
        track[b+i] += 1

print(max(track))