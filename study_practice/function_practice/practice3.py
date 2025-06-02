a = None
print(a is None)


def foo():
    return 1, "hello", 10.0     # packing

test = foo()    # (1, "hello", 10.0)
print(test[0], test[1], test[2])

a, b, c = foo()     # unpacking
print(a, b, c)



# 함수 정의 시 매개변수 순서 규칙
def bar(a, b, c, d = 50, e = 60, f = 70, g = 80, h = 90):   # d, e, f, g, h 기본값을 가지는 매개변수
    print(a, b, c, d, e, f, g, h)
    

bar(1, 2, 3, 4, 5, h = 100)
bar(1, 2, 3, 4, 5, f = 100)
bar(1, 2, 3, h = 200)
