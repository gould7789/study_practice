"""
문자열 binomial이 매개변수로 주어집니다. 
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요
"""

def solution(binomial):
    value_list = binomial.split()   # 공백을 기준으로 요소들을 나누어 리스트로 만듦
    a, op, b = value_list           # 각 요소들을 변수에 저장
    a, b = map(int, [a, b])         # 문자형을 정수형으로 변환

    # 경우에 맞게 계산
    if op == "+":
        return int(a+b)
    elif op == "-":
        return int(a-b)
    else:
        return int(a*b)


print(solution("43 + 12"))
print(solution("0 - 7777"))
print(solution("40000 * 40000"))