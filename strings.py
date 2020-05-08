# 1. Create a variable and assign it the string "Just do it!"

ex_1 = "Just do it!"

# 2. Access the "!" from the variable by index and print() it

print(ex_1[10])

# 3. Print the slice "do" from the variable

print(ex_1[5:7])

# 4. Get and print the slice "it!" from the variable
sliced_1 = ex_1[8:]
print(sliced_1)

# 5. Print the slice "Just" from the variable

print(ex_1[0:4])

# 6. Get the string slice "do it!" from the variable and concatenate it with the
# string "Don't ".  Print the resulting string.

sliced = ex_1[5:]
sliced_2 = "Don't"
print(sliced + " " + sliced_2)
