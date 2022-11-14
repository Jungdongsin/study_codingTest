import sys

x = int(input())    # 입력받을 정수의 갯수
y = list(map(int, sys.stdin.readline().split(" "))) # 정수 리스트
z = int(input()) # 입력 정수
# output : z(입력 정수)와 일치한 정수의 갯수
num = 0

11
for i in range(0, x):
    if z == y[i]:
        num += 1
    else: continue
print(num)