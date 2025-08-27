def solution(keymap, targets):
    answer = []
    real_answer = []
    min_idx = 101
    for target in targets:
        for t in target:
            min_idx = 101
            print(t)
            for key in keymap:
                if t in key:
                    if key.index(t) < min_idx:
                        min_idx = key.index(t)
            if min_idx == 101:
                answer.append(0)
            else:
                answer.append(min_idx + 1)
        print(answer)
        if 0 in answer:
            real_answer.append(-1)
        else:
            real_answer.append(sum(answer))
        answer = []
    return real_answer
