def solution(array, n):
    min = 1000 # 차의 최소 값
    answer = 0
    array = sorted(array)
    length = len(array)
    
    for i in range(length):
        if abs(array[i] - n) < min:
            answer = array[i]
            min = abs(array[i] -n) # min을 계속 바꿔줘야지!
    return answer
            
#array 원소중에서 n에서 array원소를 뺏을때 그 뺀 값이 가장 작은 값을 리턴
