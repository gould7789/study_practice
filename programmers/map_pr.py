"""
0 이상의 두 정수가 문자열 a, b로 주어질 때, 
a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요
"""

def solution(a, b):
    num1, num2 = map(int, [a, b])
    result = str(num1 + num2)
    
    return result

print(solution("582", "734"))
print(solution("18446744073709551615", "287346502836570928366"))
print(solution("0", "0"))