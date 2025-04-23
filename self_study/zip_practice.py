a = [1, 2, 3]
b = ["철수", "영희", "민정"]

for num, name in zip(a, b):
    print(f"{name}의 점수는 {num}점 입니다.")

zipped = zip(a, b)
print(list(zipped))

data = dict(zip(a, b))
print(data)