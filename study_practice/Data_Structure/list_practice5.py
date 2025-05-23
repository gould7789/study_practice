bar = [3, 4, 5]
foo = [6, 7, 8]

bar += foo

print(bar)
print(foo)


# 리스트의 곱하기

bar = [0, 0, 0, 0, 0]

foo = [1, 3, 5] * 5
print(foo)

# 리스트의 비교 연산자

bar = [1, 2, 3]
foo = [1, 3, 2]

print(bar == foo)

# identity 연산자

bar = [1, 2, 3]
foo = bar

print(bar == foo)
print(bar is foo)
print(bar is not foo)


# 멤버십 연산자

bar = [1, 20, 5, 100, 200]

print(100 in bar)
print(100 not in bar)

for val in bar:
    if val == 100:
        print("100")
        
# 비교 연산자

bar = [1, 2, 3, 4, 5]
foo = [1, 3]

print(bar > foo)    # 사전 형식으로 비교 / 인덱스 위치상 bar의 2보다 foo의 3이 더 크기 때문에 false