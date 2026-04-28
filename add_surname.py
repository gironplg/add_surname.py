# Author: Gabriel Giron plata
# GitHub username: gironplg
# Date: 4/29/2026
# Description: This code takes a parameter of first names inputted by the user
# It should use a list comprehension to return a list that contains only those names that start with a "K"
# but with the surname "Kardashian" added at the end of each one

def add_surname(first_name):
    """
    Add the surname "Kardashian" to first names that start with "K" using a list comprehension.

    Args:
    first_names: A list of strings representing the first names.

    Returns:
    A list of strings with the surname added too

    """

    return [name + "Kardashian" for name in first_name if name.startswith("K")]

user_input_string = input("Enter a list of names separated by a comma: ")

user_input_list = [name.strip() for name in user_input_string.split(",")]

kardashian_names_from_user = add_surname(user_input_list)

print("Here are the names with the surname added")
print(kardashian_names_from_user)
