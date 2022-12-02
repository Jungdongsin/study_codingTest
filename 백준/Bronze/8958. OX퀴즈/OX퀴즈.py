### 백준 8958_OX퀴즈

"""
< 실패 >
x = int(input()) # 테스트 케이스 개수
y = []
for i in range(x):
    y.append(input().splitlines()) # 테스트 케이스
# print(y) # input까지 성공
# print("".join(y[0]))
# a = "".join(y[0]) # join함수 : list to str
# print(a)

a = []
for i in range(len(y)):
    a.append("".join(y[i]))
# print(a)

for i in range(len(a)):
    a[i].split("X")
    """
    
x = int(input())    # 테스트 케이스 개수
for i in range(x):
    y = input() # 테스트 케이스
    z = list(y) # 입력받은 테스트 케이스를 리스트로 햔글자씩 담기
    # print(z)
    sum = 0 # 합산한 점수
    a = 1 # 시작 점수
    for i in z:
        if i == "O":
            sum += a
            a += 1
        else:
            a = 1
    print(sum)