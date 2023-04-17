def solution(my_string):
    new = ""
    for i in my_string:
        if i.islower():
            new += i.upper()
        else:
            new += i.lower()
    return new
