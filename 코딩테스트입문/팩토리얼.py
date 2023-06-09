def solution(n):
    fact = 1
    for i in range(1, 12):
        fact = fact * i
        if fact > n :
            return i-1
    
