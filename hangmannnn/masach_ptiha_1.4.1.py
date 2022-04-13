
   
def name_of_game():
	print("""
Welcome to the Game Hangman		 
  _    _ 
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                                                                                                      

""")
name_of_game()																								   
import random
num_of_guesses = random.randint(5,10)	
print(num_of_guesses)