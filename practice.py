# 백준 8958_OX퀴즈
import sys

x = int(input()) # 테스트 케이스 개수
y = []
for i in range(x):
    y.append(input().splitlines()) # 테스트 케이스
#print(y) # input까지 성공
# print("".join(y[0]))
a = "".join(y[0]) # join함수 : list to str
print(a)
# for i in y:
    