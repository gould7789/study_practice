# 공백으로 구분된 문자열에서 특정 문자열을 검색하여 개수와 위치를 출력하는 프로그램을 작성한다

"""
▶  미리  정의된  문자열(예:  "apple  banana  orange  apple  kiwi  apple  mango")에서 사용자로부터 문자열 1개를 입력받는다.
▶ 해당 문자열이 몇 번 등장하는지 출력하고,
▶ 각 단어의 위치(인덱스)[몇 번째 단어인지]를 리스트로 출력한다.
    -인덱스는 첫 번째 단어가 0번이라고 간주
"""

# 문자열
text = "apple banana orange apple kiwi apple apple"

# 사용자가 찾을 문자열을 입력
user_input = input("찾을 문자열을 입력하세요: ")

word = ""   # 문자열을 저장해서 단어를 만들 변수
count = 0   # 인데스 위치를 카운팅
index = []  # 특정 단어의 인덱스를 저장할 리스트

# 문자열을 반복하며 단어 검색
for voca in text:
    if voca != " ":     # 공백이 아닐 때 문자로 판단
        word += voca    # 문자열을 변수에 저장
        
    else:
        if word == user_input:  # 조합된 문자열의 단어가 사용자의 입력한 단어와 같을 때
            index.append(count) # 그 단어의 인덱스를 리스트에 기록
        word = ""               # 다음 단어를 조합하기 위해 변수 초기화
        count += 1              # 인덱스 위치 판단을 위해 카운팅

# 마지막 단어는 판단할 공백이 없으므로 따로 조건식 지정
if word == user_input:
    index.append(count)

# 결과 출력
print(f"{user_input}은 총 {len(index)}번 등장합니다.")
print(f"위치(인덱스): {index}")


vocas = text.split()
index_list = [idx for idx, word in enumerate(vocas) if word == user_input]
print(f"{user_input}은 총 {vocas.count(user_input)}번 등장합니다.")
print(f"위치(인덱스): {index_list}")