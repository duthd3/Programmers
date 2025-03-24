def solution(array, n):
    answer = 0
    min_num = 101
    # 1. 각원소와 n 의 차이가 가장 작은 원소를 찾는다.
    # 2. 여러개일 경우에 대비한다. 여러개일 경우 원래 답과 현재 답을 비교해서 더작은수가 진짜 답
    for i in array:
        if abs(i - n) < min_num:
            min_num = abs(i - n)
            answer = i
        elif abs(i - n) == min_num:
            min_num = abs(i - n)
            answer = min(answer, i)
    return answer
