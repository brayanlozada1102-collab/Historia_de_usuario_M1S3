# Historia_de_usuario_M1S3
# Inventory Management System S3

A robust, modular Python-based tool for comprehensive inventory control, featuring full CRUD operations, data validation, and CSV persistence.

## Description
This system manages product data (name, price, and quantity) through a professional command-line interface. It focuses on data integrity through a centralized validation module and ensures long-term storage by allowing users to save and load data from external files.

## Features
* **Full CRUD Lifecycle:** Register (Create), View (Read), Search, Update, and Delete products dynamically.
* **Advanced Data Validation:** A unified `validate_inputs` function ensures all data types (int, float, str) are correct and prevents negative values.
* **Persistent Storage:** Export your inventory to `.csv` files and import them later with smart merging logic.
* **Smart Merging:** When loading files, the system can either overwrite the current session or merge data (adding quantities and updating prices for existing items).
* **Inventory Insights:** Calculates total units, total stock value, and identifies outliers (Most Expensive and Largest Stock items).

## Project Structure
* `main.py`: The application's main entry point and user interaction loop.
* `app.py`: Core business logic containing product management functions (`inventory_register`, `search_product`, `update_product`, `delete_product`, etc.).
* `files.py`: Persistence layer handling CSV input/output (`save_as_csv`, `load_csv`).
* `README.md`: Technical documentation and usage guide.

## Requirements
* Python 3.x.
* Ensure `app.py` and `files.py` are located in the same directory as `main.py`.

## Usage Instructions
1.  **Launch:** Run the application from the terminal: `python main.py`.
2.  **Register (1):** Provide the name, unit price, and quantity. The system rejects negative values or non-numeric inputs.
3.  **Manage (2-5):** View the full summary, search for a specific product, update details (price/quantity), or delete an item.
4.  **Statistics (6):** View a detailed report of total units, total value, and product highlights.
5.  **Persistence (7-8):** * **Save:** Export current data to a `.csv` file.
    * **Load:** Import data from a file. Choose **'Y'** to overwrite or **'N'** to merge with the current inventory.
6.  **Exit (0):** Safely close the program.

## Example Execution
```text
--- Inventory System S3 ---

1. Register Product 
2. View Inventory 
3. Search by name 
4. Update Product 
5. Delete Product 
6. Show Statistics 
7. Save as .csv 
8. Load .csv 
0. Exit
Select an option: 1
Enter name product: Sugar
Enter price: 1.50
Enter quantity: 20
Product Sugar successfully registered!

Select an option: 6
Total units: 20 | Total Value: $30.00
Most Expensive: Sugar ($1.5)
Largest stock: Sugar (20 units)

Select an option: 7
File path (e.g., data.csv): backup.csv
Inventory saved in: backup.csv