"""
문제 개요
- 별다방에서 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램을 작성하시오.
- 이 실습문제를 통해 선택문 흐름 제어의 다양한 구조를 이해하고, 실제 서비스 로직
설계에 가까운 조건문 분기를 실습해 본다
"""

"""
문제 설명
- 고객에게 다음 정보를 입력받고, 이에 따라 최종 주문 정보와 혜택을 출력하시오
- 모든 입력은 정확한 값이 들어온다고 가정(Happy scenario)하며, 입력값에 대한 오류
예외 처리는 하지 않는다.
‣ 입력 항목
① 음료 종류 (coffee, latte, juice 중 하나)
② 크기 (small, medium, large)
③ 멤버십 여부 (yes, no)
‣ 입력 항목
1) 가격 계산
‣ coffee: 3000원
‣ latte: 4000원
‣ juice: 3500원
2) 크기 추가 요금
‣ small: 추가 없음
‣ medium: 500원 추가
‣ large: 1000원 추가
3) 멤버십 혜택
‣ 멤버십 고객에게는 총 금액의 10% 할인 적용
4) 무료 샷 제공 조건
‣ 멤버십 고객 중, coffee 또는 latte 주문이면서 크기가 large인 경우
→ "무료 샷이 제공됩니다!" 문구 출력(중첩 조건 사용)
"""


# 사용자에게 음료를 입력 받음
choice_drink = input("음료를 선택하세요 (coffee, latte, juice): ").lower() # 음료 선택
drink_price = 0   # 음료의 가격

# 고객이 각 음료를 주문 했을 때 가격 결정
if choice_drink == "coffee":
    drink_price = 3000
elif choice_drink == "latte":
    drink_price = 4000
elif choice_drink == "juice":
    drink_price = 3500
    

# 사용자에게 음료의 크기를 입력 받음
size = input("크기를 선택하세요 (small, medium, large): ").lower() # 크기 선택
size_price = 0  # 크기 추가 요금

# 크기별 추가 요금
if size == "medium":
    size_price = 500
elif size == "large":
    size_price = 1000

total = drink_price + size_price

# 사용자에게 멤버십 유무를 입력 받음
membership = input("멤버십이신가요? (yes/no): ").lower()
membership_discount = 0
membership_no = "없음"

# 멤버십 고객에게는 할인 적용
if membership == "yes":
    membership_discount = int(total * 0.1) # 멤버십 고객에게는 총 금액의 10% 할인 적용
    membership_no = f"-{membership_discount}원"
else:
    membership_no
    
 
print(f"""기본가격: {drink_price}원
크기 추가 요금: {size_price}원
할인 적용: {membership_no}
최종 결제 금액: {total - membership_discount}원""")    

# 멤버십 고객 중, coffee 또는 latte 주문이면서 크기가 large인 경우 "무료 샷이 제공됩니다!" 
if (choice_drink == "coffee" or choice_drink == "latte") and size == "large":
        print("무료 샷이 제공됩니다!")  
