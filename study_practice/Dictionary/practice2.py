bar = {"std1" : 10, "std2" : 20, "std3" : 30}

# append
bar[0] = 20

# update
bar["std2"] = 100

# read
print(bar.get("std4", False))

# 딕셔너리의 전체 키값을 출력하는 함수
keys = bar.keys()

# 키값이 딕셔너리에 있는지 확인
print("True") if "std1" in keys else print("False")

# create
print(bar.setdefault("std4", 200))  # std4 생성
print(bar.setdefault("std1", 100))  # 기존값을 반환
print(bar)

# 삭제하고 싶을 때는 del 사용
print(bar.pop("std4", False))
print(bar)