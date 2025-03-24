def solution(my_string):
    answer = 0
    str = "0"
    for i in my_string:
        if i.isdigit():
            str += i
        else:
            answer += int(str)
            str = "0" 
    if str != "0":
        answer += int(str)
    return answer
