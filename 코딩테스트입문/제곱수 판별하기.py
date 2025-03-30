import math

def solution(n):
    answer = 0
    if str(math.sqrt(n))[-1] == "0":
        answer = 1
    else:
        answer = 2
    return answer
