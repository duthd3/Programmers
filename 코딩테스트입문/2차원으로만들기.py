def solution(num_list, n):
    count = len(num_list) // n
    answer = []
    for (i) in range(0, count):
        print(num_list[i*n :(i*n)+n])
        answer.append(num_list[i*n : (i*n) + n])
    return answer
