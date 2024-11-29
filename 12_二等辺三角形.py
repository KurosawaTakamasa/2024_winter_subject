#3辺の長さ
a, b, c = map(int, input().split())

#正三角形を除外
if a==b and b==c and c==a:
    print('No')
#二等辺三角形であるかを判定
elif a==b or b==c or c==a:
    print('Yes')
#それ以外
else:
    print('No')