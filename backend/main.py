import time
from storage import load_data
from manage import add_expense,view_expenses,search_expense,delete_expense

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
OYAN = '\033[32m'
RESET = '\033[0m'

def validating_input(placeholder,options_range):
    try:
        user_choice = int(input(placeholder))

        if 0 < user_choice <= options_range:
            return user_choice

        else:
            print(f"{RED}Please enter valid service code!{RESET}")

    except Exception as e:
        print("Invalid Input.",e)

def typing_animation(line,sleep=0.005):
    for char in line:
        print(char,end="")
        time.sleep(0.005)

line = """
===== EXPENSE TRACKER =====

1. Add Expense
2. View Expenses
3. Search Expense
4. Delete Expense
5. Total Expenses
6. Exit\n"""
        

if __name__ == "__main__":
    data = load_data()


    while True:
        # Typing Animations
        typing_animation(line)

        # Taking imput from user
        user_choice = validating_input("Enter the service code you want to access:- ",6)
        if user_choice == 1:
            add_expense()

        elif user_choice == 2:
            view_expenses()
        
        elif user_choice == 3:
            search_expense(data)

        elif user_choice == 4:
            delete_expense()

        elif user_choice == 6:
            endline = f"{GREEN}Thanks for using our application.{RESET}"
            typing_animation(endline,sleep=0.05)
            break
