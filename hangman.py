#!/usr/bin/env python3
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words = ["python", "java", "swift", "javascript"]
#count = 8
#word = 'java'
result = {"win":0, "lost":0} 
print("H A N G M A N  # 8 attempts", end="\n")
while True:
    count = 8
    word = random.choice(words)
    print(f'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:', end = '')
    action = input()
    letters_given = []
    word_display = ['-']*len(word)
    if action == "play":
        print(*word_display, sep = '')

        while True:
            print("Input a letter:", end = '' )
            letter = input()
            if len(letter) > 1 or len(letter) == 0:
                print("Please, input a single letter.")
            elif letter not in alphabet :
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in letters_given:
                print("You've already guessed this letter.")
            elif letter  not in word:
                count -= 1
                print(f"That letter doesn't appear in the word.  # {count} attempts".format(count))
            elif letter in word_display:
                count -= 1
                print(f"No improvements.  # {count} attempts")
            else:
                for i in [index for index, char in enumerate(word) if char == letter]:
                    word_display[i] = letter

            letters_given.append(letter)
    
            if (''.join(word_display)) == word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                result["win"] += 1 
                break
            elif count == 0 and ''.join(word_display) != word:
                print("You lost!")
                result["lost"] += 1
                break
            print(*word_display, sep = '')
    elif action == "results":
        print(result['win'])
        print('You won:', result['win'], 'times.') 
        print("You lost:", result['lost'] , "times.")
    else:
        break 

