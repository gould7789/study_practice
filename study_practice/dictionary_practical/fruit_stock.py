# 가게에 있는 과일 이름과 재고 수량을 딕셔너리에 저장
# 사용자로부터 과일 이름을 입력받아 재고를 관리하는 프로그램 작성

# 과일 재고
stock = {
    "사과" : 5,
    "바나나" : 3,
    "포도" : 10
}

choice = input("구매할 과일 이름: ")
count = int(input("수량: "))

if choice in stock:
    # 재고가 모자랄 때
    if stock[choice] < count:
        print(f"재고가 부족합니다. 현재 재고: {stock[choice]}개")
    
    # 재고가 충분할 때
    else:
        stock[choice] -= count
        print(f"구매 완료! 남은 재고: {stock[choice]}개")

else:
    print("해당 과일은 판매하지 않습니다.")