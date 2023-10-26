import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple","camel","umbrella"]
chosen_word = random.choice(word_list)
end_of_game = False
print(f'solutin {chosen_word}')
display = []

lives = 6

word_length = len(chosen_word)

for letter in range (word_length):
    display.append("_")
    
print(display)



while  not end_of_game:
    guess = input("please guess a letter:")

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
        
        