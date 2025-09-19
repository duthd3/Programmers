def solution(a, b, n):
    # a = 2, b = 1, n = 20
    #콜라 빈병 2개 -> 콜라 1병을 주는 마트
    
    # 보유중인 빈병이 1개 또는 0개이면 콜라를 받을 수 없다.
    no_cola = n # 빈병
    real_cola = 0 # 실제 콜라
    answer = 0
    na = 0
    while no_cola >= a:
        # 새로 받은 콜라
        real_cola = (no_cola // a) * b
        # 나머지 콜라
        na = no_cola % a
        answer += real_cola
        no_cola = real_cola + na
 
    return answer
