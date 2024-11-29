#入力を受け付ける
n = int(input())
s = input()

#文字列sの先頭の文字と末尾の文字を辞書順で比較
if s[0] > s[n-1]:
    print('Yes')
else:
    print('No')