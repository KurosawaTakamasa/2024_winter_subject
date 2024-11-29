#ボールの個数
n = int(input())

#隣り合うことがないので１個おきに取り出すとき最大
result = n//2

#nの偶奇によって結果が変わる
if n%2 == 0:
    print(result)
else:
    print(result+1)