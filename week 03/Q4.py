

monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both = monday_class & wednesday_class
either = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one_class = monday_class ^ wednesday_class
is_subset = monday_class <= either

print("\nMonday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both)
print("Attended either class:", either)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one_class)
print("Is Monday subset of all students?", is_subset)
