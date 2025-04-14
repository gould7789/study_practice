# 정수 한 개를 입력 받아
# 홀수이면 "홀수 입니다."
# 짝수이면 "짝수 입니다."
# 를 출력하는 함수 작성

# 함수 정의
# def prt_even_odd(arg_input):
#     if arg_input % 2 == 0: # 입력값이 짝수이면 arg_input % 2 == 0
#         print("짝수 입니다.")
#     else:
#         print("홀수 입니다.")
#     return

def prt_even_odd(arg_input):
    msg = ""
    if arg_input % 2 == 0: # 입력값이 짝수이면 arg_input % 2 == 0
        msg = "짝수"
    else:
        msg = "홀수"
        
    print(f"{msg} 입니다.")


# 정의 된 호출
prt_even_odd(2)
prt_even_odd(3)
prt_even_odd(454243)