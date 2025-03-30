def solution(common):
    last_element = common[-1]
    answer = 0
    # 등비인지, 등차인지부터 알아야 함
    isPlus = common[2] - common[1] == common[1] - common[0] # true이면 등차, false이면 등비
    
    if isPlus:
        answer = (last_element + (common[1] - common[0]))
    else:
        answer = (last_element * (common[1] // common[0]))

    return answer
