def solution(s):
    words = s.split(" ") # s 문자열을 " "을 기준으로 단어로 분리
   
    result = [] # 변환될 결과를 저장할 리스트 초기화 
    
    for word in words:
        print("word=" + word)
        new_word = '' # 변환된 단어를 저장할 변수 초기화
        for idx, alp in enumerate(word):
            if idx % 2 == 0:
                new_word += alp.upper()
            else:
                new_word += alp.lower()
        
        result.append(new_word)
        print(result)
    return " ".join(result)
