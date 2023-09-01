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
word_list = ["house","mouse","dog","rat",]
# choose_a_word= word_list[random.randrange(0,len(word_list))]
choose_a_word= random.choice(word_list)
# print(choose_a_word)

# print(len(choose_a_word))

display=[]
for i in range(len(choose_a_word)):
    display += "_"
print(display)
# Guessing the letter by input
chances_left=6

while  "_" in display and chances_left > 0:
    guess=input("Guess a letter :").lower()
    a=display.count("_")
    for position in range(len(choose_a_word)):
        letter=choose_a_word[position]
        if letter==guess:
           display[position]=letter
    if a==display.count("_"):
       chances_left-=1 
   
    print(display)
    print(stages[chances_left])

if "_" in display:
    print("you lost.")
else:print("you won.")