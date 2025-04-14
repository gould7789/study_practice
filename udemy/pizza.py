"""
스몰 피자 : $15
미디엄 피자 : $20
라지 피자 : $25
스몰 피자에 페퍼로니 더하기 : $2
미디엄, 라지 피자에페퍼로니 더하기 : $3
치즈 더하기 : $1
"""

# 각 음식별 사이즈 및 가격
pizza_price = {"S":15, "M":20, "L":25}
pepperoni_price = {"S":2, "M":3, "L":3}
cheese_price = 1

print("피자 주문!")

# 사용자에게 피자 주문 질문 출력
size = input("어떤 사이즈를 주문 하시겠습니까? (S, M, L): ").upper()
pepperoni = input("페퍼로니를 추가하시겠습니까? Y or N: ").upper()
cheese = input("치즈를 추가하시겠습니까? Y or N: ").upper()

# 상황에 따른 최종 가격 계산
if size not in pizza_price:
    print("없는 사이즈 입니다.")
elif pepperoni not in ["Y", "N"] or cheese not in ["Y", "N"]:
    print("Y 또는 N 중에 선택해주세요")
else:
    bill = pizza_price[size]
    bill += pepperoni_price[size] if pepperoni == "Y" else 0
    bill += cheese_price if cheese == "Y" else 0
    print(f"최종 금액은 ${bill}입니다.")