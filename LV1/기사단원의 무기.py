def solution(number, limit, power):
    # 약수 개수에 해당하는 무기 구매
    answer = 0
    count = 0
    count_list = []
    for i in range(1, number + 1):
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if j < i // j:
                    count += 1
        if count > limit:
            count = power
        count_list.append(count)
        count = 0
    return sum(count_list)
