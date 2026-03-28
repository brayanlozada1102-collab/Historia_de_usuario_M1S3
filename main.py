from app import validate_inputs, inventory_register, show_summary, search_product, update_product, delete_product, calculate_statistics
from files import save_as_csv, load_csv

inventorylist = []
def main(inventorylist):
    
    #This is the introduction message
    print("--- Inventory System S3 ---")

    #We run the program In a while loop, so the program only stop when we decide.  
    option = ":)"
    while option != "0" :
        #This is the menu options.
        print("\n1. Register Product \n2. View Inventory \n3. Search by name \n4. Update Product \n5. Delete Product \n6. Show Statistics \n7. Save as .csv \n8. Load .csv \n0. Exit")
        option = input("Select an option: ")
        
        if option == "1":
            #The first option is to create a new user in the user database.
            product_name_validated = validate_inputs(str, "name product")
            price_validated = validate_inputs(float,"price",True)
            quantity_validated = validate_inputs(int,"quantity",True)
            
            inventorylist = inventory_register(product_name_validated,quantity_validated,price_validated,inventorylist)

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
            name = validate_inputs(str, "name to search")
            product = search_product(inventorylist, name)
            print(product if product else "Not found.")
        
        elif option == "4" :
            if not inventorylist:
                print("Error: Need inventory first.")
                continue
            updatename = validate_inputs(str, "name to update")
            newproduct = validate_inputs(float,"new price (0 to skip)",True)
            newquantity = validate_inputs(int,"new Quantity (0 to skip)",True)
            if update_product(inventorylist, updatename, newproduct if newproduct > 0 else None, newquantity if newquantity > 0 else None):
                print("Update.")
            else: print("Not found.")            
        
        elif option == "5" :
            if not inventorylist:
                print("Error: Need inventory first.")
                continue     
            deletename = validate_inputs(str, "name to delete")
            if delete_product(inventorylist, deletename): 
                print("Deleted.")
            else: print("Not found.")

        elif option == "6" :
            statistics = calculate_statistics(inventorylist)
            if statistics:
                print(f"Total units: {statistics['units']} | Total Valeu: ${statistics['valeu']:.2f}")
                print(f"Most Expensive: {statistics['expensive'][0]} (${statistics['expensive'][1]})")
                print(f"Largets stock: {statistics['stock'][0]} ({statistics['stock'][1]} units)")
            else: print("No data.")

        elif option == "7" :

            path = validate_inputs(str,"File path (e.g., data.csv): ")
            msg = save_as_csv(inventorylist, path)
            print(msg)

        elif option == "8" :
            path = validate_inputs(str,"Route to load: ")
            new_inventory, error = load_csv(path)
            if new_inventory is not None:
                op_c = input("Overwrite current inventory? (Y/N):").upper()
                if op_c == "Y":
                    inventorylist = new_inventory
                    print("Replaced Inventory.")
                else:
                    # Merge: add quantities, update price
                    for new_product in new_inventory:
                        old_product = search_product(inventorylist, new_product["nombre"])
                        if old_product:
                            old_product["cantidad"] += new_product["cantidad"]
                            old_product["precio"] = new_product["precio"]
                        else:
                            inventorylist.append (new_product)
                    print("Merged inventory (quantities added together).")
                print(f"Load complete. Invalid rows skipped.: {error}")
            else: print(error)

        elif option == "0" :   
            print("Program completed, thank you.")

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main(inventorylist)
