def solution(cipher, code):
    a = (len(cipher) // code) -1
    str = ""
    for i in range(a+1):
        str = str + (cipher[code*(i+1)-1])
    answer = str
    return answer
