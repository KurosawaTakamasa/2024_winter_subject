#入力を受け付け
n = int(input())

#nの偶奇によって結果が変わることに注意
if n < 0:
    print(0)
elif n%2==0:
    print(n//2)
else:
    print(n//2 + 1)