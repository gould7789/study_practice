# 문자열 내 단어 개수 출력

# for문을 사용하여 아래 문자열 내 단어 개수를 출력하는 프로로그램을 작성하라

count = 1                                       # 단어는 무조건 1개 이상 존재
myString = "It is a great weather with you"     # 단어 개수를 계산할 문장


for word in myString:                           # 문장의 글자 수만큼 반복
    if word == " ":                             # 공백만큼 카운트 1 증가
        count += 1
        
print(f"문자열 단어 갯수 : {count}")


# split 버전

myString = "It is a great weather with you"
word = myString.split()

count = 0

for char in word:
    count += 1
    
print(f"문자열 단어 갯수 : {count}")


# for문 단어세기 심화버전

text = "It is a great weather with you"      # 문자열 준비
count = 0                                    # 단어 수 세는 변수
in_word = False                              # 단어 안에 있는지 표시

for char in text:    # 글자 하나씩 반복
    if char != " " and not in_word:  # 공백 아니고, 아직 단어 안이면
        count += 1                   # 단어 하나 발견
        in_word = True               # 단어 안에 들어왔다고 표시
    elif char == " ":                # 공백 만나면
        in_word = False              # 단어 끝났다고 표시

print(count)         # 단어 개수 출력