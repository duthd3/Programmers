def solution(players, callings):
    # 이름을 부르면 추월
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for i in callings:
        idx = result[i] # 현재 호명된 선수의 등수
        result[i] -= 1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    answer = players
    return answer
