#入力の受け付け
n = int(input())
s = input()

#母音のリスト
l = ["a", "i", "u", "e", "o"]

#カウンター変数
cnt = 0

#母音をカウントする処理
for k in s:
    if k in l:
        cnt += 1

#結果の表示
print(cnt)