import uuid
import json
from datetime import datetime
from expense import Expense
from storage import save_expense, load_data

# ---------------------
#   COLORS
# ---------------------

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
OYAN = '\033[32m'
RESET = '\033[0m'

FILE_PATH = r'..\data\expense.json'


# ---------------------
#   ADD Expense
# ---------------------
def add_expense():
    try:
        id = str(uuid.uuid4())
        amount = int(input("Enter the amount(like: 1000):->  "))
        category = input("Enter the Category :->  ")
        desc = input("Enter the description:->  ")
        
        while len(desc) > 30:
            desc = input("Enter the description:->  ")
            print('description must be under 30 words!')
        date = datetime.today().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        
        spend = Expense(id=id,amount=amount,category=category,description=desc,date=date,time=time)
        if save_expense(spend):
            print(f"{GREEN}Expense add successfully!{RESET}")

    except ValueError:
        print(f"{RED}Please Input Valid format! {RESET}") 


# ---------------------
#   VIEW expense
# ---------------------
def view_expenses():
    data = load_data()
    print(display_card(data))

# ---------------------
#   Search expense
# ---------------------
def search_expense(data):
    try:
        category = input("Enter the category you wanna search -> ")
        display_data = []
        for i,expense in enumerate(data):
            if expense["category"].lower() == category.lower():
                display_data.append(expense)
        print(display_card(display_data))
    except Exception as e:
        print(f"{RED} ERROR OCCURED{RESET}")


# ---------------------
#   DELETE expense
# ---------------------
def delete_expense():
    try:
        data = load_data()
        serial_no = int(input("Enter the Serial number of expense that you want to delete-> "))
        if 0 < serial_no >= len(data): 
            data.pop(serial_no - 1)
            try:
                with open(FILE_PATH,'w') as file:
                    json.dump(data,file)
                print(f"{GREEN}Expense Deleted successfully{RESET}")
            except FileNotFoundError:
                print(f'{RED}DATA not Found!{RESET}')
        else:
            print(f"{RED}Please Enter valid serial no{RESET}")
    except ValueError:
        print(f"{RED}Please Enter valid number{RESET}")

# -------------------------
#   Expense display card 
# -------------------------
def display_card(data):
    total = 0
    output = []

    output.append("*"*110)

    output.append(
        f"{GREEN}{"Serial No.":<15}"
        f"{"DATE":<15}" 
        f"{"TIME":<15}"
        f"{"CATEGORY":<20}" 
        f"{"DESCRIPTION":<35}"
        f"{"AMOUNT":>5} {RESET}" )

    output.append("*"*110)

    if data:
        for i,expense in enumerate(data):

            serial_no = f"{i+1:<15}"
            date =  f"{expense['date']:<15}"
            time = f"{expense['time']:<15}"
            category = f"{expense['category']:<20}"
            desc = f"{expense['description']:<35}"
            amount = f"{expense['amount']:>5}"

            output.append(
                f"{serial_no}"
                f"{BLUE}{date}{RESET}"
                f"{BLUE}{time}{RESET}"
                f"{OYAN}{category}{RESET}"
                f"{desc}"
                f"{amount}"

            )
            total +=  expense['amount']


        output.append("*"*110)
        output.append(
            f"{"TOTAL EXPENSE":<99}"
            f"{RED} {f'₹ {total}':>5}{RESET}")
    else:
        message = f"{'No Record Found':^100}"
        output.append(f"{RED}{message}{RESET}")
    output.append("*"*110)
    return "\n".join(output)

