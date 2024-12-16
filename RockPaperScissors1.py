#Rock wins against scissors
#scissors win against paper
#paper wins against rock
#0 for rock
#1 for paper
#2 for scissors
import random
rock="🪨"
paper="📜"
scissors="✂"

img=[rock,paper,scissors]
user_choice=int(input("choose 0 for rock,Choose 1 for paper,choose 2 for scissors: "))
if(user_choice<0 or user_choice>2):
    print("You lose as you enter invalid no.")
else:
  print(img[user_choice])
  computer_choice=random.randint(0,2)
  print(f"Computer chose: {computer_choice}")
  print(img[computer_choice])

  if computer_choice==user_choice:
        print("MATCH DRAWN!!")
  elif(computer_choice==0 and user_choice==2):
        print("You lose.")
  elif(computer_choice==2 and user_choice==0):
        print("You win")
  elif(computer_choice>user_choice):
        print("You lose") 
  elif(user_choice>computer_choice):
        print("you win")
