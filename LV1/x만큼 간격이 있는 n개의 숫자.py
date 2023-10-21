def solution(x, n):
    answer = []
    t = x
    for i in range(n):
        answer.append(t)
        t += x
    
    return answer
