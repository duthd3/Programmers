import math

def solution(n):
    answer = 0
    if math.sqrt(n) % 1 == 0 :
        answer = (int(math.sqrt(n)) + 1) ** 2
    else :
        answer = -1
          
    return answer
