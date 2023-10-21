def solution(n):
    answer = 0
    na = []
    for i in range(1, n):
        if n % i == 1:
           na.append(i)
    na.sort()
    answer = na[0]
    return answer
