def solution(numbers, hand):
    # hand - 왼손잡이 , 오른손잡이
    # 1 4 7은 무조건 왼손
    # 3 6 9는 무조건 오른손
    # y좌표가 같은 손의 위치를 알아야 한다.
    # 5를 눌러야 해 -> 5의 y좌표는 1이야 왼손은7에있고, 오른손은 6에있어 7의 y좌표는 2, 6의 y좌표는 1이잖아 즉, 오른손의 y좌표가1이니 오른손으로 눌러야함
    # 근데 만약 양손의 y좌표가 모두 눌러야할 y좌표와 같다? 그럼 hand로 누른다.
    answer = ''
    key = {0:(3,1), 1: (0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6: (1,2), 7:(2, 0), 8:(2,1), 9:(2,2)}
    left = (3,0)
    right = (3,2)
    l_distance = 0
    r_distance = 0
    for num in numbers:    
        if num in [1, 4, 7]:
            answer += "L"
            left = key[num]
        elif num in [3, 6, 9]:
            answer += "R"
            right = key[num]
        else: # 2 5 8 0
            for i in range(2):
                l_distance += juldae(left[i] - key[num][i])
                r_distance += juldae(right[i] - key[num][i])
            print("num = ", key[num])
            print("left: ", left)
            print("right: ", right)
            print("l_distance = ", l_distance)
            print("r_distance = ", r_distance)
            if l_distance == r_distance:
                if hand == "left":
                    answer += "L"
                    left = key[num]
                else:
                    answer += "R"
                    right = key[num]
            elif l_distance < r_distance:
                answer += "L"
                left = key[num]
            
            else:
                answer += "R"
                right = key[num]
            l_distance = 0
            r_distance = 0
                
                
            
    return answer

def juldae(k):
    if k < 0:
        return -k
    else:
        return k


