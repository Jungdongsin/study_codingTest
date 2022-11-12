import sys

sum_num = []
a = 0

while a != 1:
    x, y = map(int, sys.stdin.readline().split(" "))
    sum_num.append(x+y)
    if x == 0 and y ==0:
        break
    else:
        continue
    # if x != 0 and y != 0:
    #     sum_num.append(x + y)
    # else:
    #     break
    
del sum_num[-1] # 0 제거

for i in sum_num:
    print(i)