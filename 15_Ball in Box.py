#幅h, 奥行d, 高さh, 半径r
h, d, h, r = map(int, input().split())

#直径を計算する
l = 2*r

#幅、奥行、高さが直径以上の場合は入る
if h>=l and d>=l and h>=l:
    print('Yes')
else:
    print('No')