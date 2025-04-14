"""
키보드로부터 영문 문자열을 입력 받아, 아래 테이블 규칙을 따라
한글로 변환하는 프로그램을 작성하라.
단, 아래 테이블 이외의 영문 이름이 입력 될 경우 “그 외” 문자열 출력
"""

company = {
    "SAMSUNG" : "삼성",
    "NAVER" : "네이버",
    "LG" : "엘쥐",
    "HYENDAI" : "현대",
    "KAKAO" : "카카오",
    "SK" : "에스케이"
}

input_value = input("회사명을 입력하세요: ").upper()

if input_value in company:
    print(company[input_value])
else:
    print("그 외")