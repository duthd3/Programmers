def solution(numbers):
    n_numbers = sorted(numbers)
    answer = []
    for i in range(0, len(n_numbers)-1):
        for j in range(i+1, len(n_numbers)):
            answer.append(n_numbers[i] + n_numbers[j])
    
    return sorted(list(set(answer)))
