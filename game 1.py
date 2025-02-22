import math

# python project using while loop and if and else statement 
# basically using thr loop , the user continuously get the programmed request until he fulfils the condition 
# join me on this journey one python project per week 
# date uploaded:  saturday 22nd february 2025
# week one project 
secret_number = 9
Guess = 0
Total_Guess = 2
while Guess <= Total_Guess:
    user = int(input("Guess"))
    Guess = Guess +1
    print(f"you chose {user}") 
    if user == 9:
        print("hoory you won")
        break
    else:
        print (" better luck next time")

