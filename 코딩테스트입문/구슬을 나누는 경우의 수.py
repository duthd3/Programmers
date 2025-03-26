def solution(balls, share):
    # 조합
    b = 1
    s = 1
    answer = 0
    for i in range(share):
        b = b * balls
        balls -= 1
        print(b)
        s = s * share
        share -= 1
    answer = b // s
    return answer
