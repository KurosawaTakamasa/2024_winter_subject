#n, m, kの受付け
n, m, k = map(int, input().split())

while True:
    if n - k < m:
        break
    n -= k

print(n)