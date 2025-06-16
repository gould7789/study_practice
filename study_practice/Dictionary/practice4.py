bar = {"a" : 1, "b" : 2, "c" : 3}

# dictionary unpacking

# 키값이 필요할 때
t, x, y = bar

# 밸류값이 필요할 때
t, x, y = bar.values()

print(t, x, y)

# 키값, 밸류값이 필요할 때
for key, value in bar.items():
    print(key, value)


# dictionary의 연산자
foo = {"b" : 2, "a" : 5, "c" : 3, "d" : 10}

# ==, != 연산자
if bar != foo:
    print("True")
else:
    print("False")

# 병합 연산자
test = bar | foo
print(test)

# dictionary의 컴프리헨션
result = {k : v for k, v in bar.items()}
print(result)

# zip : 원소가 가장 작은 객체를 기준으로 packing
pos =["a", "b", "c"]
sal = [10, 20, 30]
val = [100, 200, 300]

zip_result = zip(pos, sal, val)

for v1, v2, v3 in zip_result:
    print(v1, v2, v3)

# zip을 활용하여 리스트 두개를 딕셔너리로 만들기
dict_result = dict(zip(pos, sal))
print(dict_result)