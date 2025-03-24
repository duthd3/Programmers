def solution(emergency):
    answer = []
    tmp = sorted(emergency, reverse = True) # 각 원소의 순위를 알기 위해서
    print(tmp)
    for i in emergency:
        answer.append(tmp.index(i) + 1)
    return answer
