# 사용자로부터 정수를 입려받아,
# 해당 정수가 양의 정수인지, 음의 정수인지,
# 아니면 0인지 판별하는 프로그램입니다.

# 사용자로부터 정수 입력 받음 (입력 값이 정수라고 가정)
inputNumber = int(input("정수 값을 입력하세요: "))

msg = "입력값은"

# 정수의 값이 양의 정수 였을 때
if inputNumber > 0:
    msg = msg + " 양수입니다."
# 정수의 값이 음의 정수 였을 때
elif inputNumber < 0:
    msg = msg + " 음수입니다."
# 정수의 값이 0일 때
else:
    msg = msg + " 0입니다."

print(msg)