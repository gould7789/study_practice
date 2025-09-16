"""
FizzBuzz 문제는 
i = 1, 2, ... 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.
    i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.
    i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.
    i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.
    i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.
FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?
"""

# 사용자가 입력한 문자열을 저장
val_list = []
# 다음 숫자 판별을 위한 정수
trans_num = None
# 최종 숫자
result_num = None

# 사용자에게 입력 받음
for _ in range(3):
    user_input = input()
    val_list.append(user_input)

# 문자열을 순회하면서 정수 타입으로 변환 가능한지 확인(숫자인지 확인)
for num in range(2, -1, -1):
    # 문자열이 정수일 경우 그 자리의 인덱스를 기준으로 다음에 올 정수 계산
    try:
        trans_num = int(val_list[num])
        result_num = trans_num + (3-num)
        break
    # 문자형일 경우 다음 루프로 이어감
    except ValueError:
        continue

# total <- 다음 숫자로 fizzbuzz 판별
if result_num % 3 == 0 and result_num % 5 == 0:
    print("FizzBuzz")
elif result_num % 3 == 0:
    print("Fizz")
elif result_num % 5 == 0:
    print("Buzz")
else:
    print(result_num)
