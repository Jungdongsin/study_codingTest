x = list(map(int, input("").split(" ")))
A = x[0]
B = x[1]
C = x[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)