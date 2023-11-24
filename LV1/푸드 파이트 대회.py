def solution(food):
    answer = ''
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            answer += str(i)
    print(answer)
    r_answer = answer[::-1]
    return answer + '0' + r_answer
