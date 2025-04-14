# 3, 6, 9 게임 구현
for index in range(1, 60):
    value = str(index)
    flag = False
    msg = ""
    
    # 문자열 갯수 만큼 순회
    # 예) "34" -> 2번 순회, 첫 번째 "3", 두 번째 "4"
    for index_char in value:
        # 현 문자가 3, 6, 9 중에 하나일 경우 "박수" 출력
        if index_char == "3" or index_char == "6" or index_char == "9":
            msg += "박수"
            flag = True
            
    if flag: # 3, 6, 9 중에 하나
        print(msg)
    else:    # 3, 6, 9 가 아닐 경우
        print(index)    # 숫자 출력
