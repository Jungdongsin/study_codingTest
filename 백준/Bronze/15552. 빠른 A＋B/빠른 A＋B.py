import sys

x = int(input())
n = []

for i in range(1,x+1):
    a, b = map(int, sys.stdin.readline().split())
    n.append(a + b)

for i in n:
    print(i)