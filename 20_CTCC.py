#cとtの文字数をカウントする変数
count_c = 0
count_t = 0

#入力の受け付けと文字のカウント
for _ in range(4):
    if (s:=input()) == 'C':
        count_c += 1
    elif s == 'T':
        count_t += 1

#結果の表示
print('Y' if count_c==3 and count_t==1 else 'N')