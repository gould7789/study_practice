# 공백으로 구분된 문자열에서 특정 문자열을 검색하여 개수와 위치를 출력하는 프로그램을 작성한다

"""
▶  미리  정의된  문자열(예:  "apple  banana  orange  apple  kiwi  apple  mango")에서 사용자로부터 문자열 1개를 입력받는다.
▶ 해당 문자열이 몇 번 등장하는지 출력하고,
▶ 각 단어의 위치(인덱스)[몇 번째 단어인지]를 리스트로 출력한다.
    -인덱스는 첫 번째 단어가 0번이라고 간주
"""

# 문자열
text = "apple banana orange apple kiwi apple apple"

word = ""   # 문자열을 순회하며 문자를 저장
count = 0   # 입력한 단어가 몇번 나오는지 카운트
index = []  # 입력한 단어의 인덱스 위치

# 사용자에게 찾을 문자열을 입력받음
user_input = input("찾을 문자열을 입력하세요: ")

# for을 사용하여 문자열 순회
# 공백을 기준으로 단어 판단
for voca in text:
    if voca != " ":
        word += voca
    
    else:
        if word == user_input:  # word 안의 저장된 단어가 사용자가 입력한 단어와 일치하면
            index.append(count) # 해당 단어의 인덱스 위치를 리스트에 저장
        word = ""
        count += 1
        
# 마지막 단어 처리 - 마지막 단어 뒤에는 공백이 없으므로 따로 if문 지정
if word == user_input:
    index.append(count)

# 출력
print(f"{user_input}은 총 {len(index)}번 등장합니다.")
print(f"위치 (인덱스): {index}")