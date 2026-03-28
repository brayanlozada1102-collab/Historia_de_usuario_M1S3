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
    """
    function that records data in a list using dictionaries
    """
    update = {
            "name":product_name,
            "price" : unit_value,
            "quantity" : quantity,
         
         }
    daily_sales.append(update)
    print(f"Product {product_name} successfully registered!")
    return daily_sales

def show_summary(daily_sales: list) -> list :
    """
    This function displays the inventory contents
    """
    for i in daily_sales:
        print(f"{i['name']} \nQuantity of product in the inventory: {i['quantity']} \nPrice per unit: ${i['price']}\nTotal value of the product in inventory: ${i['price']*i['quantity']}")
        print("---------------------")
def search_product(inventory, name):
    """Searches for a product by name and returns it. If it does not exist, it returns None."""
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None
def update_product(inventory, name, new_price=None, new_quantity=None):
    """Update price and/or quantity of an existing product."""
    product = search_product(inventory, name)
    if product:
        if new_price is not None: product["price"] = new_price
        if new_quantity is not None: product["quantity"] = new_quantity
        return True
    return False
def delete_product(inventory, name):
    """Remove a product from the inventory by name."""
    productdelete = search_product(inventory, name)
    if productdelete:
        inventory.remove(productdelete)
        return True
    return False
def calculate_statistics(inventory):
    """Calculate inventory metrics using lambdas for subtotals."""
    if not inventory: 
        return None
    
    # Lambda function to calculate the subtotal of a product
    subtotal = lambda x: x["price"] * x["quantity"]
    
    total_units = sum(product["quantity"] for product in inventory)
    total_valeu = sum(subtotal(product) for product in inventory)
    
    # lambda function to achieve maximums
    more_expensive = max(inventory, key=lambda p: p["price"])
    largest_stock = max(inventory, key=lambda p: p["quantity"])
    
    return {
        "units": total_units,
        "valeu": total_valeu,
        "expensive": (more_expensive["name"], more_expensive["price"]),
        "stock": (largest_stock["name"], largest_stock["quantity"])
    }