def solution(t, p):
    result = 0
    p_len = len(p)
    
    
    for i in range(len(t) - (p_len-1)):
        a_string = t[i:p_len + i]
        if int(a_string) <= int(p) :
            result += 1
    
    return result
