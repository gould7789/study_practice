def bar(value1, value2):    # parameter(매개 변수) -> value1, value2
    sum = value1 + value2
    avg = sum / 2
    
    return sum, avg

value = bar(1, 3)           # 함수 호출
print(value[0], value[1])

value_sum, value_avg = value
print(value_sum, value_avg)


def foo(a, b, c, d = 10, e = 20, f = 30, g = 100, h = 1000):     # parameter(매개 변수) -> a, b, c, d, e
    print(a, b, c, d, e)
    
foo(1, 2, 3)
foo(10, 20, 30)
foo(20, 10, 30, g = 200)