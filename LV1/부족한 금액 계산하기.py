def solution(price, money, count):
    # price : 원래요금
    # total: 필요한 총 요금
    total = 0
    plus = price
    answer = 0
    
    for i in range(count):
        total += plus
        plus += price
    
 
    answer = total - money
    if answer < 0 :
        answer = 0
    
    return answer
