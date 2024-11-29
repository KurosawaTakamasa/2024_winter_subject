#入力の受け付け(スペース区切りで3つに注意)
s = input().split()

#USOが含まれているかをチェック
if 'USO' in s:
    print('Yes')
else:
    print('No')