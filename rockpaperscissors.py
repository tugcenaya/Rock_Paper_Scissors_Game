import random

list = ["rock", "paper", "scissors"]
computer_score = 0
player_score = 0

rounds = input("How many rounds do you want to play? Enter a number here:")
round_counter = 0

while True:
  round_counter += 1
  print("Round number:", round_counter)

  computerchoice = random.choice(list)
  playerchoice = input("Your action:")

  print("Computer:", computerchoice)
  print("Player:", playerchoice)

  if computerchoice == playerchoice:
    print("Both players choose the same action.")

  elif computerchoice == "rock":
    if playerchoice == "paper":
      print("Winner is: Player")
      player_score += 1
    else:
      print("Winner is: Computer")
      computer_score += 1

  elif computerchoice == "paper":
    if playerchoice == "rock":
      print("Winner is: Computer")
      computer_score += 1
    else:
      print("Winner is: Player")
      player_score += 1

  elif computerchoice == "scissors":
    if playerchoice == "paper":
      print("Winner is: Computer")
      computer_score += 1
    else:
      print("Winner is: Player")
      player_score += 1


  if round_counter == int(rounds):
    break

if computer_score == player_score:
  print("There is no winner, tie.", computer_score, ":", player_score )
elif computer_score > player_score:
  print("You lost. Computer won with score", computer_score, ":", player_score)
elif computer_score < player_score:
  print("You won!! Player won with score", computer_score, ":", player_score)