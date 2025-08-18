"""
문자열 myString이 주어집니다. 
myString을 문자 "x"를 기준으로 나눴을 때 
나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요
"""

def solution(myString):
    # vanilla
    answer = [] # x를 기준으로 문자열 길이를 저장하는 리스트
    count = 0   # 문자열 길이 카운팅

    for x in myString:
        if x == "x":
            answer.append(count)    # 'x'를 만난다면 앞 문자열 길이를 리스트에 추가
            count = 0               # 다시 0부터 카운팅
            continue
        count += 1                  # 문자열 길이 카운팅
    
    answer.append(count)            # 마지막 문자열 길이 추가

    # spilt 사용
    answer = [len(x) for x in myString.split("x")]

    return answer

print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))