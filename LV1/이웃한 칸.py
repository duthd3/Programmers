def solution(board, h, w):
    answer = 0
    # h, w
    # h-1, h+1, w-1, w+1 만확인하면 되는거아냐?
    if h - 1 >= 0:
        print(board[h-1][w])
        if board[h][w] == board[h-1][w]:
            answer += 1
    if h + 1 < len(board):
        print(board[h+1][w])
        if board[h][w] == board[h+1][w]:
            answer += 1
    if w - 1 >= 0:
        print(board[h][w-1])
        if board[h][w] == board[h][w-1]:
            answer += 1
    if w + 1 < len(board):
        print(board[h][w+1])
        if board[h][w] == board[h][w+1]:
            answer += 1
    return answer
