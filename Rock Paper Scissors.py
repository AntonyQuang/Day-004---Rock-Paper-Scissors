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

#Write your code below this line 👇
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player > 2 or player < 0:
    print("Invalid choice. Please start again.")
else: 

    cpu = random.randint(0,2)
    game_images =[rock,paper,scissors]
    player_img = game_images[player]
    cpu_img = game_images[cpu]
    
    print(f"\nYou chose: {player_img}")

    print(f"\nThe computer chose: {cpu_img}")


    if player == cpu:
        print("It's a draw.")
    elif cpu + 1 == player:
        print("You win.")
    elif cpu == 2 and player == 0:
        print("You win.")
    else:
        print("You lose.")
