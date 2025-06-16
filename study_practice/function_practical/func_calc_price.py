# 상품명과 가격을 위치 인자로 받고, 부가세율은 키워드 인자로 받도록 하여 최종 가격을 계산하는 함수 작성
# 부가세율은 입력하지 않으면 기본적으로 10% 적용
def calc_price(product, price, tax=0.10):
    total = price * tax
    result = price + total
    
    print(f"{product}의 최종 가격은 {result:.0f}원입니다.")

calc_price("노트북", 1000000)

# 필요 시 tax = 0.08 처럼 옵션으로 조정 가능
calc_price("모니터", 300000, tax=0.05)
