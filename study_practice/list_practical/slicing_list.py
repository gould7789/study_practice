# 사용자로부터 받은 리스트에서 다양한 슬라이싱 방법으로 부분 리스트를 생성한다

"""
▶ 사용자로부터 정수 10개를 입력받아 리스트 data 생성
▶ 다음과 같은 조건에 따라 부분(복사된) 리스트 출력
- 처음 5개 원소
- 뒤에서 3개 원소
- 짝수 인덱스 원소만 추출
- 리스트를 거꾸로 뒤집은 결과
"""

# 반복해서 출력할 메뉴 함수 작성
def menu():
    while True:
        print("""[메뉴]
1. 처음 5개 원소
2. 뒤에서 3개 원소
3. 짝수 인덱스 원소
4. 거꾸로 뒤집은 리스트
5. 시스템 종료\n""")
        
        menu_choice = int(input("메뉴를 선택해주세요: "))   # 사용자에게 메뉴 선택 받음
        
        if menu_choice == 1:        # 처음 5개 원소 출력
            result = (data[:5])
            
        elif menu_choice == 2:      # 뒤에서 3개 원소
            result = (data[-3:])
            
        elif menu_choice == 3:      # 짝수 인덱스 원소
            result = (data[::2])
            
        elif menu_choice == 4:      # 거꾸로 뒤집은 리스트
            result = (data[::-1])
            
        elif menu_choice == 5:      # 프로그램 종료
            print("프로그램을 종료합니다.")
            break
            
        else:                       # 오류메시지 출력
            result = "메뉴 안에서 선택해주세요."
            
        print(result)
        print()



# 리스트 생성
data = []
print("정수 10개를입력하세요.")

# 사용자로부터 정수 10개를 입력 받음
for index in range(1, 11):
    user_input = int(input(f"{index}번째 정수: "))
    data.append(user_input)

# 원본 리스트 출력
print(f"\n[원본 리스트]\n{data}\n")


# 메뉴 반복 출력
menu()
