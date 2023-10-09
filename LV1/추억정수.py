def solution(name, yearning, photo):
    answer = []
    for p in photo:
        score = 0
        for pp in p :
            if pp in name:
                score += yearning[name.index(pp)]
        answer.append(score)
    return answer
