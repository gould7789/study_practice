# a = 10
# b = "5"
# c = 3.0
# d = True

# print(a + int(b)) # a = 10 (int 정수) + b = "5" str이지만 int로 변환 10 + 5 = 15
# print(str(a) + b) # a = 10 int 정수지만 str으로 변환 문자열 a + b 이므로 연산 없이 연속 출력 = 105
# print(c + a) # c = 3.0 float 과 a = 10 int 일 때 좀 더 용량이 큰 float형으로 환산해서 연산 = 13.0
# print(a * d) 



# # Truthy, Falsy 예제
# temp_1 = 1     # 정수형 변수
# temp_2 = -1    # 정수형 변수
# temp_3 = 0     # 정수형 변수
# temp_4 = -0    # 정수형 변수

# if temp_1:            # 1 -> Truthy 값
#     print("참")       # 출력값
# else:
#     print("거짓")

# if temp_2:            # -1 -> Truthy 값
#     print("참")       # 출력값
# else:
#     print("거짓")

# if temp_3:            # 0 -> Falsy 값
#     print("참")
# else:
#     print("거짓")     # 출력값

# if temp_4:            # -0 -> Falsy 값
#     print("참")
# else:
#     print("거짓")     # 출력값
    
    
    
# 흐름제어
# 1) 순차
# 2) 선택
# 3) 반복

# if 조건식:
#     조건식이 참 인 경우 실행되는 코드들
# else:
#     조건식이 거짓인 경우 실행된는 코드들
# 조건식이 반환 할 수 있는 건 true, false 밖에 없음


# if 4551231 > 1513215: 
#     print("참")
# else:
#     print("거짓")


# 입력값이 0이면 0입니다.
# 입력값이 0이 아니면 0이 아닙니다.
# try:
#     input_value = int(input("값을 입력하세요: "))
#     if input_value == 0:
#         print("0입니다.")
#     else:
#         print("0이 아닙니다")
# except ValueError:
#     print("숫자만 입력해주세요.")


# input_value2 = int(input("입력 값: "))

# if input_value2 > 0: # 입력 값이 양수이면 "양수" 출력
#     print("양수")
# elif input_value2 < 0: # 입력 값이 음수이면 "음수" 출력
#     print("음수")
# else: # 입력 값이 0이면 "0" 출력
#     print("0")


# 입력 값이 짝수이면 "짝수" 출력
# 입력 값이 홀수이면 "홀수" 출력
# 입력 값이 0이면 "0" 출력

# input_value3 = int(input("입력 값: "))

# if input_value3 % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")


# # 암호를 입력하세요 : "0539405442"
# input_value4 = input("입력 값: ")

# if input_value4 == "0539405442": # 암호가 일치 할 경우 "로그인 성공"
#     print("로그인 성공")
# else: # 암호가 일치 하지않을 경우 "로그인 실패"
#     print("로그인 실패")




# # 사용자로부터 문자 1개를 입력 받습니다.
# input_value5 = input("입력 값: ")
# # 그 다음, 사용자로부터 정수 1개를 입력 받습니다.
# num = int(input("반복 값: "))
# # 입력 받은 문자를 입력받은 정수만큼 반복 출력합니다.
# print(input_value5 * num)

# 실행 예)
# 문자 하나를 입력하세요 : $
# 문자를 반복 출력할 정수를 입력하세요 : 5
# 출력 결과 : $$$$$




# 정사각형의 면적을 구하시오
# 가로 또는 세로의 길이 입력: 5
# size_of_rect = int(input("변의 길이: "))
# result = size_of_rect * size_of_rect
# # 정사각형의 면적 : 5 * 5 = 25
# print(f"정사각형의 면적은 {result}입니다.")


