from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES={"I":"Income",
            "E": "Expense"}

def get_date(prompt,allow_default=False):
    while True:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(date_format)
        try:
            valid_date = datetime.strptime(date_str,date_format)
            if(valid_date):
                return valid_date.strftime(date_format)
                break;
        except ValueError:
            print("Invalid date format.Please enter the date in dd-mm-yyyy format")
            
    


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <=0:
            raise ValueError("Amount  must be  non-negative non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter the category  ('I for Income or 'E' for expense): ")
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category.Please enter 'I' for income or 'E' for expense ")
    return get_category()


def get_description():
    description = input("Enter the description: ")
    return description