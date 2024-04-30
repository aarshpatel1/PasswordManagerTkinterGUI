# Types of Errors

# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# dictionary = {"key": "value"}
# print(dictionary["not_existing_key"])

# IndexError
# fruits = ["apple", "banana", "cherry"]
# print(fruits[3])


# Exception Handling

try:
    file = open("a_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["not_existing_key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Hello World!")
except KeyError as not_existing_key:
    print(f"The key {not_existing_key} is not existing.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
