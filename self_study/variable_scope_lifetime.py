# # 변수의 scope(접근법위)와 lifetime(생명주기)


# bar = "hello"
# print(bar)

# del bar
# print(bar)

# # scope 4 -> 6
# # lifetime 4 -> 7

# bar = "hello"

# lifetime 13 -> 프로그램 종료 시
# scope 13 -> 소스코드의 마지막 줄

# 변수의 scope 관점
# - Global variable (전역변수)
#   -> 함수 밖에서 선언된 변수
#   -> B : 변수 선언
#   -> D : 프로그램 종료 시

# - Local variable (지역변수)
#   -> 함수 내에서 선언된 변수
#   -> B : 함수를 호출 할 때
#   -> D : 함수가 종료 될 때


def getName(arg_name):
    return arg_name + "님"

def getGreeting(arg_name):
    greeting = arg_name + "안녕하세요"
    return greeting

def prtShow(arg_name):
    name = getName(arg_name)
    msg = getGreeting(name)
    print(f"name: {name} -> msg: {msg}")
    
prtShow("홍길동")





