# dirty_dozen = ["stawberries", "spinach", "kale", "apples", "grapes"]

# fruits = ["stawberries", "stawberries", "apples", "grapes"]
# vegetbles = ["spinach", "kale"]

# dirty_dozen = [fruits, vegetbles]
# print(dirty_dozen[1][0])

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''




game = [rock, paper, scissors]


user_choice = int(input("가위! '0' 바위! '1' 보! '2' : "))
print(game[user_choice])

computer_choice = random.randint(0, 2)
print("coputer chose: ")
print(game[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("그런 건 없소오")
elif user_choice == 0 and computer_choice == 2:
    print("당신의 승!")
elif computer_choice == 0 and user_choice == 2:
    print("컴퓨터 승!")
elif computer_choice > user_choice:
    print("컴퓨터 승!")
elif computer_choice < user_choice:
    print("당신의 승!")
elif computer_choice == user_choice:
    print("무승부!")
