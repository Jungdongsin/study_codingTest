### 백준 4673 "셀프 넘버"

# d(n)의 생성자는 n
# d(n) = n + n//10 + n%10 
# 33 -> 33 + 3 + 3 = 39 -> 39 + 3 + 9 = 51 -> 51+ 5 + 1 = 57 => ...
# 생성자 = d(n) - 생성자의 앞자리수 - 생성자의 뒷자리수
"""
< 실패 >
def d(n):
    nn = n + (n//10) + (n%10) 
    # n + n의 첫째 자리수 + n의 둘째 자리수
    return nn
# print(d(10))

for i in range(1,10001):
    if i !=  d(i) - (i//10) - (i%10):
        print(i)
    else: continue
"""

# 함수 d(n)
def d(n):
    # 생성자 n을 이용해 d(n)을 만드는 수식
    n = n + sum( map(int, str(n)) )
    return n

# 셀프 넘버가 아닌 수들(생성자가 있는 수들)이 들어갈 집합
nonSelfNum = set()

# nonSelfNum 집합에 들어갈 수들을 찾아 넣기
for i in range(1, 10001):
    nonSelfNum.add( d(i) )

# 셀프 넘버들을 출력하기
for j in range(1, 10001):
    if j not in nonSelfNum:
        print(j)