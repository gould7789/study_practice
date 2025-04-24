"""
사용자에게  최대  5번까지  로그인  시도를  허용하며,  올바른  아이디와  비밀번호가 입력되면 로그인 성공 메시지를 출력하고 프로그램을 종료하시오.
5번 실패하면 계정 잠금 메시지를 출력한다
"""


# 올바른 ID 및 Password 설정
user_ID = "admin"
user_PW = "1234"


# 입력 기회 5번 설정
count = 5

# 최대 5번 반복문 작성
while count > 0:
    input_ID = input("ID 입력: ")   # 사용자에게서 아이디 입력 받음
    input_PW = input("PW 입력: ")   # 사용자에게서 비밀번호 입력 받음
    
    if user_ID == input_ID and user_PW == input_PW:
        print("로그인 성공!")       # 입력된 정보가 일치했을 때 로그인 성공 출력
        break
    else:
        count -= 1                 # 정보 불일치 시 입력 횟수 차감
        print(f"ID 또는 PW가 잘못되었습니다. (남은 시도: {count})") # 사용자에게 남은 입력 횟수 알림
        print()
        
    if count == 0:                 # 입력 횟수 전부 소진 시 계정 잠금 통지
        print("계정이 잠금되었습니다.")