
from io import StringIO

def return_print(*message):
    io = StringIO()
    print(*message, file=io, end="")
    """
   *message와 같은 용법은 위치 기반 가변 인수를 참고
    중간의 print 함수에서 end=""로 둔 이유는 
    그냥 print는 기본적으로 줄바꿈을 포함하기 때문에 그것을 제외하기 위함이다
    """
    return io.getvalue()

x = int(input())
a=[] # 10보다 미만

if x < 10: 
    a.append(return_print(f"0,{x}")) # 두자리로 만들기
    #print(a)
else:
    x
    #print(x)

print(a.split(""))

