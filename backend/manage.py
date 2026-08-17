from datetime import datetime
from expense import Expense
from storage import save_expense
import uuid


def add():
    try:
        id = str(uuid.uuid4())
        amount = int(input("Enter the amount(like: 1000):->  "))
        categories = input("Enter the Categories :->  ")
        desc = input("Enter the description:->  ")
        date = datetime.today().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        
        spend = Expense(id=id,amount=amount,categories=categories,description=desc,date=date,time=time)
        print(spend)
        if save_expense(spend):
            print("Expense add successfully!")

    except ValueError:
        Print("Please Input Valid format! ") 
