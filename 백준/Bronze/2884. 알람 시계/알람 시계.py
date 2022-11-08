x, y = map(int, input().split())

"""
x:시, y:분
y - 45
y가 0보다 작으면 x에서 1을 뺀다
10시 10분일때 45분 전은 9시 + 10+60 - 45
"""

if (x > 0) and (y < 45):
    print(x - 1,(y+60) - 45)
elif (x == 0) and (y < 45):
    print(x + 23, (y+60) - 45)
else:
    print(x, y - 45)
