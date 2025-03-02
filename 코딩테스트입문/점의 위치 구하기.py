def solution(dot):
    # dot[0]은 x, dot[1]은 y
    # x, y > 0 => 1사분면
    # x > 0, y < 0 => 4사분면
    # x < 0, y > 0 => 2사분면
    # x, y < 0 => 3사분면
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    else:
        answer = 3
    return answer
