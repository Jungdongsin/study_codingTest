import sys

x = int(input()) # 케이스의 개수
sum_num = []

for i in range(x):
    a, b = map(int, sys.stdin.readline().split(" "))
    sum_num.append(a+b)
# print(sum_num)

for i in range(1,x+1):
    print(f"Case #{i}: {sum_num[i-1]}")