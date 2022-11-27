x = []
for i in range(10):
    x.append(int(input()))
#print(x) # 10개

a = []
for i in range(len(x)):
    a.append(x[i]%42)
    #print(x[i]%42)
a = set(a)
print(len(a))

