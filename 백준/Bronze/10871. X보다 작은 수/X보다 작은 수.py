x, y = map(int, input().split(" "))
# x는 갯수, y는 특정 정수
a = list(map(int, input().split(" ")))

num_check = []
for i in a:
    if i < y:
        num_check.append(i)
    else: continue
print(*num_check)    