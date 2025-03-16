def solution(my_string):
    s1 = my_string.lower()
    list_s1 = list(s1)
    answer = "".join(sorted(list_s1))
    return answer
