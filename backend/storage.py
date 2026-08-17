from expense import Expense
import json 


FILE_PATH = r'..\data\expense.json'

def load_data():
    try:
        with open(FILE_PATH,'r') as file:
            data = json.load(file)
            if isinstance(data,list):
                return data
            return []
            
    except FileNotFoundError:
        return []
    

    except Exception as e:
        print("Unexpected error occurred",e)
        return []


def save_expense(expense: Expense):
    try:
        expenses = load_data()
        expenses.append(expense.__dict__)
        with open(FILE_PATH,'w') as file:
            json.dump(expenses,file)
            return True
    except Exception as e:
        print("Unexpected error occurred",e)



