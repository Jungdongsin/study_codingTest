chess_origin = [1,1,2,2,2,8] # 원래 피스 갯수
x = list(map(int, input().split()))
for i in range(6):
    print(chess_origin[i] - x[i], end=" ")