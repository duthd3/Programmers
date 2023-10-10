def solution(k, score):
    glory = []
    answer = []
    for i in score:
        glory.append(i)
        glory.sort(reverse=True)
        if len(glory) < k :
            answer.append(glory[-1])
        else :
            answer.append(glory[k-1])
        
 
    return answer
