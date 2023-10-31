def solution(s):
    answer = True
    p_num = 0
    y_num = 0
    
    upper_s = s.upper()
    for i in upper_s:
        if i == 'P':
            p_num += 1
        elif i == 'Y':
            y_num += 1
    
    if p_num == y_num or (p_num == 0 and y_num == 0):
        answer = True
    else:
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    

    return answer
