def solution(chicken):
    # 쿠폰 10장당 1마리
    # 서비스 치킨에도 쿠폰 1장
    answer = 0
    coupon = 0
    while chicken >= 1:
        coupon += chicken % 10
        chicken //= 10
        answer += chicken + coupon // 10
        coupon += (coupon // 10)
        coupon %= 10
    
    return answer
