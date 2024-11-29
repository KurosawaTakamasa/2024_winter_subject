#入力の受け付け
a, b = map(int, input().split())

#a+bが3の倍数か否かの判定
#3項演算子を用いた書き方にしてみました
print('Yes' if (a+b)%3==0 else 'No')