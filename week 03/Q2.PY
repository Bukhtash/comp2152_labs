cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("\nNumber of apples:", cart.count("apple"))
print("Position of milk:", cart.index("milk"))

cart.remove("apple")
removed_item = cart.pop()  

print("Removed item using pop:", removed_item)
print("Is banana in cart?", "banana" in cart)
print("Final cart:", cart)
