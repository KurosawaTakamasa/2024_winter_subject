#アッカーマン関数
def f(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return f(m-1, 1)
    else:
        return f(m-1, f(m, n-1))

m, n = map(int, input().split())
print(f(m, n))
