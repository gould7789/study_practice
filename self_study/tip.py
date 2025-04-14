# 팁 계산기 프로그램
def cal(a, b, c):
    if c == 0:  # 0명으로 나누는 오류 방지
        return "0명으로 나눌 수 없습니다."

    total = a + a * (b / 100)  # 팁 포함 총 금액 계산 (들여쓰기 수정 완료!)
    return round(total / c, 2)  # 소수점 2자리 반올림

print("계산에 오신 걸 환영합니다!")

# 금액, 팁 퍼센트, 사람 수 설정
bill = int(input("얼마가 나왔습니까: "))
tip = int(input("주고 싶은 팁의 양(%)를 고르세요: "))
man = int(input("몇 명이서 먹었나요: "))

# 팁 포함 금액을 나누는 계산
result = cal(bill, tip, man)

# 결과 출력 (0명이면 예외 처리)
if isinstance(result, str):  
    print(result)  # 사람이 0명일 경우 메시지 출력
else:
    print(f"한 사람당 지불해야 하는 금액은 {result:.2f} 입니다.")  # ✅ 올바르게 실행됨