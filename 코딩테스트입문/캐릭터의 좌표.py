def solution(keyinput, board):
    ver = board[1] // 2
    hor = board[0] // 2
    result = [0, 0]
    for i in keyinput:
        if i == "left":
            if result[0] > -hor:
                result[0] -= 1
        elif i == "right":
            if result[0] < hor:
                result[0] += 1
        elif i == "up":
            if result[1] < ver:
                result[1] += 1
        else:
            if result[1] > -ver:
                result[1] -= 1
    answer = result
    return answer
