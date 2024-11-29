#入力文字を受付け一文字ずつリストへ格納
n = [s for s in input()]

#リストnに3が含まれていれば４進数、そうでなければ不明
if '3' in n:
    print("quaternary")
else:
    print("ambiguous")