def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# print(fibo(500)) # -> 렉걸림..

def fibo1(n):

    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]


memo = [0] * 501
memo[0] = 0
memo[1] = 1
print(fibo1(500)) # 0.2초정도 걸림