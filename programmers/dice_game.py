"""
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

    - 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
    - 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
    - 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
    
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요
"""

def solution(a, b, c):
    answer = a + b + c  # 숫자가 모두 다를 때
    
    # 숫자가 모두 같을 때
    if a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    # 세 숫자 중 두개가 같을 때
    elif a == b or a == c or b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
        
    return answer


print(solution(2, 6, 1))    # 9
print(solution(5, 3, 3))    # 473
print(solution(4, 4, 4))    # 110592
print(solution(0, 0, 0))    # 0