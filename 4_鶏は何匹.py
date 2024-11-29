#鶏舎の数
n = int(input())

#鶏の総数を格納する変数
total = 0

#i番目の鶏舎にi*2匹の鶏がいることに注意し
#合計を計算する
for i in range(1, n+1):
    total = total + i*2

#結果の出力    
print(total)