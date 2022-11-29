### 백준 4344 "평균은 넘겠지"

import sys

# x : 테스트 케이스의 개수
# y : 각 테스트 케이스 학생의 수
# z : y명의 학생의 점수

x = int(input())
#print(x)
for i in range(x):
    # y = int(input())    # 첫번쨰 테스트 케이스의 학생 수
    temp = list(map(int, sys.stdin.readline().split(" ")))
    y = temp[0] # 테스트 케이스의 학생 수
    z = temp[1:] # 각 학생의 점수
    #print(y, z)
    a = (sum(z) / y) # 각 테스트 케이스별 평균
    up_avg = []
    for j in range(y):
        if z[j] > a:
            up_avg.append(z[j])
        else: continue
    #print(f"{round((len(up_avg) / y)*100,3)}%")
    print(f"{round((len(up_avg) / y)*100,3):.3f}%")