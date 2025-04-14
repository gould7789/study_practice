
# def sum(input1, input2, input3):
#     return input1 + input2 + input3

# print(sum(1, 2, 3))
# print(sum(5, 5, 6))

# msg = "hello"

# def prt_msg(arg_msg):
#     msg = "안녕하세요"
#     print(arg_msg + msg)
    
# prt_msg(msg)

# print(msg)


# 지역변수
    # 함수 내에서 선언된 변수
    # 생명주기 B -> 함수 호출 후 변수 선언 시
    # 생명주기 D -> 함수가 종료되면
    # 접근범위 S -> 변수 선언 후
    # 접근범위 F -> 함수 종료 전까지

# 전역변수
    # 함수 밖에서 선언된 변수  
    # 생명주기 B -> 변수 선언 시
    # 생명주기 D -> 프로그램 종료 시
    # 접근범위 S -> 변수 선언 후 
    # 접근범위 F -> 프로그램 종료 전까지
    

# msg1 = "님 안녕하세요."
# msg2 = " 반갑습니다."

# # scope chaining (스코프 체이닝)
#     # 함수 안에서 변수를 get 할 때
#     # 함수 안에서 전역변수 호출 시, 인터프리터는 먼저 함수 영역에서 변수 탐색
#     # 없으면 전역변수 영역으로 이동
#     # 없으면 내장변수 영역으로 이동 -> 그래도 없으면 에러!

# def prt_something(arg_name): # 함수 안에서 전역 변수 사용
#     global msg1, msg2 # global이 없어도 출력 가능
#     print(arg_name + msg1 + msg2)
    
# prt_something("홍길동")
# print(__name__) # 파이썬 내부에서 지정 된 변수(내장변수). __로 시작


bar = 3

def test():
    # 전역 변수 bar의 값을 1 증가 하고 싶음
    global bar
    bar = 4
    
test()
print(bar) # 4