def solution(a, b):
    answer = 0
    if a < b :
        for i in range(a, b):
            answer += i 
        answer += b
    elif a > b :
        for i in range(b, a):
            answer += i
        answer+= a
    else :
        answer = a
    return answer
