bar = [1, 2, 3]
foo = (4, 5, 6)

# 상수가 []로 패킹돼있으면 list
print(bar, type(bar), bar[1])

# 상수가 ()로 패킹돼있으면 tuple
print(foo, type(foo), foo[1])


def bar(*args):
    print(args[0])
    print(args)

# [2, 4, 6, 8, 10]
arg_1 = [val for val in range(2, 11, 2)]

# [1, 3, 5, 7, 9]
arg_2 = [val for val in range(1, 11 , 2)]

bar(*arg_1)
bar(*arg_2)


# 변수의 동작 모드

bar = [5, 6, 7]
foo = bar

# 언패킹이 일어나려면 좌항이 멀티플 어싸이먼트가 돼야함
a, b, c = bar
sol, *pos = bar

print(foo)
print(sol, pos)