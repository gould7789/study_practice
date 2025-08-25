"""
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은 ["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 
나눠진 문자열을 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며, 
return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.
"""

def solution(myStr):
    answer = []
    voca = ''

    for word in myStr:
        # voca가 비어있는 상태에서(처음부터 abc가 나오는 경우)는 무시하고 진행
        if word in "abc" and len(voca) <= 0:
            continue
        # voca에 단어가 있는 상태에서 abc를 만난다면 리스트에 추가 후 voca 리셋
        elif word in "abc" and len(voca) > 0:
            answer.append(voca)
            voca = ''
        
        # abc가 아닌 문자는 voca에 추가
        if word not in "abc":
            voca += word
    
    # 반복 종료 후 남은 문자를 voca에 추가
    if voca:
        answer.append(voca)
    # 반복이 종료된 후에도 voca가 비어있다면 "EMPTY" 추가
    else:
        answer.append("EMPTY")
        
    return answer

print(solution("baconlettucetomato"	))
print(solution("abcd"))
print(solution("cabab"))