# 0, 1 두 번 반복
for count in range(2):
    print(f"{count}번째 실행")

# while은 반복 횟수를 지정해줘야 한다
count = 0
while count < 2:    # 종료 조건
    print(f"{count}번째 실행")
    count += 1      # 종료 조건을 만들기 위해 설정


# yes가 입력되기 전까지 반복되는 반복문 작성
input_msg = ""
while input_msg != "yes":
    input_msg = input("입력 값: ")
