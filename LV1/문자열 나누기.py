def solution(s):
    answer = 0
    first = s[0]
    x = 1
    n = 0
    result = []
    if len(s) == 1:
        answer = 1
    for i in range(1, len(s)):
        if i == len(s) - 1:
            answer += 1
            break
        print("first:",first)
        print("s:",s[i])
        if s[i] == first: # x와 같다면
            x += 1
        else:
            n += 1
        if x == n: #x와 n의 갯수가 같다면
            print("같음")
            answer += 1
            first = s[i+1]
            print(first)
            
            x = 0
            n = 0
             
    return answer
