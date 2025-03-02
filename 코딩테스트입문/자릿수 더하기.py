def solution(n):
    print(list(str(n)))
    answer = 0
    for i in list(str(n)):
        answer += int(i)
    return answer
