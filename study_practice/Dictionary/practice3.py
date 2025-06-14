# iteration(순회)
bar = {"a" : 10, "b" : 20, "c" : 30}

def prt(**kwargs):
    for key in kwargs.keys():
        print(f"Key: {key}")

prt(**bar)

# 순회를 할 때 키값만 출력
for item in bar:
    print(item)
# or
for key in bar.keys():
    print(f"Key: {key}")


# 순회하면서 밸류값만 출력하고 싶을 때는 valuses 함수 사용
for item in bar.values():
    print(f"Item: {item}")


# 순회하면서 키값과 밸류값을 같이 출력하고 싶을 때는 items 함수 사용
for key, item in bar.items():
    print(f"Key: {key}, Item: {item}")