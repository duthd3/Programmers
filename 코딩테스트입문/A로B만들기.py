def solution(before, after):
    s_before = sorted(before)
    s_after = sorted(after)
    if s_before == s_after:
        answer = 1
    else:
        answer = 0
    
    return answer
