"""
- 별다방에서 고객의 주문을 받아 음료 가격과 혜택을 계산하는 프로그램을 작성하시오.
-  이  실습문제를  통해  선택문  흐름  제어의  다양한  구조를  이해하고,  실제  서비스  로직 설계에 가까운 조건문 분기를 실습해 본다
"""

"""
- 고객에게 다음 정보를 입력받고, 이에 따라 최종 주문 정보와 혜택을 출력하시오
- 모든 입력은 정확한 값이 들어온다고 가정(Happy scenario)하며, 입력값에 대한 오류 예외 처리는 하지 않는다.
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
‣ 멤버십 고객 중, coffee 또는 latte 주문이면서 크기가 large인 경우 → "무료 샷이 제공됩니다!" 문구 출력(중첩 조건 사용)
"""


# 음료의 가격, 크기, 멤버십 여부 입력
choice_drink = input("음료를 선택하세요 (coffee/latte/juice): ").lower().strip()
choice_size = input("크기를 선택하세요 (small/medium/large): ").lower().strip()
choice_member = input("멤버십이신가요? (yes/no): ").lower().strip()

# 음료 가격 딕셔너리 정리
drink = {
    "coffee" : 3000,
    "latte"  : 4000,
    "juice"  : 3500
}

# 크기 추가 요금 딕셔너리 정리
size = {
    "small"  : 0,
    "medium" : 500,
    "large"  : 1000 
}

# 할인 전 총 합계
total = drink[choice_drink] + size[choice_size]

# 멤버십 유무에 따른 결과값 설정
if choice_member == "yes":
    member_discount = total * 0.1                   # 멤버십 고객 10% 할인 적용
    final_total = f"{int(total - member_discount)}" # 멤버십 고객일 때 최종 금액
    str_discount = f"-{int(member_discount)}원"       # 멤버십 고객일 때 할인 금액
else:
    member_discount = 0                             # 멤버십 고객이 아닐 때 할인 비율
    final_total = total                             # 멤버십 고객이 아닐 때 최종 금액
    str_discount = "없음"                           # 멤버십 고객이 아닐 때 출력 문구

# 최종 출력
print(f"""기본 가격: {drink[choice_drink]}원
크기 추가 요금: {size[choice_size]}원
할인 적용: {str_discount}
최종 결제 금액: {final_total}원""")

# 멤버십 고객이면서 커피/라떼 + large 사이즈일 경우 무료 샷 제공
if choice_member == "yes" and choice_drink in ["coffee", "latte"] and choice_size == "large":
    print("무료 샷이 제공됩니다!")