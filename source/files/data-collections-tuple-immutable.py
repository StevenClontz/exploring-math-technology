triple_list = ["one", "two", "three"]
triple_tuple = ("one", "two", "three")

# Attempts indented block of code that may cause an error
try:
    print("Trying to change 'two' to 2 in the list.")
    # Replace this line to change triple_list appropriately
# Handles possible error
except TypeError:
    print("This should never appear since list elements can be replaced.")

# Attempts indented block of code that may cause an error
try:
    print("Trying to change 'three' to 3 in the tuple.")
    # Replace this line to try to change triple_list appropriately
# Handles possible error
except TypeError:
    print("This should appear since tuple elements cannot be replaced.")

print(triple_list, triple_tuple) # outputs ['one', 2, 'three'] ('one', 'two', 'three')