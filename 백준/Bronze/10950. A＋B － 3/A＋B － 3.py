x = int(input()) # 테스트 케이스 개수

input_a = []
input_b = []

for i in range(1,x+1):
    a, b = map(int, input().split(" "))
    input_a.append(a)
    input_b.append(b)

for i in range(0,x):
    print(f"{input_a[i] + input_b[i]}")

    #sum_input.append(a + b)