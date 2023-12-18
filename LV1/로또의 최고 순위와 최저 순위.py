def solution(lottos, win_nums):
    # 최저 순위는 lottos에서 실제 알아볼 수 있는 것과 진짜 당첨번호 일치하는 갯수
    answer = []
    max_answer = 0
    min_answer = 0
    ranking = {6: 1, 5: 2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for i in lottos:
        for j in win_nums:
            if i == j :
                min_answer += 1
    max_answer = lottos.count(0) + min_answer
    answer.append(ranking[max_answer])
    answer.append(ranking[min_answer])
    return answer
