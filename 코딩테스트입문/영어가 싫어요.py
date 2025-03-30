def solution(numbers):
    answer = 0
    
    
    for idx, val in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(val, str(idx))
    answer = int(numbers)
    return answer
