import random

user_score= 0
comp_score= 0
options = ["rock", "paper", "scissors"]
comp_choice = "" 

while user_score < 5:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
       continue
    
    rand_num = random.randint(0, 2)

    comp_choice = options[rand_num]

    print("The computer chose: " + comp_choice)

    if user_input == "rock" and comp_choice == "scissors":
        user_score += 1
        print("You won!")
    elif user_input == "paper" and comp_choice == "rock":
        user_score += 1
        print("You won!")
    elif user_input == "scissors" and comp_choice == "paper":
        user_score += 1
        print("You won!")
    elif user_input == comp_choice.lower():
        print("It was a tie")

    else:
        print("You Lost!")
        comp_score += 1

    print("The current score is You: " + str(user_score) + " Computer: " + str(comp_score))

print("The final score was")
print("You: " + str(user_score))
print("Computer: " + str(comp_score))

print("Goodbye")

        
        

