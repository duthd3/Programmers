from collections import defaultdict

def solution(s):
    char = defaultdict(int)
    length = len(s)
    answer = ""
    
    for text in s:
        char[text] += 1
    for i in s:
        if char[i] == 1:
            answer = answer + i
    result = "".join(sorted(answer))
    
    
    return result
