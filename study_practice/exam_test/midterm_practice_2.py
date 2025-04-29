"""
사용자에게 최대 5번까지 로그인 시도를 허용하며, 올바른 아이디와 비밀번호가 입력되면 로그인 성공 메시지를 출력하고 프로그램을 종료하시오.
5번 실패하면 계정 잠금 메시지를 출력한다
"""

"""
조건
- ID: admin, PW: 1234
- 입력 기회: 최대 5회
- 로그인 성공 시 → "로그인 성공!" 출력 후 종료
- 실패 5회 초과 시 → "계정이 잠금되었습니다." 출력
"""


# 정답인 아이디와 비밀번호 설정
user_ID = "admin"
user_password = 1234

# 로그인 횟수
count = 5

# 반복문을 사용하여 시도 횟수 제한
while count > 0:
    input_ID = input("ID 입력: ")       # 사용자에게 ID와 비밀번호를 입력 받는다
    input_password =  input("PW 입력: ")

    
    if input_ID == user_ID and input_password == user_password: 
        print("로그인 성공!")       # ID와 비밀번호가 일치 했을 때 "로그인 성공!" 출력 후 종료
        break
    else:
        count -= 1
        print(f"ID 또는 PW가 잘못 되었습니다. (남은 시도: {count})") # 틀렸을 경우 시도 횟수 1씩 차감
        print()
        
    if count == 0:     
        print("계정이 잠금되었습니다.")     # 5회 초과 시 "계정이 잠금 되었습니다." 출력