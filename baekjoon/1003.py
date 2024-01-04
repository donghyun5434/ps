def fibo(n):
    if n == 0:
        return fibo_memo[0]
    if n == 1:
        return fibo_memo[1]
    for i in range(2,n+1):
        if fibo_memo[i] ==0:
            fibo_memo[i] = fibo_memo[i-1] + fibo_memo[i-2]
            memo_zero[i] = memo_zero[i-1] + memo_zero[i-2]
            memo_one[i] = memo_one[i-1] + memo_one[i-2]
    return


fibo_memo = [0 for _ in range(41)] #fibo(index) 값을 value로 
memo_zero = [0 for _ in range(41)] #fibo(index)를 끝까지했을때 fibo(0)이 몇개 있는지가 value로
memo_one = [0 for _ in range(41)] #fibo(index)를 끝까지했을때 fibo(1)이 몇개 있는지가 value로
input_list = []

fibo_memo[0] = 0
fibo_memo[1] = 1
memo_zero[0] = 1
memo_one[1] = 1

try_n = int(input())

for i in range(try_n):
    n = int(input())
    input_list.append(n)
    fibo(n)

for i in input_list:
    print(memo_zero[i],end=" ")
    print(memo_one[i])