#文字列の受け付け
s = input()

#整数部分を取り出す
a = int(s.split('+')[0])

#分子と分母を取り出す
b = int(s.split('+')[1].split('/')[0])
c = int(s.split('+')[1].split('/')[1])

#結果の表示
print(str(b+a*c) + '/' + str(c))

