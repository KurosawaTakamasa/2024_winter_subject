#入力の受け取り
s = input()
n = int(input())

#西暦部分の取り出し
x = int(s.split('/')[0])

#日付部分の取り出し
y = s.split('/')[1]

#結果の表示
print(str(x+n)+"/"+ y)