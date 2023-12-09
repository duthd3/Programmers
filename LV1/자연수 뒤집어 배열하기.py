def solution(n):
    answer = []
    n = str(n)
    answer = n[::-1]
    answer = list(map(int, n[::-1]))
    return answer
