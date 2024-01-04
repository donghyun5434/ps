from collections import deque

max_w = int(input())
max_n = int(input())
n = int(input()) 
input_list = []
for _ in range(n):
    input_list.append(int(input()))

i = 0
count = 0
while(True):
    if i == n:
        break
    count = count + 1
    if i < n:
        queue = deque()
        queue_n = 0
        queue_w = 0
        print("새마음 새뜻")
        while(True):
            if i >= n:
                break
            if queue_n >= max_n or queue_w + input_list[i] > max_w:
                break
            queue_n = queue_n + 1
            queue_w = queue_w + input_list[i]
            queue.append(input_list[i])
            i = i + 1
        print(queue)
    while(True):
        stop_sign = 0
        print("시작",queue,i)
        if i >= n:
            break
        else:
            while(queue_n <= max_n):
                if queue_n == 0:
                    stop_sign = 1
                    print("비었음")
                    break
                if input_list[i] + queue_w > max_w:
                    print("....",queue)
                    queue.clear()
                    stop_sign = 1
                    print("clear")
                    break
                elif(input_list[i] + queue_w <= max_w):
                    save_w = queue.popleft()
                    queue_w = queue_w - save_w
                    queue_n = queue_n -1
                    queue.append(input_list[i])
                    queue_n = queue_n + 1
                    queue_w = queue_w + input_list[i]
                    print(input_list[i],"add")
                    i = i + 1
                    if i == n:
                        break
            if stop_sign == 1:
                    print("stop")
                    break

print(count)


