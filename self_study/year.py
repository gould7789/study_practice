# 현재 연도를 입력받는다.
current_year = int(input("현재 연도를 입력하세요: "))

# 사용자의 태어난 연도를 입력받는다.
birth_year = int(input("태어난 연도를 입력하세요: "))

# 현재 연도에서 태어난 연도를 뺀다.
age = current_year - birth_year

# 나이를 출력한다.
print("당신의 나이는", age, "입니다.")