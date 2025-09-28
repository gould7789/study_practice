"""
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오
"""

# a~z까지 아스키코드 변환으로 리스트 형성
a = [chr(word) for word in range(97, 123)]

# 사용자가 문자열 입력
user_input = input()

# 리스트를 순회하며 
for idx, word in enumerate(a):
    if word in user_input:
        print(user_input.index(word), end=" ")
    else:
        print(-1, end= " ")

# find 함수
# 문자열에서 해당 문자가 몇번째 인덱스인지 출력 및 그 문자가 없을 때 자동으로 false값 출력
for word in a:
    print(user_input.find(word), end=" ")