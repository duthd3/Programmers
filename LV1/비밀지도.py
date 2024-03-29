def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        value = bin(a|b)[2:]
        
        if len(value) < n:
            value = "0"*(n-len(value)) + value
        value = value.replace('1','#').replace('0',' ')
        answer.append(value)
    return answer
