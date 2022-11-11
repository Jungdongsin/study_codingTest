import sys

x = int(input()) # 케이스의 개수
num_a = []
num_b = []
sum_num = []

for i in range(x):
    a, b = map(int, sys.stdin.readline().split(" "))
    num_a.append(a)
    num_b.append(b)
    sum_num.append(a+b)
# print(sum_num)

for i in range(1,x+1):
    print(f"Case #{i}: {num_a[i-1]} + {num_b[i-1]} = {sum_num[i-1]}")