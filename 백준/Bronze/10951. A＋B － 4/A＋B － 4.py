"""
<실패>
import sys

x, y = map(int, sys.stdin.readline().split(" "))
num = []

while x>0 and y>0 and x<10 and y<10:
    num.append(x+y)
    continue

print(num)"""


#<성공>
import sys

num=[]
while 1:
    try:
        A, B = map(int, sys.stdin.readline().split(" "))
        num.append(A+B)
    except:
        break

for i in range(0, len(num)):
    print(num[i])