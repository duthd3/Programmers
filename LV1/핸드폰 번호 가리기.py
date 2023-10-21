def solution(phone_number):
    phone_number = list(phone_number)
    alen = len(phone_number) - 4
    for i in range(alen):
        phone_number[i] = "*"
        
   
    answer = ''.join(phone_number)
    
    return answer
