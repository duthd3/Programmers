def solution(answers):
    answer = []
    score = [0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    #수포자1 1,2,3,4,5 반복
    #수포자2 2,1,2,3,2,4,2,5 반복
    #수포자3 3,3,1,1,2,2,4,4,5,5 반복
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            score[0] += 1
        if answers[i] == s2[i%8]:
            score[1] += 1
        if answers[i] == s3[i%10]:
            score[2] += 1
            
    for i, v in enumerate(score):
        if v == max(score):
            answer.append(i+1)
 
        
        
    return answer
