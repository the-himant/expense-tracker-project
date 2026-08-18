from datetime import datetime
from expense import Expense
from storage import save_expense, load_data
import uuid

# ---------------------
#   COLORS
# ---------------------

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
OYAN = '\033[32m'
RESET = '\033[0m'

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
        print(spend)
        if save_expense(spend):
            print(f"{GREEN}Expense add successfully!{RESET}")

    except ValueError:
        print(f"{RED}Please Input Valid format! {RESET}") 


# ---------------------
#   VIEW expense
# ---------------------
def view_expenses():
    total = 0
    data = load_data()
    print(display_card(data))




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

