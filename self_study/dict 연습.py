


# 사용자에게 하나의 문자를 입력받습니다
voc = input("한 문자를 입력하세요: "). lower()
dict = {"aeiou" : voc + "는 모음입니다."}
print(dict.get(voc, "는 모음이 아닙니다."))
