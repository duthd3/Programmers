def solution(order):
    l_order = list(str(order))
    answer = 0
    for i in l_order:
        if i == "3" or i == "6" or i == "9":
            answer += 1
    
    return answer
