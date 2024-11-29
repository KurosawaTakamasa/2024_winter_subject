#入力の受け付け
a, b, n = map(int, input().split())

#現在地を格納する変数
c = 0

#移動の計算
for _ in range(n):
    c = a*c + b

#結果の出力
print(c)