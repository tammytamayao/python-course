#import module for randomisation
import random;
#assign values for rock paper and scissors
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

choices = [rock, paper, scissors];
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ");
computer = random.randint(0,len(choices)-1);

if int(user) == 0:
    print(rock);
elif int(user) == 1:
    print(paper);
elif int(user) == 2:
    print(scissors);

print("Computer chose:")

if computer == 0:
    print(rock);
elif computer == 1:
    print(paper);
elif computer == 2:
    print(scissors);

if int(user) == computer:
    print("It's a draw");
elif (int(user) - computer) == 1 or (computer - int(user)) == 2:
    print("You win");
elif (computer - int(user)) == 1 or (int(user) - computer) == 2:
    print("You lose");

