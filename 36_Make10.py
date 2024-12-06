#整数a, b, c の受け取り
a, b, c = map(int, input().split())

#足して10になるか確認
if a+b == 10 or b+c == 10 or c+a == 10:
    print("Yes")
else:
    print("No")