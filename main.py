from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    # shuffled the password_list and placed character in random order
    shuffle(password_list)

    # joined the password_list into a string
    random_password = "".join(password_list)

    # inserted randomly generated password into the password_input field
    password_input.insert(0, random_password)

    # copies the randomly generated password into the clipboard as soon as the generate password button get clicked
    pyperclip.copy(random_password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_input.get()

    if website == "":
        messagebox.showerror(title="Error", message="You forgot to enter the website...!")
    else:
        with open("password_data.json", "r") as password_data:
            data = json.load(password_data)
            try:
                registered_email = data[website]["email"]
                registered_password = data[website]["password"]
            except KeyError as website_name:
                messagebox.showerror(title="Error", message=f"No password data found of {website_name}.")
            except FileNotFoundError:
                messagebox.showerror(title="Error", message="No password data file is found.")
            else:
                messagebox.showinfo(title=website,
                                    message=f"Email: {registered_email}\nPassword: {registered_password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # gets input from the input fields
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # a dictionary type format what json file needs
    new_password_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # checks whether an input field is not empty and if it is than shows an error messagebox (pop-up)
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="You forgot to enter the details...!")
    else:
        is_yes = messagebox.askyesno(title=website, message=f"Email: {email}\nPassword: {password}\n"
                                                            f"\n Do you want to save this data?")

        # creates or opens password_data.txt file in append mode and stores the password
        if is_yes:
            # storing password data into .txt file
            # with open("password_data.txt", "a") as password_data:
            #     password_data.write(f"{website} | {email} | {password}\n")

            # storing data into .json file
            try:
                with open("password_data.json", "r") as password_data:
                    # reads the old data inside the json file
                    data = json.load(password_data)
                    # updates the old data with new data
                    data.update(new_password_data)
            except FileNotFoundError:
                with open("password_data.json", "w") as password_data:
                    # writes a new data into json file
                    json.dump(new_password_data, password_data, indent=4)
            else:
                with open("password_data.json", "w") as password_data:
                    # writes a new data (updated) into json file
                    json.dump(data, password_data, indent=4)

            # deletes the past inputs and focuses on the website_input field again
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
# creates GUI based output screen using Tk class from the tkinter module
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

# creates the canvas for showing logo image
canvas = Canvas(height=200, width=200, highlightthickness=0)

# specifies the logo image file and path
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
website_label.config(pady=15)

# website input
website_input = Entry(width=25)
website_input.grid(column=1, row=1)
website_input.focus()

# search button
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1)

# email label
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

# email input
email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "aarsh@gmail.com")

# password label
password_label = Label(text="Password")
password_label.grid(column=0, row=3)
password_label.config(pady=15)

# password input
password_input = Entry(width=25)
password_input.grid(column=1, row=3)

# generate button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# holds the output screen open while running the program and until click the close button
window.mainloop()
