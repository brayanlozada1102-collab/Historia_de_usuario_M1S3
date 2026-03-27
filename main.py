from app import validate_inputs, inventory_register, show_summary
inventory_valeu = 0
number_of_units = 0
inventorylist = []
def main(inventorylist,number_of_units,inventory_valeu):
    
    #This is the introduction message
    print("--- Inventory System S3 ---")

    #We run the program In a while loop, so the program only stop when we decide.  
    option = ":)"
    while option != "0" :
        #This is the menu options.
        print("\n1. Register Product \n2. View Inventory \n3. Calculate Statistics \n4. Search Product \n0. Exit")
        option = input("Select an option: ")
        
        if option == "1":
            #The first option is to create a new user in the user database.
            product_name_validated = validate_inputs(str, "name product")
            price_validated = validate_inputs(float,"price",True)
            quantity_validated = validate_inputs(int,"quantity",True)
            
            inventorylist = inventory_register(product_name_validated,quantity_validated,price_validated,inventorylist)
            inventory_valeu = inventory_valeu + (quantity_validated*price_validated)
            number_of_units = number_of_units + quantity_validated
          
        elif option == "2":
            if not inventorylist:
                print("Error: Need inventory first.")
                continue
            #This is the option to create a new product in the product database.
            show_summary(inventorylist)
            
        elif option == "3" :
            if not inventorylist:
                print("Error: Need inventory first.")
                continue
            print(f"The total number of products registered was {len(inventorylist)}, {number_of_units} units were stored, and the total inventory value is {inventory_valeu}")
        
        elif option == "4" :
            if not inventorylist:
                print("Error: Need inventory first.")
                continue
            def Search_product (inventorylist):
                
        elif option == "0" :   
            print("Program completed, thank you.")

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main(inventorylist,number_of_units,inventory_valeu)
