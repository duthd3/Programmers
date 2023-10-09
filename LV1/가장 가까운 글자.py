def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(-1)
        
        for j in range(i):
            if s[j] == s[i]:
                 answer[i] = i-j
    return answer
