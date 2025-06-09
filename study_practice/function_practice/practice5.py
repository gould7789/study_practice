# def 함수 (positional argument, variant arguments, keyword argument, variant keyword arguments)
def foo(**kwargs):     # 가변 키워드 인자 : **kwargs
    pass

foo(a = 2, b = 3, c = 4)
foo(d = 70, e = 80, f = 90, g = 100)

# hashfunction
# 랜덤한 해시값을 출력
print(hash("123"))
print(hash("hello world"))
print(hash("hello 541561"))
print(hash("555"))