# [1, 2, 3, 4, 5]
bar = [val for val in range(1, 6)]

# 리스트의 값이 각 변수에 맞게 선언
a, b, c, d, e = bar
print(a, b, c, d, e)

list = [val for val in range(1, 6)]

# * -> collection - list
# 변수 앞에 *을 입력하면 순서대로 변수 지정 후 남은 엘리멘트를 리스트로 팩킹해서 변수에 지정

i, *v = list

i, *v, w = list

i, v, *w = list
print(i, v, w)

# assigment operator
sol = 8

# multiple assigment operator
foo, pos, kin = 2, 3, 4

print(foo, pos, kin)


# zip 함수
foo = [1, 2, 3]
pos = [4, 5, 6]

for x, y in zip(foo, pos):
    print(f"{x}, {y}")
    
