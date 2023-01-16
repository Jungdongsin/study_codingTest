### 백준 1065 "한수"

"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 
1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
"""

def get_hansu_num(N):
    if N < 100:
        hansu = N
    else:
        hansu = 99
        for i in range(100, N+1):
            num_list = list(map(int, str(i)))
            
            if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
                hansu += 1
    return hansu

if __name__ == "__main__":
    input_num = int(input())
    
    print(get_hansu_num(input_num))