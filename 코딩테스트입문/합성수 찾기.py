def solution(n):
    count = 0
    answer = 0
    for i in range(1, n + 1): ## n 이하의 모든 수에 대해서
        for j in range(1, i + 1):
            if i % j == 0 :
                count += 1
        if count >= 3:
            answer += 1
        count = 0 # 하나의 수를 검사한 후 count(합성수의 약수의 개수) 초기화 
    return answer
