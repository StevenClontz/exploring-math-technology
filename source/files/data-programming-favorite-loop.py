for number in favorite_numbers:
    # code indented four spaces right will run for each
    # "number" in the list of "favorite_numbers"
    squared = number**2
    print(f"{number} squared is {squared}")
    # TODO add more information about each number
    # (don't forget to indent!)

# Because we removed the indent, this only
# happens after all numbers are looped through.
print("All done looping!")