# 일급 시민 조건
# 1. 값을 변수에 저장
# 2. 함수에 매개변수로 전달
# 3. 함수의 반환 값

bar = lambda msg : print(msg)
bar("hello")

def bar(msg):
    print(msg)

# foo = bar -> 값을 변수에 저장 할 수 있다
foo = bar
foo("hello")

# 함수의 매개변수로 전달 가능
def foo(my_func, msg):
    my_func(msg)
    
    return my_func

# 반환값으로 사용 가능    
kin = foo(bar, "hello")

kin("hi")