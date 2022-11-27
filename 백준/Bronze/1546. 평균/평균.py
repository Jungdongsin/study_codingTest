# M : 자기 점수 중에 최댓값
# 계산식 : 점수 / M * 100
import sys

x = int(input()) # 시험 본 과목 개수
y = list(map(int, sys.stdin.readline().split(" "))) # 현재 성적
#print(y)

M = max(y)
#print(M) # M(자기 점수 중에 최댓값)

z = []
for i in range(x):
    z.append((y[i] / M) * 100)
#print((z))
print(sum(z)/len(z))