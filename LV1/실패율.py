def solution(N, stages):
    answer = []
    
    faillist = {}
    people = len(stages)
    for i in range(1, N+1):
        if people != 0 :
            faillist[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            faillist[i] = 0
    
    return sorted(faillist, key = lambda i: faillist[i],  reverse = True)
