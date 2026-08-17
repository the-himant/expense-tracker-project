from storage import load_data
from manage import add

def validating_input(placeholder,options_range):
    try:
        user_choice = int(input(placeholder))

        if 0 < user_choice <= options_range:
            return user_choice

        else:
            print("Please enter valid service code!")

    except Exception as e:
        print("Invalid Input.",e)


if __name__ == "__main__":
    data = load_data()

    print("""
    ===== EXPENSE TRACKER =====

    1. Add Expense
    2. View Expenses
    3. Delete Expense
    4. Total Expenses
    5. Exit
    """
    )



    while True:
        user_choice = validating_input("Enter the service code you want to access:- ",5)
        if user_choice == 1:
            add()

        elif user_choice == 5:
            print("Thanks for using our application.")
            break
