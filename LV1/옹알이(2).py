def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for say in can:
            if say in babbling[i] and say * 2 not in babbling[i]:
                babbling[i] = babbling[i].replace(say, "*")
        print(babbling)    
   
        if all(char == "*" for char in babbling[i]):
            answer += 1
    return answer
