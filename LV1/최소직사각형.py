def solution(sizes):
    answer = 0
    min_min = 1001
    min_array = []
    max_max = max(map(max,sizes))
    for i in range(len(sizes)):
        if min_min > min(sizes[i]):
            min_array.append(min(sizes[i]))
    return max_max * max(min_array)
