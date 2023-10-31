def solution(left, right):
    even = 0 # 약수의 개수가 짝수
    odd = 0 # 약수의 개수가 홀수
    # 약수 담을 변수
    answer = 0
    for i in range(left, right + 1):
        num = 0
        for j in range(1, i+1):
            if i % j == 0:
                num += 1
                
        if num % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
