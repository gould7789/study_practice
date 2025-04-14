# 길이를 입력하세요 : 2
input_value = int(input("길이를 입력하세요: "))

# 도형을 선택하세요(1. 사각형, 2. 삼각형)
choice = int(input("도형을 선택하세요. (1. 사각형, 2. 삼각형): "))
result = input_value ** 2

if choice == 1: # 만약 1번을 선택하면 정사각형의 면적을 출력
    print(result)
elif choice == 2: # 2번을 선택하면 정삼각형의 면적을 출력
    print(result / 2)
else: # 1, 2번 이외에 값이 입력될 경우 "잘못된 입력 입니다."
    print("잘못된 입력 입니다.")

