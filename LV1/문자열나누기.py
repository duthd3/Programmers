def solution(s):
    answer = 0
    xcount = 0
    ncount = 0
    for i in s:
        if xcount == ncount:
            answer += 1
            k = i
        if k == i :
            xcount += 1
        else :
            ncount += 1
    return answer
