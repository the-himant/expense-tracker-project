from storage import load_data
from manage import add_expense,view_expenses

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


if __name__ == "__main__":
    data = load_data()

    while True:
        print("""
    ===== EXPENSE TRACKER =====

    1. Add Expense
    2. View Expenses
    3. Delete Expense
    4. Total Expenses
    5. Exit
    """
    )
        user_choice = validating_input("Enter the service code you want to access:- ",5)
        if user_choice == 1:
            add_expense()

        elif user_choice == 2:
            view_expenses()

        elif user_choice == 5:
            print(f"{GREEN}Thanks for using our application.{RESET}")
            break
