def solution(dartResult):
    answer = 0
    score = ""
    result = []
    bonus = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    # 3번, 각 게임마다 0~10점 
    # 점수 보너스 [옵션]
    # S **1, D **2 T**3
    print(dartResult.split())
    
    for i in dartResult:
        if i.isdigit():
            score += i
            
        elif i in bonus:
            result.append(int(score)**bonus[i])
            score = ""
        elif i == "#":
            result[-1] *= -1
        elif i == "*":
            result[-1] *= 2
            if len(result) >= 2:
                result[-2] *= 2
    
    return sum(result)
