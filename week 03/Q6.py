

inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8),
}

print("\n=== Current Inventory ===")
for product, (price, qty) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {qty}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
all_products = electronics | accessories

print("\nAll product categories:", all_products)

price_list = [info[0] for info in inventory.values()]
print("\nPrice list:", price_list)

sorted_prices = sorted(price_list)
print("Sorted prices:", sorted_prices)
print(f"Lowest price: ${sorted_prices[0]:.2f}")
print(f"Highest price: ${sorted_prices[-1]:.2f}")


inventory["Headphones"] = (49.99, 20)

mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

del inventory["Monitor"]

print("\n=== Final Inventory ===")
for product, (price, qty) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {qty}")
