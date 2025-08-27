def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    students = [True] * n
    for j in lost:
        students[j-1] = False
        if j in reserve:
            students[j-1] = True
            reserve.remove(j)
    for r in reserve:
        if r == 1:
            # 자기 자신 먼저
            if students[r-1] == False:
                students[r-1] = True
            # 자신보다 오른쪽
            elif students[r-1+1] == False:
                students[r-1+1] = True
        elif r < n:
            # 자기 자신 먼저
            if students[r-1] == False:
                students[r-1] = True
            # 자신보다 왼쪽
            elif students[r-1-1] == False:
                students[r-1-1] = True
            # 자신보다 오른쪽
            elif students[r-1+1] == False:
                students[r-1+1] = True
        else:
            # 자신 먼저
            if students[r-1] == False:
                students[r-1] = True
            # 자신보다 왼쪽
            elif students[r-1-1] == False:
                students[r-1-1] = True
    print(students)
    for stu in students:
        if stu == True:
            answer += 1
    return answer
