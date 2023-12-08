def solution(n, m):
    answer = []
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0 :
            cso = i
    answer.append(cso)     
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0 :
            cde = i
            break
    answer.append(cde)
            
   
    return answer
