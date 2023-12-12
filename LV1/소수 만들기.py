from itertools import combinations

def solution(nums):
    answer = -1
    comsum = []
    result = 0
    
    #소수란 1과 자기 자신으로만 나누어 지는 수
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    com = list(combinations(nums, 3))
    # 3개 더한게 1과 자기 자신으로만 나누어 지냐?
    for i in range(len(com)):
        comsum.append(sum(com[i]))
    comsum = list(comsum)
    for i in range(len(comsum)):
        sosu = True
        
        for j in range(2, comsum[i]):
            if comsum[i] % j == 0:
                sosu = False
        if sosu:
            result += 1
  

    return result
