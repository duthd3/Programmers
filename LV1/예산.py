def solution(d, budget):
    answer = 0
    count = 0
    d.sort()
    for i in d :
        count += i
        if count > budget:
            return answer
        answer += 1
    return answer
