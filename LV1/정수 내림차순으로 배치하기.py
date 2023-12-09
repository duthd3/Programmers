def solution(n):
    answer = 0
    n = str(n)
    n = sorted(n, reverse=True)

    answer = "".join(n)
    
    return int(answer)
