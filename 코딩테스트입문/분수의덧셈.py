import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    result = [0, 0]
    result[0] = numer1 * denom2 + numer2 * denom1
    result[1] = denom1 * denom2
    # 기약분수 만들기
    print(math.gcd(result[0], result[1]))
    mok = math.gcd(result[0], result[1])
    result[0] //= mok
    result[1] //= mok
    return result
