import math
def solution(n):
    answer = [True for i in range(0, n+1)]
    
    result = []
    
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if answer[i] == True :
            j = 2
            while i * j <= n:
                answer[i*j] = False
                j += 1
    for i in range(2, n+1):
        if answer[i] == True:
            result.append(i)
            
    return len(result)
