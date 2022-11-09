"""x, y = map(int, input().split(" "))
# x시 y분 : 현재 시각
z = int(input())
# z분 : 요리 시간

hour = (x+((y+z)//60))
if hour >= 24:
    x = ((y+z)//60)-1

else: x = hour
    
minute = (y+z)%60

print(x, minute)"""

'''
minute = []
for i in range(0,17): #16*60=960
    if (y+z >= i*60) and (y+z < (i+1)*60):
        minute.append(x+i, y+z-(i*60))
    elif (y+z) >= (i+1)*60:
        # input이 180분이면, 180 >= 120
        minute.append(x +((y+z)//60), ((y+z)%60))
    else: # y+z < i*60
        minute.append(x, y+z-(i*60))
print(minute[0])
''' 
"""if x+((y+z)//60) > 23:
    x = (y+z)//60 """

H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)