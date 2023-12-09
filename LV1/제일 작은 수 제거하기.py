def solution(arr):
    answer = []
    
    index = arr.index(min(arr))
    arr.pop(index)
    
    if len(arr) == 0 :
        return [-1]
    else :
        return arr
