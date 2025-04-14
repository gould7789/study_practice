# 키보드로부터 숫자를 입력받아
# 짝수이면 "짝수", 홀수이면 "홀수"를
# 화면에 출력하시오.

# 키보드로부터 정수 입력
# input_value = int(input("숫자를 입력하세요:\t"))
# # 입력값 % 2 == 0 -> "짝수" 출력
# if input_value % 2 == 0:
#     print(f"{input_value}는 짝수입니다.")
# # else -> "홀수" 출력
# else:
#     print(f"{input_value}는 홀수입니다.")


# for val in range(1, 11):
#     print(f"{val % 3}, ", end="")





# 키보드로부터 두 개의 정수를 입력받아 저장 후
# 아래 메뉴를 출력하세요
# ----------------------------
# 1. 더하기
# 2. 빼기
# 3. 곱하기
# 4. 나눗셈 if 
# -----------------------------

# 메뉴 출력 후다시 키보드로부터 메뉴 선택값을 입력 받고,
# 선택한 연산자에 따라 이전 입력 받은 두 수의 연산값을 출력하시오



# # 사용자에게 두 개의 정수를 입력받음
# input_value1 = int(input("첫 번째 숫자를 입력해주세요: "))
# input_value2 = int(input("두 번째 숫자를 입력해주세요: "))

# # 연산 메뉴 출력
# menu = """------------------
# 1. 더하기
# 2. 빼기
# 3. 곱하기
# 4. 나누기
# ------------------"""
# print(menu)

# # Test - 1
# # print(f"{input_value1} + {input_value2} = {input_value1 + input_value2}")

# # 사용자에게 메뉴 선택 입력
# sel_menu = int(input("메뉴를 선택하세요: "))

# # 선택된 메뉴에 따른 연산 실시
# try:
#     result = 0
#     if sel_menu == 1:
#         result = input_value1 + input_value2
#     elif sel_menu == 2:
#         result = input_value1 - input_value2
#     elif sel_menu == 3:
#         result = input_value1 * input_value2
#     elif sel_menu == 4:
#         result = input_value1 / input_value2
#     else:
#         result = "잘못된 입력 입니다."

#     # 연산자에 따른 연산값 출력
#     print(result)
# except ValueError:
#     print("숫자만 넣어주세요.")




# 키보드로부터 두 개의 정수를 입력받아 저장 후
try:
    input_value1 = int(input("첫 번째 숫자를 입력해주세요: "))
    input_value2 = int(input("두 번째 숫자를 입력해주세요: "))
except ValueError:
    print("숫자만 입력해주세요.")
# 아래 메뉴를 출력하세요
print("""----------------------------
1. 더하기
2. 빼기
3. 곱하기
4. 나눗셈 
-----------------------------""")

# 연산자 딕셔너리
operation = {
    1 : ("+", lambda a, b : a + b),
    2 : ("-", lambda a, b : a - b),
    3 : ("*", lambda a, b : a * b),
    4 : ("%", lambda a, b : a / b if b != 0 else "0으로는 나눌 수 없습니다.")
}

# 메뉴 출력 후다시 키보드로부터 메뉴 선택값을 입력 받고,
# 선택한 연산자에 따라 이전 입력 받은 두 수의 연산값을 출력하시오
try:
    choice = int(input("1~4 중에 선택해주세요: "))
    
    if choice in operation:
        symbol, func = operation[choice]
        result = func(input_value1, input_value2)
        
        print(f"{input_value1} {symbol} {input_value2} = {result}")
    else:
        print("1~4 중에 입력해주세요.")
except ValueError:
    print("숫자만 입력해주세요.")
