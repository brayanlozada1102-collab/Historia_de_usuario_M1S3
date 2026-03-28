import csv

def save_as_csv(inventory, path):
    """Save the inventory to a CSV file."""
    if not inventory:
        return "The inventory is empty. Nothing to store.."
    
    with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            writer.writerows(inventory)
    return f"Inventory stored in: {path}"

def load_csv(path):
    """Load products from a CSV file, validating each row.."""
    products_loaded = []
    errors = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as files:
            reader = csv.DictReader(files)
            # Validate header
            if not all(col in reader.fieldnames for col in ["name", "price", "quantity"]):
                raise ValueError("Invalid header.")
            
            for fila in reader:
                try:
                    # Validate exactly 3 columns and data types
                    name = fila["name"].strip()
                    price = float(fila["price"])
                    quantity = int(fila["quantity"])
                    
                    if price < 0 or quantity < 0: raise ValueError("Invalid valeu in quantity or price")
                    
                    products_loaded.append({
                        "name": name, "price": price, "quantity": quantity
                    })
                except (ValueError, KeyError):
                    errors += 1
        return products_loaded, errors
    except FileNotFoundError:
        return None, "Not found."
    except Exception as error:
        return None, f"Error al cargar: {error}"