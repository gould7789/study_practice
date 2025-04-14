# student_scores = [150, 142, 185, 120, 174, 185, 35, 456, 47, 74]


# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
        
# print(max_score)

# total = 0
# for number in range(1, 101):
#     total += number
    
# print(total)



# Fizz Buzz 게임

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("비밀번호 생성기")

try:
    password_list = []
    #사용자에게서 희망 비밀번호 조건 입력
    nr_letter = int(input("몇 개의 문자를 넣으시겠습니까? "))
    nr_number = int(input("몇 개의 숫자를 넣으시겠습니까? "))
    nr_symbol = int(input("몇 개의 기호를 넣으시겠습니까? "))
    
    if nr_letter < 0 or nr_number < 0 or nr_symbol < 0:
        print("0 이상의 숫자를 입력해주세요.")
    else:
        for _ in range(nr_letter):
            password_list.append(random.choice(letters))
        for _ in range(1, nr_number + 1):
            password_list.append(random.choice(numbers))
        for _ in range(1, nr_symbol + 1):
            password_list.append(random.choice(symbols))
            
        random.shuffle(password_list)
        print(password_list)
        
        password = ''.join(password_list)
        
        print(f"당신의 비밀번호는 {password}입니다.")
except ValueError:
    print("숫자를 입력해주세요.")

# # 쉬운 버전
# password = ""
# # 원하는 문자 숫자가 4자리
# for char in range(1, nr_letter + 1):
#     password += random.choice(letters)
    
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
    
# for char in range(1, nr_number + 1):
#     password += random.choice(numbers)

# print(password)


# 어려운 작업

# password_list = []
# # 원하는 문자 숫자가 4자리
# for char in range(1, nr_letter + 1):
#     password_list.append(random.choice(letters))
    
# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))
    
# for char in range(1, nr_number + 1):
#     password_list.append(random.choice(numbers))

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char
    
# print(f"당신의 비밀번호는 : {password}")

