import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)




chosen_word = random.choice(word_list)
end_of_game = False

display = []

lives = 6

word_length = len(chosen_word)

for letter in range (word_length):
    display.append("_")
    



while  not end_of_game:
    guess = input("please guess a letter:")

    if guess in display:
        print(f"you have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
       
   
   
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")
    
        
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print("you won")
        
    print(stages[lives])
        
        