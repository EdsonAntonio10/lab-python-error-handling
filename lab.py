
# LAB | ERROR HANDLING


# Función 1: Inicializar inventario con manejo de errores
def initialize_inventory(products):
    inventory = {}
    for product in products:
        while True:
            try:
                quantity = int(input(f"Enter the quantity of {product}s available: "))
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                inventory[product] = quantity
                break
            except ValueError as e:
                print(f"Error: {e}")
    return inventory


# Función 2: Calcular precio total con manejo de errores
def calculate_total_price(products):
    total_price = 0
    product_prices = {}
    for product in products:
        while True:
            try:
                price = float(input(f"Enter the price of {product}: "))
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                product_prices[product] = price
                total_price += price
                break
            except ValueError as e:
                print(f"Error: {e}")
    return total_price, product_prices


# Función 3: Obtener pedidos de clientes con manejo de errores
def get_customer_orders(inventory):
    orders = {}

    # Número de productos diferentes a pedir
    while True:
        try:
            num_orders = int(input("Enter the number of different products the customer wants to order: "))
            if num_orders <= 0:
                raise ValueError("Number of orders must be positive.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Pedir cada producto
    for i in range(num_orders):
        while True:
            product_name = input(f"Enter product name for order {i+1}: ")
            if product_name not in inventory:
                print("Error: Product does not exist in inventory.")
                continue
            if inventory[product_name] == 0:
                print("Error: Product out of stock.")
                continue

            # Pedir cantidad del producto
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {product_name} (max {inventory[product_name]}): "))
                    if 0 < quantity <= inventory[product_name]:
                        orders[product_name] = orders.get(product_name, 0) + quantity
                        inventory[product_name] -= quantity
                        break
                    else:
                        print(f"Error: Enter a quantity between 1 and {inventory[product_name]}")
                except ValueError:
                    print("Error: Please enter a valid integer quantity.")
            break

    return orders



# BLOQUE PRINCIPAL

products_list = ["apple", "banana", "orange"]

print("=== Initialize Inventory ===")
inventory = initialize_inventory(products_list)
print("Inventory:", inventory)

print("\n=== Calculate Total Price ===")
total, prices = calculate_total_price(products_list)
print("Total price:", total)
print("Prices by product:", prices)

print("\n=== Get Customer Orders ===")
orders = get_customer_orders(inventory)
print("Customer orders:", orders)
print("Updated inventory:", inventory)