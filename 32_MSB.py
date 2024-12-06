#正の整数nの受け取り
n = int(input())

#2進数の変換
n_s = format(n, 'b')

#結果の表示
print(2**(len(n_s)-1))