def solution(polynomial):
    answer = ''
    num_value = 0
    x_value = 0
    for i in polynomial.split(" + "):
        if i.isdigit():
            num_value += int(i)
        else: 
            if i != "x":# ?x 일경우
                x_value += int(i.replace("x", "")) 
            else: # x 일경우
                x_value += 1    
    if (num_value != 0 and x_value != 0):
        if x_value != 1:
            answer = str(x_value) + "x" + " + " + str(num_value)
        else:
            answer = "x" + " + " + str(num_value)
          
    elif (x_value != 0 and num_value == 0):
        if x_value != 1:
            answer = str(x_value) + "x"
        else:
            answer = "x"
    elif (x_value == 0 and num_value != 0):
        answer = str(num_value)
        
    return answer
