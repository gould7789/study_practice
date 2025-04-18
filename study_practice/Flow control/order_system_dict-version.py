"""
- 리스트(list), 딕셔너리(dict) 자료구조 사용
- 반복(for) 사용
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


# 주문 정보 입력
choice_drink = input("음료를 선택하세요 (coffee/latte/juice): ").lower()
choice_size = input("크기를 선택하세요 (small/medium/large): ").lower()
choice_membership = input("멤버십이신가요? (yes/no): ").lower()

# 음료 정보를 딕셔너리에 저장
drink = {
    "coffee" : 3000,
    "latte"  : 4000,
    "juice"  : 3500
}

# 사이즈 정보를 딕셔너리에 저장
size = {
    "small"  : 0,
    "medium" : 500,
    "large"  : 1000
}

# 가격 계산 
total = drink[choice_drink] + size[choice_size]     # 음료 가격 + 사이즈 추가 요금
discount = total * 0.1                              # 멤버십 할인 10%
final_total = total - discount                      # 멤버십을 가입한 손님일 때 최종 요금

# 할인 문구 및 최종 결과 계산
discount_str = f"-{int(discount)}원" if choice_membership == "yes" else "없음"      # 멤버십이 없을 때 "없음" 출력
final_price = f"{int(final_total) if choice_membership == "yes" else total}원"      # 최종 결제 금액 출력

# 출력
print(f"""기본 가격 : {drink[choice_drink]}원
크기 추가요금 : {size[choice_size]}원
할인적용 : {discount_str}
최종 결제 금액 : {final_price}""")


# 무료 샷 조건
if (choice_membership == "yes") and (choice_drink in ["coffee", "latte"]) and (choice_size in ["large"]):
    print("무료 샷이 제공 됩니다!")