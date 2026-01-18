# Sample Coding Questions 01 Week 01
# Mukhtar Ali


# Defining Variables

numbers = [1, 4, 7, 9]
print("Array:", numbers)

# Order of Operations

a = 1
b = 2
c = 3
d = 4

# Fully bracketed version of:
# e = a - b ** c // d + a % c
e = a - ((b**c) // d) + (a % c)
print("Value of e:", e)

# Formatting

temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))


# Common Functions (User Input)

userAge = int(input("Enter your age: "))
userAge = userAge + 22
print("Now showing the shop items filtered by age:", userAge)
