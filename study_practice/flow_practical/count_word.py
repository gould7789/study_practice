# 문자열 내 'h' 글자 개수 구하기

# for문을 사용하여 아래 문자 내 'h'의 개수를 출력하는 프로그램을 작성하라

count = 0
myString = "hello hyundai hoho"         # h 개수를 출력 할 문장

for word in myString:                   # 글자의 수만큼 반복
    if word == "h":                     # 문장의 h일 때마다 카운트 + 1
        count += 1
        
print(f"문자열 내 h 갯수 : {count}")