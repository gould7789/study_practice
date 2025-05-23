"""
이 프로그램은 사용자로부터 소득금액을입력받아 소득세를 계산합니다.
소득세 계산은 다음과 같이 진행됩니다.
"""
# 첫 1만달러의 소득(income)에는 10%의 세율이 적용 됩니다.
# 1만 달러를 초과하고 2만 달러 이하의 소득에 대해서는 초과 금액에 15%의 세율을 적용용하고
# 2만 달러를 초과하는 소득에 대해서는 초과 금액에 20%의 세율을 적용하고
# 앞선 구간의 세금인2천 5백 달러를 더합니다

"""
소득 금액을 입력받는 부분과 소득세를 계산하는 부분을 함수로 작성하고
계산된 소득세를 출력하는 코드를 완성하세요
"""

# 소득세 계산 부분을 아래 함수로 작성하고, 이 함수를 호출하여 소득세계산 값을 출력하세요
# 소득세 계산 함수
def calculate_tax(income):
    if income <= 10000:
        return income * 0.10
    elif 10000 < income <= 20000:
        return (income - 10000) * 0.15 + 1000
    else:
        return (income - 20000) * 0.20 + 2500

# 사용자로부터 소득 금액 입력 받기    
mon = int(input("소득 금액을 입력하세요: "))
result = calculate_tax(mon)

# 소득세 출력
print(f"소득세는 {result}입니다.")