def solution(participant, completion):
    # 한명 제외 모두 완주
    par = {}
    sum_hash = 0
    for parti in participant:
        par[hash(parti)] = parti
        sum_hash += hash(parti)
        
    for com in completion:
        sum_hash -= hash(com)
 
    return par[sum_hash]
