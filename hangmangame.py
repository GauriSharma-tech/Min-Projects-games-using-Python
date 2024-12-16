import random
word_list=["apple","banana","orange","potato","beautiful","babydoll"]
lives=int(input("Enter the no. of lives: "))
choosen_word=random.choice(word_list)
print(f"The chosen word is : {choosen_word}")
display=['_']*len(choosen_word)
print(display)

game_over=False
while not game_over:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(choosen_word)):
        letter=choosen_word[position]
        if letter==guessed_letter:
           display[position]=guessed_letter
    print(display)


    if guessed_letter not in choosen_word:
        lives-=1
        print(f"Incorrect guess! Lives remaining: {lives}")
        if lives==0:
            game_over=True
            print("You Lose!!")
            break;
          
    if '_' not in display:
        game_over=True
        print("You win")