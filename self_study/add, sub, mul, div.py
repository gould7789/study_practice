# 사용자로부터 두 개의 정수 숫자를 입력 받고
# 그 합, 차, 곱, 나눗셈의 결과를 출력하는 프로그램 작성

# 입력받은 숫자들의 합, 차, 곱, 나눗셈 결과를계산합니다
def cal(a, b):
    add = float(a + b)
    min = float(a - b)
    mul = float(a * b)
    div = float(a / b) if b != 0 else "0으로는 나눌 수 없습니다"
    
    return add, min, mul, div

# 사용자에게 두 정수 숫자를 입력 받습니다
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

add, min, mul, div = cal(num1, num2)

# 계산된 결과를 출력 합니다
print(f"합: {add}\n차: {min}\n곱: {mul}\n나눗셈: {div}")