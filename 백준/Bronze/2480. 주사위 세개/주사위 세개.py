# 같은 눈 3개
# 10,000원+(같은 눈)×1,000원

# 같은 눈 2개
# 1,000원+(같은 눈)×100원

# 모두 다른 눈
# (그 중 가장 큰 눈)×100원

x, y, z = map(int, input().split(" "))

a = [x, y, z]


if x == y == z :    # 같은 눈 3개
    print(10000 + (x * 1000))
elif (x == y):    # 같은 눈 2개
    print(1000 + (x*100))
elif (y == z):    # 같은 눈 2개
    print(1000 + (y*100))
elif (x == z):    # 같은 눈 2개
    print(1000 + (z*100))
else: # 모두 다를 떄
    print(max(a) * 100)