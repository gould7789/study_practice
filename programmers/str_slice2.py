"""
문자열 myString과 pat가 주어집니다. 
myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요
"""

def solution(myString, pat):
    # myString을 뒤에서 부터 순회하며 pat의 첫번째 인덱스와 일치하면 그 인덱스까지 슬라이싱
    for idx in range(len(myString)-1, 0, -1):
        if myString[idx] == pat[-1]:
            return myString[:idx+1]

    # rfind 함수 사용 버전
    # rfind는 뒤부터 순회하며 해당 문자열을 찾아내고 인덱스를 출력
    return myString[0:myString.rfine(pat)] + pat

print(solution("AbCdEFG", "dE"))
print(solution("AAAAaaaa", "a"))