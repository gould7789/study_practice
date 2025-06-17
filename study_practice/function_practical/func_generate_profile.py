# 고객의 기본 정보, 관심 항목, 기타 메타 정보를 바탕으로 개인 맞춤형 요약 보고서를 생성하는 함수 작성

"""
•  name, age: 필수 위치 인자 (positional arguments)
•  gender: 선택 키워드 인자 (기본값: "미정")
•  *interests: 고객이 선택한 관심 항목 (가변 위치 인자)
• **metadata: 기타 추가 정보 (예: 직업, 거주 국가, 회원 등급 등)
"""

# vanilla 버전
def generate_profile(name, age, gender="미정", *interests, **metadata):
    print("출력:")
    print("[고객 프로필]")
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"성별: {gender}")    # 사용자에게 입력된 성별이 없으면 "미정" 출력
    
    # 취미
    if interests:
        print("관심사: ", end="")
        last_idx = len(interests) - 1
        # 마지막 단어는 뒤에 ","가 아닌 줄바꿈으로 출력
        for idx, val in enumerate(interests):
            print(f"{val}{(", " if idx != last_idx else "\n")}", end="")
    
    # 추가 정보
    if metadata:
        print(f"추가 정보: ", end="")
        last_idx = len(metadata) - 1
        # 마지막 단어는 뒤에 ","가 아닌 줄바꿈으로 출력
        for idx, (key, val) in enumerate(metadata.items()):
            print(f"{key}={val}{(", " if idx != last_idx else "\n")}", end="")
            

generate_profile("홍길동", 30)
generate_profile("지민", 26, "남성", *["여행", "사진", "독서"], job="디자이너", country="한국")