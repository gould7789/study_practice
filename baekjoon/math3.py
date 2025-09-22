import math

# 가장 높이 올라가는 시간 = 꼭짓점
def top(a, b):
    return -b / (2*a)

# 바닥에 떨어지는 시간
def down(a, b, c):
    num = (b**2) - (4*a*c)
    
    # 합이 0이하일 경우
    if num < 0:
        print("실근이 존재하지 않습니다.")    
    
    return (-b + math.sqrt((b**2) - (4*a*c))) / (2*a), (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)

# 계산기
def cal(a, b, c):
    while True:
        # 메뉴
        print("""
1. 최대 높이까지 걸리는 시간
2. 바닥까지 떨어지는 시간
3. 프로그램 종료""")
        
        try:
            # 메뉴 선택
            user_input = int(input("계산식 선택: "))
            
            if 0< user_input < 4:
                # 메뉴 선택 결과
                # 각 메뉴에 따른 리턴하는 변수값이 다름
                if user_input == 1:
                    return top(a, b)
                elif user_input == 2:
                    return down(a, b, c)
                elif user_input == 3:
                    return print("종료합니다")
        except ValueError:
            print("숫자를 입력해주세요.")

        

# 방정식 수 입력
a, b, c = map(float, input().split())
print(cal(a, b, c))