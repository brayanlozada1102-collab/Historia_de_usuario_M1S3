def validate_inputs(type : type, message:str, is_number:bool= False) -> str | float | int :
    """
    Validate the inputs to ensure they are in the correct format
    If it's a number, set the last argument to true.
    """
    warning = ""
    while message:
        try:
            a = type(input(f"Enter {message}{warning}: "))
            if is_number:
                if a <= 0:
                    print("Enter a positive number")
                    warning = " positive"
                    continue
            return a
        except:
            print(f"Enter a valid {'number' if is_number else 'letter'}")
            warning = " again"
            
def inventory_register(product_name: str,quantity: int,unit_value: float,daily_sales: list):
    update = {
            "name":product_name,
            "unitvalue" : unit_value,
            "quantity" : quantity,
         
         }
    daily_sales.append(update)
    print(f"Product {product_name} successfully registered!")
    return daily_sales

def show_summary(daily_sales: list) -> list :
    for i in daily_sales:
        print(f"{i['name']} \nQuantity of product in the inventory: {i['quantity']} \nPrice per unit: ${i['unitvalue']}\nTotal value of the product in inventory: ${i['unitvalue']*i['quantity']}")
        print("---------------------")
