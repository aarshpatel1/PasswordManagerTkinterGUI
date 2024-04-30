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

# try:
#     file = open("a_file.txt")
#     dictionary = {"key": "value"}
#     print(dictionary["not_existing_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Hello World!")
# except KeyError as not_existing_key:
#     print(f"The key {not_existing_key} is not existing.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError("This is an error that I made up.")


# BMI Example

# height = float(input("Height in meters: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)
