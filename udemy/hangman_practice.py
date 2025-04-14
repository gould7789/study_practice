# 행맨 프로그램 작성
import random

from hangman_words import word_list
from hangman_art import stages, logo
life = 6

print(logo)

# word_list에서 랜덤으로 단어 출력
choose_words = random.choice(word_list)
print(choose_words)

# 단어에 맞게 _ 출력
placeholder = ""
word_length = len(choose_words)
for _ in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False

# 사용자에게 입력 받은 문자들을 리스트에 저장
correct_words = []
# 사용자에게 단어 입력 받음

    
# 입력 받은 단어를 확인 후 정답이면 입력, 오답이면 _ 출력
# 라이프가 0이 되면 게임오버 패배
# _ 가 다 사라지면 게임오버 승리