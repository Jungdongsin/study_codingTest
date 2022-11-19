x = int(input()) # 마지막에 비교할 원본(기존 입력값)
num = x # num: 계속 변경되어 나갈 수
cnt = 0 # cnt : 사이클 횟수

while True: # input = 68
    a = num//10 # 나누기 후 몫, 앞 숫자(6)
    b = num % 10 # 나누기 후 나머지, 뒷 숫자(8)
    c = (a+b)%10 # 앞 뒤 숫자 더한 숫자의 나누기 후 나머지(a+b 결과값의 뒤숫자)(6+8=14의 4)
    num = (b*10) + c # 80+4=84
    
    cnt += 1
    if (num == x):
        break
print(cnt)