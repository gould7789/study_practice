# 가게의 메뉴와 가격을 딕셔너리로 저장하고
# 사용자로부터 메뉴 이름과 수량을 입력받아 총 주문 금액을 계산하는 프로그램 작성

# 메뉴와 가격을 저장하는 딕셔너리
menu = {
    "김밥" : 2500,
    "라면" : 3000,
    "떡볶이" : 4000,
    "순대" : 3500
}

# 사용자에게 메뉴를 입력 받음
choice = input("주문할 메뉴 이름: ")

# 사용자에게 메뉴 수량을 입력 받음
count = int(input("수량: "))

if choice in menu:
    total = menu[choice] * count    # 메뉴 총 가격 계산
    print(f"총 주문 금액은 {total}원입니다.")
    
else:
    print("해당 메뉴는 없습니다.")