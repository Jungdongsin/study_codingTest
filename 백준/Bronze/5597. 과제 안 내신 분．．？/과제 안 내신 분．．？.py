x = []
for i in range(1,29): # 과제를 제출한 28명의 학생들
    x.append(int(input())) # 과제 제출한 학생들의 출석번호 저장
#print(len(x))

"""
<실패>
a = [0,0]
x.extend(a) # x의 길이를 30개 맞춰줌
print(x)
print(len(x))
y = [] # 과제를 제출하지 않은 학생들

for i in range(1,31):
    if x[i-1] not in i:
        y.append(i)
    else: continue
print(y)
print(len(y))
#x[i-1]과 i가 동시에 같을 가능성이 희박함"""

y = []
for i in range(1,31):
    y.append(i)

x = set(x)
y = set(y)
a = list(y.difference(x))
print(min(a))
print(max(a))