import math

def cal(a, b, c):
    try:
        # 판단 기준
        sum = b**2 - (4*a*c)
        
        # 계산식
        answer =  (-b+math.sqrt(b**2-4*a*c)) // (2*a)
        answer1 = (-b-math.sqrt(b**2-4*a*c)) // (2*a)
        
        # 서로 다른 두 실근을 가짐
        if sum > 0:
            return answer, answer1
        # 한 개의 실근을 가짐
        elif sum == 0:
            return 0
    
    # 그 외의 상황(허근)은 식에 적용이 안 되니 예외 처리
    except ZeroDivisionError:
        return "허근"
    except ValueError:
        return "허근"
    
print(cal(1, -4, 3))
print(cal(-1, 4, -3))
print(cal(1, 8, 12))
print(cal(1, -2, 1))
print(cal(2, 0, 0))
print(cal(1, -2, 2))