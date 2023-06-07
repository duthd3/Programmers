from collections import deque as dq

def solution(numbers, direction):
    numbers = dq(numbers)
    if direction == "right":
        numbers.appendleft(numbers.pop())
    else:
        numbers.append(numbers.popleft())
    return list(numbers)
