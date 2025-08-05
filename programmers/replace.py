"""
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, 
my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
"""

def solution(my_string, alp):
    
    # replace 함수
    # 문자열에서 특정 문자를 다른 문자로 바꾸는 함수
    # 새로운 문자열을 반환하기 때문에 변수로 저장 필수
    # 문자열.replace(바꾸는 문자, 새 문자, 바꾸는 횟수[선택])
    answer = my_string.replace(alp, alp.upper())
    return answer

print(solution("programmers", "p")) # Programmers
print(solution("lowercase", "x"))   # lowercase