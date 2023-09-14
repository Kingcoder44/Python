import os
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                     ''')

word_list = ["aardvark", "baboon", "camel"]
length = []
import random

word = random.choice(word_list)
#print({word})
# char = input("Enter char \n")

for i in range(len(word)):
    length.append('_')

end = False
live = 6

while not end and live > 0:
    #os.system('clear')  # Add this line to clear the screen after each guess
    char = input("Enter a character: ")

    if len(char) != 1:
        print("Please enter a single character.")
    else:
        found = False
        for i in range(len(word)):
            if char == word[i]:
                length[i] = char
                found = True

        if found:
            print("Correct guess!")
        else:
            live -= 1
            print(f"Wrong guess. You have {live} lives left.")
        

        print(" ".join(length))

    if "_" not in length:
        end = True
        print("Congratulations! You win")
    elif live == 0:
        print("Game over. The word was:", word)
