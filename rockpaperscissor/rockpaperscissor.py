import random

print("Welcome to Rock Paper Scissor Game")
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors")
)
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

objects_graphic = [rock, paper, scissor]
objects_name = ["rock", "paper", "scissor"]


if user_choice > 2 or user_choice < 0:
    print("You Lost since invalid input")
else:
    print(f"User input is {objects_name[user_choice]} {objects_graphic[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(
        f"computer choice is {objects_name[computer_choice]} {objects_graphic[computer_choice]}"
    )
    if user_choice == computer_choice:
        print("It's a draw")
    else:
        if user_choice == 0 and computer_choice == 1:
            print("You lost")
        elif user_choice == 0 and computer_choice == 2:
            print("You won")
        elif user_choice == 1 and computer_choice == 0:
            print("You won")
        elif user_choice == 1 and computer_choice == 2:
            print("You lost")
        elif user_choice == 2 and computer_choice == 0:
            print("You lost")
        elif user_choice == 2 and computer_choice == 1:
            print("You won")
