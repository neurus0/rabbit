import random

print("This is ODD/IF.\nIt is a game like cricket between two players.\nThe rules are:")
print("\t1. First you choose ODD or IF(even).")
print("\t2. Then you toss, it is decided by you and the computer choosing a number randomly.\n"
      "\t   And then if the sum of your and computer's number is odd or even, based on your choice you will get batting or bowling.")
print("\t3. When batting, if the bowler and the batter choose the same number, the batsman gets out\n"
      "\t   and the score of the batsman +1 is the target.\n\n")

choice = ["batting", "bowling"]
bold = '\033[1m'
normal = '\033[0m'

def choose_number():
    while True:
        try:
            num = int(input("Enter any random number (1-10): "))
            if 1 <= num <= 10:
                return num 
            else:
                print("ENTER A NUMBER BETWEEN 1 TO 10 ONLY, YOU BLIND!!")
        except ValueError:
            print("I ASKED YOU ENTER A NORMAL NUMBER!!!")

def toss(total_num, uc):
    if total_num % 2 == 0:
        print("It's an IF (even)")
        if uc == "if":
            user_choice = input("You won the toss! What do you want, batting or bowling? ").lower()
            return user_choice, "bowling" if (user_choice == "batting") else "batting"
        else:
            print(f"You {bold}lost{normal} the toss!")
            return comp_choice, "batting" if (comp_choice == "bowling") else "bowling"
    else:
        print("It's an ODD")
        if uc == "odd":
            user_choice = input(f"You {bold}won{normal} the toss! What do you want, batting or bowling? ").lower()
            return user_choice, "bowling" if (user_choice == "batting") else "batting"
        else:
            print("You lost the toss!")
            return comp_choice, "batting" if (comp_choice == "bowling") else "bowling"

def user_batting(t=0):
    score = 0
    while True:
        user_run = choose_number()
        comp_run = random.randint(1, 10)
        print(f"Computer chose {comp_run}")
        if user_run == comp_run:
            print(f"You are {bold}out!{normal} Your score was {score}")
            return score 
        else:
            score += user_run
            print(f"Your score: {score}")
            if t != 0 and t <= score:
                return score

def user_bowling(t=0):
    score = 0
    while True:
        user_run = choose_number()
        comp_run = random.randint(1, 10)
        print(f"Computer chose {comp_run}")
        if user_run == comp_run:
            print(f"Computer is {bold}out!{normal} Computer score was {score}")
            return score 
        else:
            score += comp_run
            print(f"Computer's score: {score}")
            if t != 0 and t <= score:
                return score

while True:
    start = input("Enter 'p' to play and 'q' to quit: ").lower()
    if start == 'q':
        break
    elif start != 'p':
        print("Enter 'p' or 'q' only!")
        continue

    print("\nChoose a number between 1-10 for all cases!")
    user_choice1 = input("Choose ODD or IF (even): ").lower()
    while user_choice1 not in ["odd", "if"]:
        user_choice1 = input("Please choose either 'ODD' or 'IF': ").lower()

    num = choose_number()
    comp_num = random.randint(1, 10)

    print(f"Computer chose {comp_num}")
    total_num = num + comp_num
    print(f"Sum = {total_num}")

    comp_choice = random.choice(choice)
    user_ans, comp_ans = toss(total_num, user_choice1)

    if user_ans == "batting":
        print("\nYou will bat.")
        print("Computer will ball.\n")

        user_score = user_batting()
        print(f"\n{bold}Computer target is {user_score + 1} {normal}")
        comp_score = user_bowling(user_score)
        if user_score > comp_score:
            print(f"{bold}You win!")
        elif user_score < comp_score:
            print(f"{normal}Computer wins!")
        else:
            print("It's a tie!")

    elif user_ans == "bowling":
        print("\nYou will ball.")
        print("Computer will bat.\n")

        comp_score = user_bowling()
        print(f"\n{bold}Your target is {comp_score + 1} {normal}")
        user_score = user_batting(comp_score)
        if user_score > comp_score:
            print(f"{bold}You win!{normal}")
        elif user_score < comp_score:
            print(f"{bold}Computer wins!{normal}")
        else:
            print("It's a tie!")