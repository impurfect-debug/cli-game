import random
import time


def shifumi():
    
    player_score = 0
    bot_score = 0
    choices = ["rock","paper","scissors"]
    
    while True:
        player = input("\nEnter'rock','paper','scissors' or 'q' to quit the game: ").lower()
        if player == "q":
             print("\nYou are leaving shifumi")
             time.sleep(1)
             return
        bot = random.choice(choices)     
        if player == bot:
            print("it's a draw\n")
            print(f"Your score: {player_score} | bot score:{bot_score}")
        elif player == "rock" and bot == "scissors" or player == "paper" and bot == "rock" or player == "scissors" and bot == "paper":
            player_score += 1
            print(f"\nYou've won, player score: {player_score} | bot score: {bot_score}")
        elif player == "scissors" and bot == "rock" or player == "rock" and bot == "paper" or player == "paper" and bot == "scissors": 
           bot_score += 1   
           print(f"You've lost, player score: {player_score} | bot score: {bot_score}") 
        else:
         print("Ivalid entry, please retry!")
         break

def guess_the_number():
    
    while True:
        a = random.randint(0, 10)
        b = random.randint(10, 15)
        number = random.randint(a, b)
        while True:
            user_gues = input(f"\nEnter a number between {a} and {b} or 'q' to exit\n")
            if user_gues.lower() == "q":
                print("You are leaving Guess the Number game.")
                time.sleep(1)
                return
            if not user_gues.isdigit():
                print("Please enter a valid number!")
                continue
            user_gues = int(user_gues)
            if user_gues == number:
                print("Yeah! You found it!")
                break
            elif user_gues < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
 
def main():
    
    print("\nwelcome to the cli game menu".upper())
    print("-"*29)
    while True:
        user = input("\n1.Shifumi\t2.Guess the number\t3.To quit \n")
        if user == "1":
            shifumi()
        elif user == "2":
            guess_the_number()
        elif user == "3":
            time.sleep(1)
            print("Bye!")
            break
        else:
            print("\nIvalid entry please retry!") 
            continue

if __name__ == "__main__":
    main()


    
    
    
                               
        
                
                
       
            
    