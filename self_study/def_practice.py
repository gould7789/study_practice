# 정수 두 개를 입력 받고
# 합계를 출력하는 함수를 정의
# def add(input1, input2):
#     sum = input1 + input2
#     return sum # return은 값을 반환한다는 의미, 함수 실행을 종료한다는 의미미

# input_value1 = int(input("숫자 1 입력: "))
# input_value2 = int(input("숫자 2 입력: "))

# result = add(input_value1, input_value2)

# print(result)

# 정수 3개를 입력 받고
# 평균을 반환하는 함수 정의

# def cal(a, b, c):
#     ave = (a + b + c) / 3
#     return ave

# input_value1 = int(input("첫 번째 숫자 입력: "))
# input_value2 = int(input("두 번째 숫자 입력: "))
# input_value3 = int(input("세 번째 숫자 입력: "))

# result = cal(input_value1, input_value2, input_value3)

# print(result)    


# def greeting(name):
    # "좋은 아침입니다, {이름}님!"
    # 문자열 반환

# def greeting(name):
#     input_name = print(f"좋은 아침입니다, {name}님!")
#     return input_name

# user_name = input("이름을 알려주세요: ")

# result = greeting(user_name)

# print(result)


def c():
    print("c 함수 호출")
    print("c 함수 종료")

def b():
    print("b 함수 호출")
    c()
    print("b 함수 종료")

def a():
    print("a 함수 호출")
    b()
    print("a 함수 종료")
    
a()