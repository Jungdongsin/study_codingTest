x = []

for i in range(9):
    x.append(int(input()))
#print(x)
a = max(x)
print(a)

for i in range(len(x)):
    if a == x[i]:
        print(i+1)
    else: continue