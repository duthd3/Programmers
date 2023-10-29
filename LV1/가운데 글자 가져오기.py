def solution(s):
    answer = ''
    if len(s) % 2 == 0: # s의 길이가 짝수일 때
        answer = s[len(s)//2 - 1] + s[len(s)//2]  
        print(answer)
    else: # s의 길이가 홀수일 때
        answer = s[len(s)//2]
        print(answer)
   
    return answer
