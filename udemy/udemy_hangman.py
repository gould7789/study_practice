import random

# import hangman_words # hangman_words.py 파일을 import로 불어오기
from hangman_words import word_list # 불러올 파일이 소량일 때 적절함함
from hangman_art import stages, logo
lives = 6

print(logo)

choose_word = random.choice(word_list) 
print(choose_word)

# 선택한_단어와 동일한 수의 빈칸을 가진 "자리 표시자"를 만듭니다
# placeholder = "_" * len(choose_word)
# print(placeholder)

placeholder = ""
word_length = len(choose_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# for 루프를 변경하여 이전 올바른 문자를 표시하도록 합니다.

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("답변을 입력해주세요: ").lower() # 사용자에게서 답변 입력받기

    if guess in correct_letters:
        print(f"이미 입력한 답입니다 : {guess}")

    display = ""

    for letter in choose_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print(display)
    
    
    if guess not in choose_word:
        lives -= 1
        print(f"입력한 {guess}는 정답에 없습니다. 생명이 하나 줄어듭니다.")
        if lives == 0:
            game_over = True
            print(f"*********************** 정답은 {choose_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        
    print(stages[lives])