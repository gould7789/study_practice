# 팁 계산기 프로그램 작성
def cal(a, b, c):
    if c == 0:
       return "0명으로 나눌 수 없습니다"
       
    total = a + a * (b / 100)
    return round(total / c, 2)

print("계산에 오신 걸 환영합니다!")

# 금액, 팁 퍼센트, 사람 수 설정
bill = int(input("얼마가 나왔습니까: "))
tip = int(input("주고 싶은 팁의 양(%)를 고르세요: "))
man = int(input("몇명이서 먹었나요: "))

result = cal(bill, tip, man)

if isinstance(result, str):
    print(result)
else:
    print(f"한 사람당 지불해야 하는 금액은 {result:.2f} 입니다.")