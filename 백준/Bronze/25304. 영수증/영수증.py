# 영수증
    # 구매한 물건의 가격과 개수
    # 총 금액

x = int(input()) # 총 금액
y = int(input()) # 모든 물건 종류의 수

sum_price = []
for i in range(1,y+1):
    a, b = map(int, input().split(" ")) # a: 품목당 가격, b: 구매한 품목당 물건 개수
    sum_price.append(a * b)
# print(sum_price)
if sum(sum_price) == x:
    print("Yes")
else:
    print("No")