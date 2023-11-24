def solution(k, m, score):
    answer = 0
    sort_score = sorted(score, reverse=True)
    num = len(score) // m
    
    
    for i in range(num):
        # 0~2 3~5 6~8 9~11
        # 0~3 4~7
        s = sort_score[i*m: (i*m)+(m)]
        
        answer += min(s)*m
   
    return answer
