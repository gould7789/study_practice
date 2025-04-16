# 키보드로부터 정수 5개를 입력받아 합계와 평균을 출력하는 프로그램을 작성하시오

"""
1. 입력: 사용자로부터 정수 5개를 입력받는다.
2. 합계 계산: 입력받은 정수의 합계를 계산한다.
3. 평균 계산:  입력받은 정수의 평균을 계산한다    
4. 결과 출력:  계산된 합계와 평균을 출력한다 
5. 코드 구조화 및 간결화: 코드의 구조가 명확하고 간결하게 작성되어야 한다다
"""

num_list = []

# 사용자로부터 정수 5개를 입력 받는다
result = 0
for char in range(5):
    input_number = int(input(f"{char + 1}번째 값을 입력하세요: "))
    num_list.append(input_number) # 입력 받은 정수를 리스트에 저장
    result += input_number        # 입력 받은 정수들의 합을 더한다
    
# 평균 계산 : 전체 숫자의 합 % 숫자의 갯수    
total = result / len(num_list) 
    
# 결과 출력
print(f"합계: {result}\n평균: {total}")

    
        
